# 💧 Droplet Generator (Blender / Cycles)

A procedural tool that scatters realistic water droplets over any mesh surface: condensation on a cold can, rain on glass, sweat on a bottle. Built as a Python script so it works on any object, with the same look every time.

![Thumbnail](renders/thumbnail.jpg)

## Goal
Replace hand-placed droplets with a repeatable generator. The condensation in [redbull-drink](../redbull-drink/) used Geometry Nodes; this project is a script version that works on any object and gives full control over size, spacing, and density.

## Tools
- Python (`bpy`, `bmesh`, `mathutils`)
- Blender 4.x / 5.x, Cycles
- Script: [`scripts/blender/droplet_generator.py`](../../scripts/blender/droplet_generator.py)

## How it works
1. Reads the evaluated target mesh and splits it into triangles in world space.
2. Picks random points on the surface, **weighted by triangle area**, so droplets are evenly spread.
3. Picks a radius with a bias toward small sizes (many small, few large).
4. Rejects any droplet that would overlap an existing one.
5. Builds every droplet as a flattened sphere, oriented along the surface normal and sunk slightly into the surface.
6. Merges all droplets into **one mesh** with a glass-like `Droplet` material (IOR 1.33, transmission 1, roughness 0).

## Settings
| Setting | What it does |
|---|---|
| `count` | Droplets to try to place |
| `min_radius` / `max_radius` | Size range |
| `size_bias` | Higher = more small droplets |
| `flatten` | Height vs width (1 = sphere, 0.5 = flat bead) |
| `sink` | How deep each droplet sits into the surface |
| `gap` | Minimum space between droplets |
| `seed` | Change for a different pattern |

## How to use
1. Open `source/droplet-demo.blend` (or any scene) and select a mesh.
2. In the **Scripting** workspace open `scripts/blender/droplet_generator.py`.
3. Adjust `SETTINGS`, then **Run Script**.
4. Render with **Cycles**.

## Render Settings
- Resolution:
- Samples / denoiser:
- Render time:

## Lessons Learned
- What worked:
- What I'd improve (ideas: drips and trails, drop-size variation by height, merging touching droplets):

## Files
```
droplet-generator/
├── README.md
├── source/          # demo .blend
└── renders/         # final renders, thumbnail.jpg
```
