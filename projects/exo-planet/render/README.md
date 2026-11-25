# 🪐 EXO — Procedural Exoplanet (Blender / Cycles)

A cinematic, fully procedural rust-and-salt exoplanet floating in a star field, lit by a single hard sun with a faint cold blue fill. The planet surface, cloud shell, and star field are all generated with shader nodes (no image textures on the planet), and the final frame is rendered in portrait 4K-class resolution with Cycles.

![Final render](renders/exoplanet.png)

> **Resolution:** 2160 × 3840 (9:16 portrait) · **Renderer:** Cycles (GPU) · **Blender:** 5.2 · Full-resolution render: [`renders/exoplanet.png`](renders/exoplanet.png)

---

## Overview

This project is a planetary-visualisation study built to practice the things that make space renders feel believable:

- **Hero object** — a banded, eroded planet surface built entirely from layered procedural noise
- **Procedural surface storytelling** — warm orange strata, dark iron-red channels, and bright white salt/ice deposits that follow the noise flow
- **Atmosphere & depth** — a slightly oversized cloud shell and a fresnel (Layer Weight) rim to soften the limb
- **Hard sun lighting** — one strong sun lamp plus a cold blue spot fill, falling off into deep shadow at the bottom of the frame
- **Telephoto framing** — a long lens placed far from the planet for a flat, "photographed from orbit" look

## Scene Breakdown

| Element | Details |
|---|---|
| **Planet** | UV sphere (`Sphere`) with the `Material.001` shader: two Noise Textures mixed together, Bump, multiple Color Ramps for the strata colours, a Layer Weight rim, and a second Principled BSDF blended in with a Mix Shader |
| **Clouds** | Separate shell object (`clouds`) scaled to 1.004× the planet, using the `clouds` material: Noise Textures driving a Bump and a Mix Shader between a Principled BSDF and a Transparent BSDF |
| **Star field** | Procedural, built in the `World` shader with a Voronoi Texture into a Color Ramp, plus a Volume Scatter node |
| **Lighting** | `Sun` lamp (white, strength 7.8, ~16° angle) as the key, plus a cyan-blue `Spot` lamp (5 W) as a cold fill |
| **Camera** | `Camera.001`: 250 mm focal length, 36 mm sensor, clip range 1–1200, placed about 130 units from the planet |
| **Animation** | `SphereAction` (planet) and `cloudsAction` (clouds) are keyframed; the scene's frame range is 179–1179 at 24 fps |
| **Compositing** | Compositor node tree: Render Layers → Glare → Denoise → Composite |
| **Extras in the file** | A Sketchfab space station model (8 mesh parts, 3 materials, 13 texture maps), three `Torus` objects, and a large `Cube`, none of which appear in the featured still |

## Technical Details

- **Software:** Blender 5.2
- **Render engine:** Cycles, GPU compute
- **Output:** 2160 × 3840 PNG at 100% resolution scale
- **Samples:** 256 render / 32 viewport, adaptive sampling threshold 0.01
- **Denoising:** enabled (GPU denoise), plus a Denoise node in the compositor
- **Light paths:** Max Bounces 18 (Diffuse 6, Glossy 6, Transmission 18, Volume 2, Transparent 10)
- **Lighting:** 1 Sun + 1 Spot, with the star-field world providing the background
- **Shading:** Principled BSDF–based procedural materials for the planet and the cloud layer
- **Procedural work:** Noise, Voronoi, Color Ramp, Bump, and Layer Weight node networks (no image textures on the planet)
- **Render time:** _add your numbers here_
- **Hardware:** NVIDIA RTX 4050

## Files

```
exoplanet/
├── README.md
├── source/
│   └── exo.blend              # Full Blender scene (~117 MB, Git LFS)
└── renders/
    └── exoplanet.png          # Final 2160 × 3840 render (~10 MB)
```

> Tip: the `.blend` is already zstd-compressed, so Git LFS is the right place for it.

## How to Open

1. Install [Blender](https://www.blender.org/download/) **5.2 or newer** (older versions may not open this file correctly).
2. Open `source/exo.blend` (run `git lfs pull` first if the file is only a few bytes).
3. Make sure the render engine is set to **Cycles**. GPU compute is recommended.
4. Press **F12** to render the current frame, or switch the viewport to **Rendered** to preview.
5. To render the animation, use **Render → Render Animation** (frames 179–1179 at 24 fps), and set an output path in **Output Properties** first.

> ⚠️ The planet and cloud shaders stack several noise layers and a bump map, so expect noticeable render times at full resolution. For quick previews, lower the sample count, keep the denoiser on, or reduce the resolution percentage in **Output Properties**.

## Tips for Modifying the Scene

- **Change the planet's palette:** edit the Color Ramps in the `Material.001` shader (warm strata, dark channels, and white deposits are separate stops).
- **More or less terrain detail:** adjust the scale and detail of the two Noise Texture nodes in `Material.001`.
- **Thicker or thinner clouds:** tweak the `clouds` material's Color Ramp, or change the shell's scale (currently 1.004).
- **Change the mood:** edit the colour and strength of the Sun and the blue Spot lamp.
- **Different framing:** move `Camera.001` or change its focal length (250 mm gives the compressed, telephoto look).
- **Denser or sparser stars:** edit the Voronoi scale and the Color Ramp in the `World` shader.
- **Faster renders:** lower Max Bounces and samples, or reduce the resolution percentage.

## Credits

- Modeling, shading, lighting, and rendering: **Yash** ([@yashvardhansingh442-dev](https://github.com/yashvardhansingh442-dev))
- Space station model (included in the `.blend`, not shown in the final still): downloaded from Sketchfab, _add the author name, model link, and licence here_ (check that the licence, e.g. CC-BY, allows redistribution before publishing the scene file)

## Disclaimer

This is a personal, non-commercial portfolio and learning project. The planet is entirely fictional and is not based on real astronomical data.

## License

Scene file and render: all rights reserved, see [LICENSE-ARTWORK.md](../../LICENSE-ARTWORK.md). Shared for portfolio and learning purposes only. Third-party assets (the space station model) remain under their original licences.
