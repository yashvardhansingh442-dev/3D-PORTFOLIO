<div align="center">

# 🎬 3D Portfolio

**My complete 3D work in one place: projects, assets, materials, animation, motion graphics, and the tools I build to speed it all up.**

![Primary Tool](https://img.shields.io/badge/Primary-Blender-orange?logo=blender&logoColor=white)
![Grading](https://img.shields.io/badge/Color-DaVinci%20Resolve-red)
![Python](https://img.shields.io/badge/Automation-Python-3776AB?logo=python&logoColor=white)
![Git LFS](https://img.shields.io/badge/Git%20LFS-enabled-success)
![License](https://img.shields.io/badge/License-MIT%20%2B%20All%20Rights%20Reserved-green)

<!-- Replace with your best render (recommended width: 1600px, compressed JPG) -->
![Hero render](https://github.com/yashvardhansingh442-dev/3D-PORTFOLIO/blob/d6f0156b265755fe4baa0788c2aa94d61e8263ee/docs/RENDER.png)

</div>

---

## 📑 Table of Contents

1. [About](#-about)
2. [Featured Work](#-featured-work)
3. [All Projects](#-all-projects)
4. [Skills & Disciplines](#-skills--disciplines)
5. [Tools & Software](#-tools--software)
6. [Repository Structure](#-repository-structure)
7. [Assets, Materials & Shaders](#-assets-materials--shaders)
8. [Scripts & Automation](#-scripts--automation)
9. [Pipeline](#-pipeline)
10. [Getting Started](#-getting-started)
11. [Render & Export Settings](#-render--export-settings)
12. [Conventions](#-conventions)
13. [Roadmap](#-roadmap)
14. [License](#-license)
15. [Contact](#-contact)

---

## 🧭 About

This repository is the home for **all of my 3D work**, whatever the software. It holds finished projects with process breakdowns, reusable assets and materials, animation and motion graphics work, and the scripts I write to automate repetitive tasks.

**What you'll find here**

- Polished 3D projects with renders, breakdowns, and source files
- Reusable models, materials, shaders, and node setups
- Animation, motion graphics, and compositing work
- Scripts and tools that automate parts of the pipeline
- Notes on workflow, settings, and lessons learned

**Why it exists**

- To keep every project versioned, organized, and reproducible
- To document my process so each project teaches me something for the next
- To show both the artistic and the technical side of my work

---

## 🌟 Featured Work

<!-- Pick your 3-4 strongest pieces. Keep thumbnails the same size. -->

| Project | Category | Tools | Preview |
|---|---|---|---|
| [Project Name](projects/project-name/) | Product visualization | Blender, Cycles, DaVinci Resolve | ![](projects/project-name/renders/thumb.jpg) |
| [Project Name](projects/project-name-2/) | Hard-surface modeling | Blender | ![](projects/project-name-2/renders/thumb.jpg) |
| [Project Name](projects/project-name-3/) | Animation / motion | Blender, DaVinci Resolve | ![](projects/project-name-3/renders/thumb.jpg) |

> Every project folder has its own README with a full process breakdown.

---

## 🗃 All Projects

| # | Project | Category | Tools | Status | Year |
|---|---|---|---|---|---|
| 01 | [Project Name](projects/project-name/) | Product viz | Blender | ✅ Complete | 2026 |
| 02 | [Project Name](projects/project-name-2/) | Modeling | Blender | 🚧 In progress | 2026 |
| 03 | _Next project_ | — | — | 📝 Planned | — |

**Categories used:** Product viz · Hard-surface · Character · Environment · Animation · Motion graphics · VFX · Procedural / generative · Experiments

---

## 🎯 Skills & Disciplines

| Discipline | What's covered |
|---|---|
| **Modeling** | Hard-surface and organic modeling, clean topology, modifiers |
| **Sculpting** | Detail sculpting, retopology workflow |
| **Texturing & Shading** | PBR materials, procedural textures, UV unwrapping |
| **Lighting** | Studio setups, HDRI lighting, mood and contrast control |
| **Camera & Composition** | Lens choice, framing, depth of field |
| **Rigging & Animation** | Basic rigs, keyframe animation, camera moves |
| **VFX & Simulation** | Physics, particles, fluid and cloth |
| **Rendering & Compositing** | Render optimization, denoising, render passes |
| **Motion Graphics** | Titles, product ads, animated sequences |
| **Color Grading** | Final grade and finishing |
| **Automation** | Python scripting, batch tools, pipeline helpers |

---

## 🧰 Tools & Software

| Stage | Tool | Notes |
|---|---|---|
| 3D creation (primary) | **Blender 5.0** | Modeling, sculpting, rigging, animation, simulation |
| Rendering | **Cycles** | GPU rendering with denoising |
| Color grading & editing | **DaVinci Resolve** | Final grade and delivery |
| Automation | **Python** | Blender `bpy` scripts and helpers |
| _Other tools_ | _add any others you use_ | _e.g. texturing, image editing, other 3D packages_ |

**Hardware:** NVIDIA RTX 4050

---

## 🗂 Repository Structure

```
3d-portfolio/
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes              # Git LFS tracking rules
│
├── projects/                   # One folder per project, any software
│   └── <project-name>/
│       ├── README.md           # Goal, tools, process breakdown, lessons
│       ├── source/             # Project files (.blend, etc.)
│       ├── renders/            # Final renders, thumbnails, turntables
│       ├── exports/            # FBX / OBJ / USD / GLB deliverables
│       ├── references/         # Reference images and mood boards
│       ├── textures/           # Project-specific textures
│       └── post/               # Compositing and grading project files
│
├── assets/                     # Reusable models and props
│   └── <asset-name>/
│       ├── model files
│       ├── preview.png
│       └── notes.md
│
├── materials/                  # Reusable materials, shaders, node groups
│   └── <material-name>/
│       ├── source file
│       ├── preview.png
│       └── notes.md            # Inputs, outputs, how it works
│
├── scripts/                    # Automation, grouped by software
│   ├── README.md
│   ├── blender/
│   ├── resolve/
│   └── utils/
│
├── presets/                    # Render, export, and color presets
│
└── docs/                       # Workflow notes, guides, images
    ├── images/
    └── workflow.md
```

---

## 🎨 Assets, Materials & Shaders

| Item | Type | Description | Preview |
|---|---|---|---|
| [Asset Name](assets/asset-name/) | Model | Short description | ![](assets/asset-name/preview.png) |
| [Material Name](materials/material-name/) | Procedural material | What it does, what it exposes | ![](materials/material-name/preview.png) |

**Using a Blender asset or material in your own file**

1. **File → Append** in Blender
2. Select the `.blend` file from the asset or material folder
3. Open the `Material`, `NodeTree`, or `Collection` folder and pick the item
4. Adjust the exposed inputs

Non-Blender assets are provided in portable formats (FBX, OBJ, USD, GLB) where possible.

---

## 🛠 Scripts & Automation

| Script | Software | Description | Usage |
|---|---|---|---|
| `scripts/blender/batch_render.py` | Blender | Renders multiple cameras or scenes in one run | `blender -b file.blend -P scripts/blender/batch_render.py` |
| `scripts/<tool>` | _Software_ | One-line description | See `scripts/README.md` |

**Running a Blender script headless**

```bash
blender -b path/to/scene.blend -P scripts/blender/batch_render.py -- --output ./renders --samples 128
```

**Running from inside Blender**

1. Open the **Scripting** workspace
2. Click **Open** and choose the script
3. Click **Run Script** (▶)

---

## 🔄 Pipeline

```
Concept & References
        ↓
Modeling  →  UV Unwrapping
        ↓
Texturing & Shading
        ↓
Rigging & Animation (if needed)
        ↓
Lighting & Camera
        ↓
Render  →  Compositing
        ↓
Color Grade & Edit
        ↓
Final Export
```

1. **Concept & references:** define the goal, collect references, plan shots
2. **Modeling:** block out, refine, clean up topology
3. **Texturing & shading:** UVs, PBR materials, procedural detail
4. **Animation:** rig and animate where the project needs it
5. **Lighting & camera:** build the setup and lock the composition
6. **Rendering:** GPU render with denoising, passes where needed
7. **Post:** compositing, color grade, and edit

More detail in [`docs/workflow.md`](docs/workflow.md).

---

## 🚀 Getting Started

### Requirements

- [Git](https://git-scm.com/) and [Git LFS](https://git-lfs.com/)
- [Blender 5.0+](https://www.blender.org/download/) for `.blend` projects
- Other software as listed in each project's README
- A CUDA/OptiX-capable GPU is recommended for rendering

### Clone the repository

```bash
git lfs install
git clone https://github.com/yashvardhansingh442-dev/3d-portfolio.git
cd 3d-portfolio
```

### Open a project

1. Browse [`projects/`](projects/) and open the project's README
2. Open the file in `source/` with the software listed there
3. If textures look missing, in Blender use **File → External Data → Find Missing Files**

> **Note:** large binary files are stored with Git LFS. If a file looks tiny or won't open, run `git lfs pull`.

---

## ⚙️ Render & Export Settings

Typical settings used across projects (each project README lists exact values):

| Setting | Value |
|---|---|
| Engine | Cycles |
| Device | GPU Compute (OptiX / CUDA) |
| Samples | 128–512, depending on scene |
| Denoiser | OpenImageDenoise / OptiX |
| Color management | AgX / Filmic, per project |
| Intermediate output | OpenEXR or PNG for compositing |
| Final delivery | H.264 / ProRes for video, PNG / JPG for stills |
| Model exports | FBX, OBJ, USD, or GLB, depending on target |

---

## 📐 Conventions

**Naming**

- Project folders: `kebab-case` (`neon-sneaker-ad`)
- Objects: `Category_Name_Variant` (`Prop_Bottle_Glass`)
- Materials: `MAT_Name` · Node groups: `NG_Name`
- Collections by role: `Geo`, `Lights`, `Cameras`, `Refs`

**Commits**

Short, present-tense messages describing the change:

```
Add lighting setup for hero shot
Fix UV seams on bottle cap
Add batch render script
```

**Files**

- Track heavy binaries (project files, EXR/HDR, video, PSD) with Git LFS
- Keep README preview images compressed so pages load quickly
- Don't commit backups, caches, or temp files (covered by `.gitignore`)

---

## 🗺 Roadmap

- [ ] Publish the first full project with a complete breakdown
- [ ] Add 3–5 reusable materials and shaders
- [ ] Add `batch_render.py` and document its options
- [ ] Record turntables for each project
- [ ] Write `docs/workflow.md` covering the full pipeline
- [ ] Add an animation or short-film project
- [ ] Add a motion-graphics / product-ad reel

---

## 📄 License

Code (scripts and tools) is released under the [MIT License](LICENSE).

Artwork, renders, models, and project files are © Yash, all rights reserved, unless a project's README states otherwise. You're welcome to learn from the process, but please ask before reusing the artwork.

---

## 📬 Contact

- **GitHub:** [@yashvardhansingh442-dev](https://github.com/yashvardhansingh442-dev)
- **ArtStation:** _add link_
- **Portfolio:** https://www.behance.net/avusingh
- **LinkedIn:** _add link_
- **Email:** _add address_

Feedback and collaboration ideas are welcome. Open an issue or reach out.

---

<div align="center">

⭐ If you find something useful here, consider starring the repo.

</div>
