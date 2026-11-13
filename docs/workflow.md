# Workflow

How I take a 3D project from idea to portfolio piece.

```
Concept & references → Modeling → UVs → Texturing & shading
  → Rigging & animation (if needed) → Lighting & camera
  → Render → Compositing → Color grade → Export
```

## 1. Reference and planning
- Collect references and a mood board in `projects/<name>/references/`
- Define the goal: what should this piece show?

## 2. Modeling
- Software: Blender
- Naming: `Category_Name_Variant` for objects, collections by role (`Geo`, `Lights`, `Cameras`, `Refs`)

## 3. Materials and lighting
- Reusable materials go in `materials/` (`MAT_Name`, node groups `NG_Name`)
- Render engine: Cycles, GPU (OptiX/CUDA) with denoising

## 4. Animation and simulation (if any)
- Keyframe and camera animation in Blender; physics/particles where the shot needs them

## 5. Rendering
- Stills: 3840 × 2160 PNG, 128–512 samples depending on the scene
- Intermediate output for compositing: OpenEXR or PNG

## 6. Post-processing
- Compositing in Blender's compositor, final grade in DaVinci Resolve

## 7. Publishing
- Full-resolution render: `projects/<name>/renders/final-4k.png` (Git LFS)
- Thumbnail: `projects/<name>/renders/thumbnail.jpg` (800 px wide)
- Update the project README and the table in the main README
