"""Droplet Generator for Blender (condensation / water beads on a surface).

What it does
    Scatters realistic water droplets over the surface of the active mesh
    object. Droplets are flattened, slightly sunk into the surface, sized with
    many small and few large, and never overlap. All droplets are built as ONE
    mesh object with a glass-like "Droplet" material, so it stays fast even
    with thousands of droplets.

How to run
    1. Select the mesh you want covered (a can, a glass, a wall...).
    2. Scripting workspace -> open this file -> edit SETTINGS -> Run Script.
    3. Render with Cycles (droplets are refractive).

Tested target: Blender 4.x / 5.x. If something errors, send me the message.
"""
import math
import random

import bmesh
import bpy
from mathutils import Matrix, Vector

# ----------------------------- SETTINGS ------------------------------------
SETTINGS = {
    "count": 600,            # how many droplets to TRY to place
    "min_radius": 0.002,     # smallest droplet radius (scene units)
    "max_radius": 0.010,     # largest droplet radius
    "size_bias": 3.0,        # >1 = more small droplets, 1 = uniform sizes
    "flatten": 0.55,         # droplet height vs width (1 = perfect sphere)
    "sink": 0.25,            # how deep it sits in the surface (0 to 0.5)
    "gap": 0.0005,           # minimum space between droplets
    "seed": 1,               # change for a different pattern
    "segments": 12,          # droplet smoothness (u); rings = segments // 2
    "max_attempts_per_drop": 20,
    "collection": "Droplets",
}
# ---------------------------------------------------------------------------


def get_target():
    obj = bpy.context.active_object
    if obj is None or obj.type != "MESH":
        raise RuntimeError("Select a mesh object first (the surface to cover).")
    return obj


def sample_surface(obj):
    """Return a list of triangles in world space: (p0, p1, p2, n0, n1, n2, area)."""
    depsgraph = bpy.context.evaluated_depsgraph_get()
    eval_obj = obj.evaluated_get(depsgraph)
    mesh = eval_obj.to_mesh()
    mesh.calc_loop_triangles()

    mw = obj.matrix_world
    normal_mat = mw.to_3x3().inverted_safe().transposed()
    tris = []
    for lt in mesh.loop_triangles:
        v = [mesh.vertices[i] for i in lt.vertices]
        p = [mw @ x.co for x in v]
        n = [(normal_mat @ x.normal).normalized() for x in v]
        area = ((p[1] - p[0]).cross(p[2] - p[0])).length * 0.5
        if area > 1e-12:
            tris.append((p[0], p[1], p[2], n[0], n[1], n[2], area))
    eval_obj.to_mesh_clear()
    if not tris:
        raise RuntimeError("Target mesh has no usable faces.")
    return tris


def random_point(tris, weights, rng):
    p0, p1, p2, n0, n1, n2, _ = rng.choices(tris, weights=weights, k=1)[0]
    a, b = rng.random(), rng.random()
    if a + b > 1.0:
        a, b = 1.0 - a, 1.0 - b
    c = 1.0 - a - b
    pos = p0 * c + p1 * a + p2 * b
    nrm = (n0 * c + n1 * a + n2 * b).normalized()
    return pos, nrm


def place_droplets(tris, s):
    rng = random.Random(s["seed"])
    weights = [t[6] for t in tris]
    placed = []  # (position, radius)
    for _ in range(s["count"]):
        for _try in range(s["max_attempts_per_drop"]):
            r = s["min_radius"] + (s["max_radius"] - s["min_radius"]) * (
                rng.random() ** s["size_bias"]
            )
            pos, nrm = random_point(tris, weights, rng)
            ok = True
            for q, qr, _n in placed:
                if (pos - q).length < r + qr + s["gap"]:
                    ok = False
                    break
            if ok:
                placed.append((pos, r, nrm))
                break
    return placed


def build_mesh(placed, s):
    bm = bmesh.new()
    segs = max(6, int(s["segments"]))
    for pos, r, nrm in placed:
        res = bmesh.ops.create_uvsphere(
            bm, u_segments=segs, v_segments=max(4, segs // 2), radius=1.0
        )
        rot = nrm.to_track_quat("Z", "Y").to_matrix().to_4x4()
        scale = Matrix.Diagonal((r, r, r * s["flatten"], 1.0))
        # centre sits at the surface, pushed slightly into it by "sink"
        centre = pos - nrm * (r * s["flatten"] * s["sink"])
        mat = Matrix.Translation(centre) @ rot @ scale
        bmesh.ops.transform(bm, matrix=mat, verts=res["verts"])
    for f in bm.faces:
        f.smooth = True
    return bm


def get_droplet_material():
    mat = bpy.data.materials.get("Droplet")
    if mat:
        return mat
    mat = bpy.data.materials.new("Droplet")
    mat.use_nodes = True
    bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")

    def setv(names, value):
        for name in names:
            if name in bsdf.inputs:
                bsdf.inputs[name].default_value = value
                return

    setv(["Base Color"], (1.0, 1.0, 1.0, 1.0))
    setv(["Roughness"], 0.0)
    setv(["IOR"], 1.33)
    setv(["Transmission Weight", "Transmission"], 1.0)
    return mat


def main():
    s = SETTINGS
    target = get_target()
    tris = sample_surface(target)
    placed = place_droplets(tris, s)

    bm = build_mesh(placed, s)
    mesh = bpy.data.meshes.new(f"Droplets_{target.name}_mesh")
    bm.to_mesh(mesh)
    bm.free()
    mesh.materials.append(get_droplet_material())

    obj = bpy.data.objects.new(f"Droplets_{target.name}", mesh)
    coll = bpy.data.collections.get(s["collection"])
    if coll is None:
        coll = bpy.data.collections.new(s["collection"])
        bpy.context.scene.collection.children.link(coll)
    coll.objects.link(obj)

    print(f"Placed {len(placed)} of {s['count']} droplets on {target.name}")


if __name__ == "__main__":
    main()
