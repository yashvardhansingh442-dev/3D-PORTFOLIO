# Blender 3D Modelling: The Complete Basics Guide

A start-to-end reference for Pillar 1. It covers the mindset, interface, core concepts, tools, modifiers, topology, workflow, cleanup, and troubleshooting, with tips and tricks throughout.

Shortcuts assume Blender 4.x with the default keymap. Where a feature changed between versions, it is noted.

---

## Table of Contents

1. [What modelling actually is](#1-what-modelling-actually-is)
2. [Setup before you start](#2-setup-before-you-start)
3. [Navigating the viewport](#3-navigating-the-viewport)
4. [Anatomy of a mesh](#4-anatomy-of-a-mesh)
5. [Object Mode vs Edit Mode](#5-object-mode-vs-edit-mode)
6. [Transform basics: G, R, S](#6-transform-basics-g-r-s)
7. [Selection mastery](#7-selection-mastery)
8. [The essential modelling tools](#8-the-essential-modelling-tools)
9. [Modifiers: the non-destructive toolkit](#9-modifiers-the-non-destructive-toolkit)
10. [Topology and edge flow](#10-topology-and-edge-flow)
11. [Shading: smooth, flat, and normals](#11-shading-smooth-flat-and-normals)
12. [Scale, units, and proportions](#12-scale-units-and-proportions)
13. [A professional workflow from blockout to polish](#13-a-professional-workflow-from-blockout-to-polish)
14. [Hard-surface vs organic: first principles](#14-hard-surface-vs-organic-first-principles)
15. [Cleanup and quality checks](#15-cleanup-and-quality-checks)
16. [Common problems and fixes](#16-common-problems-and-fixes)
17. [Guided practice: build a mug](#17-guided-practice-build-a-mug)
18. [Habits that make you faster](#18-habits-that-make-you-faster)
19. [Shortcut cheat sheet](#19-shortcut-cheat-sheet)
20. [Learning roadmap and practice list](#20-learning-roadmap-and-practice-list)

---

## 1. What modelling actually is

A 3D model is a collection of points in space (vertices) connected into surfaces (faces). Modelling is the craft of placing and connecting those points so the shape reads well, deforms well, shades well, and renders efficiently.

There are three big families of modelling:

| Style | Idea | Typical use |
|---|---|---|
| **Polygon / box modelling** | Push and pull vertices, extrude faces | Props, characters, environments, most things |
| **Hard-surface** | Precise, clean, mechanical shapes with bevels | Vehicles, weapons, robots, products |
| **Sculpting** | Push digital clay with brushes | Organic forms, creatures, faces (separate pillar) |

This guide focuses on **polygon modelling**, which underpins everything else.

### The three rules that never change

1. **Block out first, detail last.** Big shapes, then medium shapes, then small details.
2. **Keep it simple.** Fewer vertices, clean lines, no waste.
3. **Look from every angle.** Check front, side, top, and perspective constantly.

---

## 2. Setup before you start

### Preferences worth changing (Edit > Preferences)

- **Interface > Resolution Scale:** raise it if the UI feels small.
- **Input > Emulate Numpad:** enable on laptops with no numpad (then the top-row number keys switch views).
- **Input > Emulate 3 Button Mouse:** helps with trackpads (Alt + left click to orbit).
- **Navigation > Zoom to Mouse Position:** zooming toward your cursor feels far more natural.
- **Navigation > Orbit Around Selection:** the view orbits what you selected.
- **Save & Load:** keep auto-save on and the interval short (2 minutes is fine).
- **Add-ons (enable these):** *Extra Objects*, *LoopTools*, *Node Wrangler* (for later), *Import Images as Planes*.

### Start with a clean scene

The default scene has a cube, a light, and a camera. For modelling you usually want to delete the cube (`X` > Delete) and keep the camera and light, or just delete everything (`A`, then `X`).

### Set up reference images

Reference is not cheating. It is how professionals work.

- Drag an image into the viewport, or use **Add > Image > Reference**.
- Use **front** (`Numpad 1`), **side** (`Numpad 3`), and **top** (`Numpad 7`) views for orthographic references.
- In Object Data properties of the empty, lower the **opacity** and enable **Show in Front** off, so the reference does not hide your model.
- Lock the reference so it cannot be moved by accident (disable selectability in the Outliner using the arrow icon).
- Use **PureRef** (free) on a second monitor for loose reference boards.

**Tip:** Collect 5 to 10 references before modelling: front, side, top, and detail close-ups. Without references, proportions drift quickly.

---

## 3. Navigating the viewport

| Action | Default control |
|---|---|
| Orbit | Middle mouse drag |
| Pan | Shift + middle mouse drag |
| Zoom | Scroll wheel (or Ctrl + middle drag) |
| Front / Back view | `Numpad 1` / `Ctrl + Numpad 1` |
| Right / Left view | `Numpad 3` / `Ctrl + Numpad 3` |
| Top / Bottom view | `Numpad 7` / `Ctrl + Numpad 7` |
| Toggle perspective/orthographic | `Numpad 5` |
| Frame selected | `Numpad .` |
| Frame everything | `Home` |
| Local view (isolate selection) | `Numpad /` |
| Camera view | `Numpad 0` |
| View pie menu | `` ` `` (backtick) |
| Maximize current area | `Ctrl + Space` |

### Display aids

- **X-Ray** (`Alt + Z`): see through the mesh to select hidden vertices.
- **Wireframe view** (`Shift + Z` or `Z` pie): see only the edges.
- **Overlays > Statistics:** shows vertex, edge, face, and triangle counts. Always keep it on.
- **Overlays > Face Orientation:** blue means a face points outward, red means inward.
- **Matcap shading:** in the viewport shading dropdown, matcaps make form easy to read without lighting.

**Tip:** Work in **orthographic** views for proportions and **perspective** to judge form. Switch often.

---

## 4. Anatomy of a mesh

### The building blocks

- **Vertex:** a single point.
- **Edge:** a line connecting two vertices.
- **Face:** a surface bounded by edges. Faces can have 3 sides (**tri**), 4 sides (**quad**), or more (**n-gon**).

### Quads, tris, and n-gons

| Type | Sides | Verdict |
|---|---|---|
| **Quad** | 4 | The standard. Predictable, subdivides cleanly, easy to loop and select. |
| **Tri** | 3 | Fine in flat areas and fine for game engines (everything becomes triangles in the end). Avoid on curved areas you will subdivide. |
| **N-gon** | 5+ | Fine on flat surfaces that will not deform or subdivide. Dangerous on curved surfaces. |

**Golden rule:** model in quads where the surface curves or deforms. Triangles and n-gons are acceptable on flat, hidden, or non-deforming areas.

### Other key concepts

- **Normals:** the direction a face points. Outward-facing normals are required for correct shading and rendering.
- **Manifold (watertight) mesh:** every edge is shared by exactly two faces, with no holes or stray edges. Needed for 3D printing and many simulations.
- **Non-manifold geometry:** open edges, interior faces, or edges shared by three or more faces. Often causes boolean, subdivision, or physics bugs.
- **Poles:** a vertex where **3 or 5+ edges** meet. Five-edge poles are common in character topology, but keep them off the high-curvature or deforming areas.
- **Edge loop:** a connected ring of edges running around the mesh through quads.
- **Origin:** the object's pivot point (the orange dot). It decides where rotation and scaling happen from.
- **Transform data:** location, rotation, scale. Applying scale is crucial (see section 12).

---

## 5. Object Mode vs Edit Mode

Press **Tab** to switch between them.

- **Object Mode:** work on whole objects (move, duplicate, parent, add modifiers, apply transforms).
- **Edit Mode:** work on the mesh itself (vertices, edges, faces).

### Edit Mode selection types

- `1` = Vertex
- `2` = Edge
- `3` = Face

### Handy mode tricks

- **Multi-object editing:** select several meshes, then press `Tab` to edit them all at once.
- **Add objects at the 3D cursor:** new objects appear at the cursor. Reset it with `Shift + C` (this also frames everything), or `Shift + S > Cursor to World Origin`.
- **Object origin tools:** `Object > Set Origin > Origin to Geometry`, or `Origin to 3D Cursor`. Move the cursor to a vertex with `Shift + S > Cursor to Selected` first for custom pivots.
- **Hide and reveal:** `H` hides selected, `Alt + H` reveals all, `Shift + H` hides everything but the selection.

---

## 6. Transform basics: G, R, S

| Key | Action |
|---|---|
| `G` | Grab (move) |
| `R` | Rotate |
| `S` | Scale |

### Constrain to an axis

Press the transform key, then an axis:

- `G` then `Z` moves along Z only.
- `G` then `Shift + Z` moves on X and Y only (excludes Z).
- Press the axis twice to toggle between **global** and **local** axes.

### Type exact values

`G`, `X`, `2`, `Enter` moves exactly 2 units along X. `R`, `Z`, `45`, `Enter` rotates 45 degrees. `S`, `0`, `Enter` flattens a selection to zero on the current plane when combined with an axis (`S`, `Z`, `0`).

### Precision and snapping

- Hold **Ctrl** while transforming to snap in increments.
- Hold **Shift** while transforming for fine, slow control.
- **Snap toggle:** `Shift + Tab`. Set it to **Vertex** to snap vertices onto each other, or **Face Project** to wrap geometry onto another surface.
- **Pivot point** (`.` pie menu): choose between Median Point, 3D Cursor, Individual Origins, Bounding Box Center, or Active Element.
- **Transform orientation** (`,` pie menu): Global, Local, Normal, View, Gimbal.

### Proportional editing (`O`)

Moving one vertex pulls nearby vertices with it, with a falloff. Scroll the mouse wheel while moving to change the influence radius. Perfect for smooth organic adjustments. Switch it off when you want exact, hard edits.

**Tip:** Use **Normal** orientation with `G`, `Z` to move faces straight out along their own direction. This is the secret to precise extrusions on angled surfaces.

---

## 7. Selection mastery

Fast selection is the biggest speed boost for modelling.

### Basics

| Action | Key |
|---|---|
| Select all / none | `A` / `Alt + A` |
| Invert selection | `Ctrl + I` |
| Box select | `B` or drag |
| Circle select | `C` (scroll to resize, middle mouse to deselect) |
| Lasso select | `Ctrl + right mouse drag` |
| Add to selection | `Shift + click` |

### Smart selection

| Action | How |
|---|---|
| **Select an edge loop** | `Alt + click` on an edge |
| **Select an edge ring** | `Ctrl + Alt + click` on an edge |
| **Select linked geometry** | hover and press `L` (or `Ctrl + L` for the selection) |
| **Select by similarity** | `Shift + G` |
| **Grow / shrink selection** | `Ctrl + Numpad +` / `Ctrl + Numpad -` |
| **Select more or less** | same as grow/shrink, based on connectivity |
| **Select loop inner region** | select a closed loop of edges, then `Select > Select Loops > Select Loop Inner-Region` |
| **Select random / checker** | `Select > Select Random` or `Checker Deselect` |
| **Select sharp edges** | `Select > Select Sharp Edges` |
| **Select non-manifold** | `Select > Select All by Trait > Non Manifold` |

**Tip:** When X-Ray is off, box select only selects what you can see. Toggle X-Ray with `Alt + Z` when you need to capture hidden vertices, especially at the back of the mesh.

---

## 8. The essential modelling tools

These ten tools do about 90% of box modelling.

### 1. Extrude (`E`)

Pulls new geometry from selected vertices, edges, or faces.

- Extrude a face, then press `E` again to keep going.
- `E` then `Z`, `1`, `Enter` extrudes exactly 1 unit up.
- **Extrude Along Normals** (`Alt + E` menu) gives you control over how multiple faces extrude.
- **Cancel with right-click or Escape:** the extruded faces are created but not moved, which leaves **duplicate geometry** on top of the original. Always press `Ctrl + Z` after a cancelled extrude, or use `M` to merge by distance.

### 2. Inset (`I`)

Creates a smaller face inside the selected face. Useful for panels, windows, and buttons.

- Press `I` again while inset is active to toggle **Individual** mode (inset each face on its own).
- Hold `Ctrl` for depth. Use the **Operator Panel** (bottom left) to tune thickness and depth.

### 3. Bevel (`Ctrl + B`)

Rounds off or chamfers sharp edges.

- Scroll to add **segments**. 1 segment is a chamfer, 3+ is a smooth round.
- `Ctrl + Shift + B` bevels **vertices**.
- Bevel catches highlights on edges, which is the key to making hard-surface models look real. Almost nothing in the real world has a perfectly sharp edge.

### 4. Loop Cut (`Ctrl + R`)

Adds a ring of edges around the mesh.

- Hover over an edge, scroll up for multiple cuts, then click, then right-click to cancel any slide.
- Click twice to confirm and slide the loop. Press `Esc` after the first click to keep it centred.
- Use **Edge Slide** (`G G`) to adjust loops afterward.

### 5. Knife (`K`)

Cuts new edges freehand.

- Click to place points, `Enter` to confirm.
- Hold `Ctrl` to snap to the midpoint of edges.
- Press `C` to cut through hidden faces (X-Ray style).
- Press `Z` to constrain cuts to the screen axis.
- Alternative: **Knife Project** cuts a shape from a curve or object into a surface.

### 6. Fill (`F`) and Grid Fill

- With 2 vertices selected, `F` creates an edge.
- With 3+ vertices or a boundary loop, `F` creates a face.
- **Grid Fill** (`Face > Grid Fill`) fills a hole with clean quads. Ideal for closing a loop with an even edge count.
- **Bridge Edge Loops** (`Edge > Bridge Edge Loops`) connects two separate loops with faces. Great for joining tubes and cutting holes through shapes.

### 7. Merge (`M`) and Merge by Distance

- `M` merges selected vertices At Center, At Cursor, At First, At Last, or Collapse.
- **Merge by Distance** (`Mesh > Clean Up > Merge by Distance`) welds overlapping vertices automatically. Run it after joining objects or cancelled extrudes.

### 8. Dissolve (`Ctrl + X`)

Removes selected geometry **without leaving a hole**. Unlike `X > Delete`, it keeps the surface intact.

- Dissolve vertices or edges to clean up unnecessary edge loops.
- Use **Limited Dissolve** (`Mesh > Delete > Limited Dissolve`) to reduce flat, coplanar geometry automatically.

### 9. Spin and Screw

Draws a profile, then revolves it around an axis. Used for bottles, vases, pillars, wheels.

- Build the profile as connected vertices on a plane.
- Use **Mesh > Spin** and adjust steps and angle. Merge duplicates at the seam.

### 10. Shrink/Fatten (`Alt + S`)

Scales selected geometry along vertex normals. Use it to thicken or thin a shape evenly, such as a shell or a tire wall.

### Bonus tools

- **Poke faces:** adds a vertex in the centre of a face.
- **Triangulate** (`Ctrl + T`) and **Tris to Quads** (`Alt + J`): convert between polygon types.
- **Solidify:** gives a surface thickness (best as a modifier).
- **Loop Tools (add-on):** *Circle*, *Space*, *Flatten*, and *Curve* tidy up selections quickly. Circle is great for perfect round holes.
- **Edge Slide** and **Vertex Slide** (`G G`): move geometry along existing edges instead of free space.

---

## 9. Modifiers: the non-destructive toolkit

Modifiers (Properties > Wrench icon) change your mesh **without permanently altering it**. You can adjust or remove them at any time. They stack from top to bottom, and **order matters**.

### The essential modifiers

#### Mirror

Model half, get the whole thing for free.

- Place the object origin at the centre of symmetry.
- Enable the axis you want (usually X).
- Enable **Clipping** so vertices on the centre line stay locked there.
- Enable **Merge** so the halves weld at the seam.
- Delete the half you do not need, in Edit Mode, then let the modifier mirror the other half.
- Use an **object as the mirror pivot** for off-centre symmetry.

#### Subdivision Surface (`Ctrl + 1` to `Ctrl + 5`)

Smooths and rounds a low-poly mesh into a soft surface.

- **Levels Viewport** is the display level. **Render** is the final level.
- Add **support loops** near edges to keep them sharp (see section 10).
- Alternatively, use **Edge Crease** (`Shift + E`) to tighten edges without extra loops.
- For heavy models, keep viewport levels low (1 or 2) and render levels higher (3 or 4).

#### Bevel Modifier

Like the Bevel tool, but live and adjustable.

- Set **Limit Method** to **Angle** so only sharp edges bevel automatically.
- Set **Width** and **Segments**, and enable **Harden Normals** if you use custom shading.
- Use **Weight** or **Vertex Group** to control where it applies.

#### Solidify

Adds thickness to a surface.

- Great for cups, panels, shells, and walls.
- Use **Even Thickness** and set a sensible **Offset** (-1 inward, 0 centre, 1 outward).

#### Array

Repeats an object.

- **Relative Offset:** repeats using the object's size (fences, stairs, tiles).
- **Constant Offset:** uses fixed distances.
- **Object Offset:** uses another object's transform. Pair with an Empty to create spirals, circles, and curved patterns.
- **Fit Type > Fit Curve** repeats along a curve.

#### Boolean

Cuts, joins, or intersects shapes.

- **Difference** cuts the second object out of the first. **Union** merges. **Intersect** keeps the overlap.
- Use the **Exact** solver for quality, **Fast** for speed.
- Booleans make messy topology. Use them for **hard-surface concepts, blockouts, and shapes that will not subdivide**. Clean up before using in animation.
- The **Bool Tool** add-on (bundled) makes this faster: select two objects, use `Ctrl + Numpad -` for difference.
- Make the cutting object display as **Wire** or **Bounds** so you can keep seeing the main model.

#### Weighted Normal

Corrects shading on hard-surface models so large flat faces stay clean without artifacts. Typically used with a Bevel modifier.

#### Shrinkwrap

Snaps a mesh onto the surface of another object. Used for retopology and wrapping clothing or panels around shapes.

#### Decimate

Reduces polygon count. Useful for quick optimisation, but results are triangulated and messy.

#### Triangulate

Converts quads to triangles. Add it last in the stack for game exports.

### Modifier stack order examples

**Hard-surface prop:**
Mirror > Bevel > Weighted Normal > Triangulate (export only)

**Smooth organic form:**
Mirror > Subdivision Surface

**Thick shell with rounded edges:**
Solidify > Bevel > Subdivision Surface

### Applying modifiers

Applying (`Ctrl + A` over the modifier) bakes the effect into the mesh. Only apply when necessary. Remember:

- Apply Mirror before sculpting asymmetry or exporting for tools that mishandle it.
- Never apply Subdivision in the middle of the work unless you need the denser mesh.
- Keep a backup version before applying many modifiers.

**Tip:** Use **Show in Edit Mode** and **On Cage** toggles (small icons in each modifier header) to control whether you see modifier results while editing.

---

## 10. Topology and edge flow

Topology is how your edges and faces are arranged. Good topology makes models smooth, easy to edit, and ready for deformation or subdivision.

### What good topology looks like

- Mostly **quads**.
- **Edge loops follow the form**, such as the muscles around the eyes and mouth, or the curve of a car panel.
- **Even density:** quads are roughly square and similar in size, unless you need more detail in specific areas.
- **Poles** placed on flat, low-visibility areas.
- **No unnecessary geometry:** every loop earns its place.

### Support loops (holding edges)

When you subdivide a mesh, corners become round. To keep an edge sharp, place a loop close to it.

- A loop **close** to the edge = a **sharper** result.
- A loop **farther** from the edge = a **softer** result.
- Add supports with `Ctrl + R` and slide them with `G G`.

### Controlling density

- Add geometry only where you need curvature or detail. Flat areas can stay sparse.
- **Dissolve** loops that do not help (`Ctrl + X`).
- Transition between density levels using triangles hidden in flat areas or by "edge flow rerouting" with **Knife** and **Join** tools (`J` connects selected vertices).

### Dealing with poles

- **3-pole (E-pole):** 3 edges meet. Useful at corners.
- **5-pole (N-pole):** 5 edges meet. Common in character topology for redirecting flow.
- Keep poles away from areas that bend a lot or catch strong highlights.
- Do not stack poles in a tight cluster.

### Edge flow for common shapes

- **Cylinders and holes:** loops should circle the hole, with extra loops around it to hold the shape.
- **Eyes and mouth (characters):** concentric loops around the openings.
- **Limbs:** loops around the limb, with extra density at joints (knees, elbows).
- **Hard-surface panels:** loops follow panel borders and bevel edges.

### Test your topology

Add a Subdivision Surface modifier. If you see pinching, lumps, or wobbling, your edge flow needs work. If it stays smooth and holds its shape, you are doing it right.

**Tip:** Press `Alt + Z` and `Shift + Z` often while subdivided to check what the topology is doing under the surface.

---

## 11. Shading: smooth, flat, and normals

### Flat vs smooth shading

- **Shade Flat:** each face has one colour. Faceted look, clearly visible polygons.
- **Shade Smooth:** shading interpolates across faces for a rounded appearance without adding geometry.
- Apply with **Object > Shade Smooth** (or right-click). In Edit Mode, you can set smooth or flat on selected faces only.

### Smooth by Angle (Blender 4.1 and later)

Blender 4.1 removed the old "Auto Smooth" checkbox. Use **Object > Shade Auto Smooth** (it adds the *Smooth by Angle* modifier), then set the angle (commonly 30 to 60 degrees). Edges sharper than the angle stay crisp, and the rest smooth out.

Alternatively, mark individual edges with **Mark Sharp** (`Edge > Mark Sharp`) for exact control.

### Fixing shading artifacts

Weird dark patches or creases on a smooth-shaded surface usually mean one of these:

- **Normals are flipped:** check with the Face Orientation overlay. Fix with `Shift + N` (Recalculate Outside) in Edit Mode.
- **Non-uniform scale:** apply scale with `Ctrl + A > Scale`.
- **N-gons or bad triangulation on curved faces:** reroute the topology.
- **Long thin triangles:** add loops or restructure.
- **Overlapping vertices:** run Merge by Distance.

### Normals tools

- **Recalculate Outside** (`Shift + N`): makes normals face outward.
- **Flip** (`Alt + N > Flip`): reverses selected normals.
- **Overlay > Normals:** display normal direction as lines.

**Tip:** If a transparent or double-sided surface looks wrong, check **Backface Culling** in the material settings and the normals before changing materials.

---

## 12. Scale, units, and proportions

### Always model at real-world scale

- Set **Scene Properties > Units**: Metric, Unit Scale 1.0, Length in meters (or centimeters for small props).
- A default cube is 2 m wide, which is huge for a coffee mug. Scale appropriately.
- Real scale makes lighting, physics, depth of field, and asset sharing work correctly.
- Use a **human-scale reference object** (a 1.8 m box or a mannequin) in scenes.

### Apply your transforms

After scaling an object in Object Mode, press `Ctrl + A > Scale` (or **All Transforms**) so that scale reads `1, 1, 1`. Unapplied scale causes bad bevels, broken modifiers, and shading errors.

### Proportion checking tricks

- **Mirror reference images** to check symmetry mistakes.
- **Flip the viewport:** view the model in the camera mirrored or scale a reference by -1 occasionally to expose errors.
- **Squint test:** zoom far out. Does the silhouette read clearly?
- **Compare against a known object** such as a coin, a hand, or a door.
- **Silhouette check:** switch to a flat dark matcap, or press `Alt + Z` off and view in solid colour, then judge the outline alone.

---

## 13. A professional workflow from blockout to polish

### Stage 1: Plan (5 to 10 minutes)

- Collect references.
- Decide the purpose: still render, animation, game asset, or 3D print. This sets the polygon budget and topology needs.
- Break the object into **primitive shapes** in your head.

### Stage 2: Blockout

- Use simple primitives (cubes, cylinders, spheres) to place large forms.
- Match proportions to the reference in orthographic views.
- Do not add any detail yet. Evaluate silhouette and proportions only.
- Use **different colours or matcaps** per part if it helps readability.

**Rule:** if the blockout does not look right, no amount of detail will rescue it.

### Stage 3: Primary forms

- Refine the main shapes: add loop cuts, adjust vertices, set up the Mirror modifier.
- Merge parts into cleaner, connected meshes where appropriate.
- Check from all angles.

### Stage 4: Secondary forms

- Add medium details: panel lines, inset sections, buttons, holes, handles.
- Add bevels and support loops.

### Stage 5: Tertiary details

- Add small details: screws, grooves, stitching, tiny trims.
- Reuse parts using duplicates (`Alt + D` for linked copies that update together) and Array modifiers.

### Stage 6: Cleanup

- Merge by distance, recalculate normals, delete stray geometry.
- Apply scale and name objects.
- Check topology and shading (see section 15).

### Stage 7: Finalise

- Set shading (smooth and weighted normals).
- UV unwrap and texture (next pillars).
- Organise with collections and export if needed.

### Save versions

Use **File > Save As** with numbers: `mug_v001.blend`, `mug_v002.blend`. Or press `Ctrl + S` often and enable file versions (Preferences > Save & Load). Version files save you when something breaks.

---

## 14. Hard-surface vs organic: first principles

### Hard-surface basics

- Think in **panels, seams, bevels, and mechanical function**.
- Start with clean primitives.
- Use **Booleans** and **Bevel** to build quickly, then clean up.
- Use **Weighted Normals** for clean flat shading with rounded edges.
- Make parts **look like they could be manufactured**: tolerances, gaps, and logical joints.
- **Tip:** Add a tiny bevel to nearly every edge. Sharp 90-degree edges look fake in renders.

### Organic basics

- Think in **flowing forms, volumes, and anatomy**.
- Use **Subdivision Surface** with careful loops.
- Model **half** of symmetrical creatures using Mirror.
- Follow **muscle and bone structure** with edge loops.
- Keep density higher where deformation happens (joints, face).
- Start with a simple low-poly base mesh. Add resolution gradually, or switch to sculpting for details.

### Choosing between them

| Question | Answer |
|---|---|
| Does it have straight, precise edges? | Hard-surface |
| Does it flow, bend, or have a soft form? | Organic |
| Will it be animated or deform? | Organic-style loops, even for mechanical joints |
| Is it a still render prop? | Any approach that looks good |

---

## 15. Cleanup and quality checks

Run through this checklist before calling any model finished.

### The cleanup checklist

- [ ] **Merge by Distance** (`M > By Distance`) to remove overlapping vertices.
- [ ] **No loose vertices or edges:** use `Select > Select All by Trait > Loose Geometry`.
- [ ] **No interior faces:** hidden internal faces cause render and print bugs. Use X-Ray to check.
- [ ] **Non-manifold check:** `Select > Select All by Trait > Non Manifold` should select nothing on a closed mesh.
- [ ] **Normals correct:** use Face Orientation overlay and `Shift + N`.
- [ ] **Scale applied** (`Ctrl + A > Scale`).
- [ ] **Origin placed sensibly** (centre, base, or hinge, depending on use).
- [ ] **No n-gons on curved areas** (select with `Select > Select All by Trait > Faces by Sides`).
- [ ] **Modifiers organised** and in the right order.
- [ ] **Objects named** (`Mug_Body`, `Mug_Handle`) and arranged in collections.
- [ ] **Poly count appropriate** for the purpose.
- [ ] **Triangle test:** for game assets, add a Triangulate modifier to preview.

### Useful checking tools

- **Statistics overlay** for polygon counts.
- **3D-Print Toolbox add-on:** checks for non-manifold edges, thin walls, and overhangs.
- **Mesh Analysis overlay** (Edit Mode overlays): visualises thickness, overhangs, distortion, and sharp edges.
- **Wireframe overlay** to review edge flow quickly.
- **Select Similar > Area or Perimeter** to spot size inconsistencies.

### Poly count budgets (rough guides)

| Purpose | Rough range |
|---|---|
| Mobile game prop | 500 to 5,000 triangles |
| PC / console game prop | 5,000 to 50,000 triangles |
| Hero game asset | 50,000 to 150,000+ triangles |
| Film / still render | Practically unlimited (use subdivision) |

Budgets vary by project. Treat these as starting guidelines, not rules.

---

## 16. Common problems and fixes

| Problem | Likely cause | Fix |
|---|---|---|
| Shading looks dirty or has dark streaks | Flipped normals, unapplied scale, bad topology | `Shift + N`, apply scale, clean up faces |
| Bevel looks uneven | Non-uniform scale | Apply scale (`Ctrl + A`) |
| Subdivision makes pinched corners | Poles or n-gons at the corner | Rework topology, add support loops |
| Mirror leaves a visible seam | Vertices off the centre line | Enable **Clipping**, snap centre vertices to X = 0 (`S`, `X`, `0`) |
| Boolean fails or leaves holes | Non-manifold meshes, coplanar faces | Clean meshes, use the Exact solver, offset cutters slightly |
| Cannot select back vertices | X-Ray is off | `Alt + Z` |
| Extrude made double faces | Cancelled extrude | `Ctrl + Z` right after, or Merge by Distance |
| Object stretches strangely | Non-uniform scale | Apply scale |
| Knife tool misses | View angle or hidden geometry | Enable X-Ray or press `C` for cut-through |
| Loop cut will not appear | Mesh has triangles or n-gons blocking the loop | Rework the area into quads |
| Edges look jagged in the viewport | Low viewport subdivision | Raise viewport levels or enable smooth shading |
| Modifiers affect the wrong thing | Wrong stack order | Reorder modifiers (drag the grip icon) |
| Model is too big or too small | Wrong unit scale | Set units, scale to real size, apply |
| Faces look transparent from behind | Backface culling or flipped normals | Check normals and material setting |
| Blender crashes on heavy models | Subdivision too high | Reduce viewport levels, save often |

---

## 17. Guided practice: build a mug

This builds a mug with a handle using the core tools: cylinder, extrude, inset, solidify, loop cut, subdivision, and the Spin alternative.

### Part A: The body

1. Delete the default cube. Add a cylinder with `Shift + A > Mesh > Cylinder`.
2. In the operator panel set **Vertices** to 32, **Radius** to 0.04 m, **Depth** to 0.095 m (a typical mug).
3. Move it up so it sits on the grid: `G`, `Z`, `0.0475`, `Enter`.
4. Press `Tab`, select the **top face** (`3`), press `I` to inset slightly (about 0.004 m).
5. Press `E` and extrude **down** (`Z`, `-0.088`), forming the hollow interior.
6. Delete nothing yet. Check the thickness from a cross-section by cutting in the viewport using Clipping (`Alt + B`) or use the Bisect tool.

### Part B: Add rounding

1. Select the bottom outer edge loop (`Alt + click`) and the top rim edges.
2. Press `Ctrl + B`, scroll for 3 segments, and bevel slightly.
3. Add a **Subdivision Surface** modifier at level 2 and look at the result. If edges collapse, add support loops near the rim and base with `Ctrl + R`.

### Part C: The handle

1. Add a **Circle** (`Shift + A > Mesh > Circle`) with 16 vertices, small radius (0.008 m).
2. Move it to the side of the mug at the top handle junction. Rotate it so it faces the path of the handle.
3. In Edit Mode, press `F` to fill it, then extrude (`E`) in segments, rotating and moving to create a "C" shape. Use `R` and `G` after each extrude.
4. Alternatively, add a **Bezier Curve**, shape it into a handle, set **Geometry > Bevel > Depth**, and convert to mesh with `Object > Convert > Mesh`.
5. Aim the end faces at the mug body, then use **Bridge Edge Loops** or simply overlap and clean up later.

### Part D: Join and clean

1. Select the handle, then the body (body active), and press `Ctrl + J`.
2. If the shapes overlap, use a Boolean (Union) or delete the faces at the connection and use **Bridge Edge Loops**.
3. Run **Merge by Distance**, check normals, and apply scale.
4. Add **Shade Smooth** (or Smooth by Angle) and finish with a Subdivision modifier.

### Part E: Stretch goals

- Add a **decorative band** around the mug using an inset and extrude.
- Make the mug **chipped** with a small Boolean cut near the rim.
- Create a **matching saucer** using the Spin tool.
- Build a **set of three** mugs with different handle styles.

---

## 18. Habits that make you faster

### Workflow habits

- **Use the numpad views constantly** instead of orbiting. Orthographic views reveal errors that perspective hides.
- **Work in layers of detail:** if you are polishing small details before the silhouette is right, stop.
- **Keep everything symmetrical** until the very end.
- **Duplicate repeating parts** with linked duplicates (`Alt + D`) so a change updates every copy.
- **Name things immediately.** Future you will thank you.
- **Save versions** before risky operations (applying modifiers, booleans, retopology).
- **Take breaks.** Eye fatigue makes proportions look correct when they are not. Come back and look with fresh eyes.

### Speed tips

- **Pie menus:** hold `Z` (shading), `Tab` (mode, in some keymaps), `.` (pivot), `,` (orientation), `` ` `` (view), and `Shift + S` (snap). They are faster than hunting for buttons.
- **Repeat last action:** `Shift + R`.
- **Search for any tool:** `F3` opens the operator search. Type the name and run it.
- **Quick favourites:** `Q` opens a customisable menu.
- **Redo panel:** after most operations, open the operator panel at the bottom left to change values.
- **Duplicate and move:** `Shift + D`, then right-click to cancel the move (keeps the duplicate in place).
- **Use the Outliner:** `Ctrl + click` to select, `H` to hide, and right-click to organise.
- **Move to a collection:** `M` in Object Mode.
- **Quick modifiers:** `Ctrl + 1` through `5` adds Subdivision.
- **Quick smooth:** right-click > Shade Smooth.

### Mindset habits

- **Finish small projects.** Ten finished mugs teach more than one abandoned dragon.
- **Study real objects.** Look at how bevels catch light, how panels meet, how thickness varies.
- **Recreate objects around you.** Desk lamps, bottles, headphones, and chairs.
- **Do not skip fundamentals.** Topology and scale errors compound, and they are painful to fix late.
- **Compare your work** to reference side by side, not memory.
- **Accept ugly early stages.** Everything looks bad at 30% complete.

---

## 19. Shortcut cheat sheet

### General

| Action | Key |
|---|---|
| Add object | `Shift + A` |
| Delete menu | `X` |
| Duplicate | `Shift + D` |
| Linked duplicate | `Alt + D` |
| Join objects | `Ctrl + J` |
| Separate (Edit Mode) | `P` |
| Apply transforms | `Ctrl + A` |
| Undo / Redo | `Ctrl + Z` / `Ctrl + Shift + Z` |
| Search operators | `F3` |
| Repeat last | `Shift + R` |
| Hide / Reveal | `H` / `Alt + H` |
| Snap menu | `Shift + S` |
| Toggle snapping | `Shift + Tab` |
| Proportional editing | `O` |
| Side panel (N panel) | `N` |
| Toolbar | `T` |

### Edit Mode

| Action | Key |
|---|---|
| Vertex / Edge / Face | `1` / `2` / `3` |
| Extrude | `E` |
| Inset | `I` |
| Bevel / Vertex bevel | `Ctrl + B` / `Ctrl + Shift + B` |
| Loop cut | `Ctrl + R` |
| Knife | `K` |
| Fill | `F` |
| Join vertices | `J` |
| Merge | `M` |
| Dissolve menu | `Ctrl + X` |
| Edge slide | `G G` |
| Shrink/Fatten | `Alt + S` |
| Edge menu | `Ctrl + E` |
| Face menu | `Ctrl + F` |
| Vertex menu | `Ctrl + V` |
| Recalculate normals | `Shift + N` |
| Normals menu | `Alt + N` |
| Mark seam / sharp | via Edge menu |
| Triangulate | `Ctrl + T` |
| Tris to Quads | `Alt + J` |
| Edge crease | `Shift + E` |
| Select loop / ring | `Alt + click` / `Ctrl + Alt + click` |

### Viewport

| Action | Key |
|---|---|
| Front / Right / Top | `Numpad 1` / `3` / `7` |
| Opposite views | `Ctrl + Numpad` |
| Perspective toggle | `Numpad 5` |
| Frame selected | `Numpad .` |
| Local view | `Numpad /` |
| X-Ray | `Alt + Z` |
| Wireframe | `Shift + Z` |
| Maximise area | `Ctrl + Space` |

---

## 20. Learning roadmap and practice list

### Progression

| Stage | Focus | Weeks (rough) |
|---|---|---|
| **1. Interface and tools** | Navigation, G R S, selection, extrude, inset, loop cut | 1 to 2 |
| **2. Box modelling** | Simple props, quad-based thinking, Mirror | 2 to 3 |
| **3. Modifiers** | Bevel, Subdivision, Array, Solidify, Boolean | 2 to 3 |
| **4. Topology** | Edge flow, support loops, poles, cleanup | 3 to 4 |
| **5. Hard-surface** | Panels, bevels, Weighted Normals, kitbash thinking | 4 to 6 |
| **6. Organic basics** | Faces, hands, creatures with good loops | 4 to 6 |
| **7. Retopology** | Rebuilding clean meshes over sculpts and scans | 3 to 4 |
| **8. Production habits** | Naming, scale, collections, export | ongoing |

### Practice objects (easy to hard)

**Easy:** cube-based crate, mug, book, pencil, simple chair, dice, bottle.
**Medium:** desk lamp, sneaker, kettle, headphones, bicycle wheel, alarm clock.
**Harder:** camera, motorbike engine parts, sci-fi helmet, car body, stylized character head.

### Daily practice routine (30 to 60 minutes)

1. **5 minutes:** warm up with shortcuts and navigation.
2. **30 minutes:** model one real object from reference.
3. **10 minutes:** cleanup and check with the checklist in section 15.
4. **5 minutes:** compare against reference and note one thing to improve.

### Mistakes to avoid as a beginner

- Starting with complex projects before mastering simple shapes.
- Adding detail before getting proportions right.
- Ignoring scale and normals.
- Applying modifiers too early.
- Using Booleans for everything without cleaning up.
- Never saving versions.
- Skipping reference images.
- Giving up after the first ugly attempt.

### Final reminders

- Good modelling is **planning, patience, and cleanliness**.
- Simple shapes done well beat complex shapes done badly.
- Every professional modeller started with ugly cubes. Keep building, keep finishing, and keep comparing against reality.

---

*End of guide. Pair this with the 21-project list for Pillar 1 in the journey tracker and work through them in order.*
