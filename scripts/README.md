# 🛠 Scripts & Automation

Python helpers that automate repetitive parts of my 3D pipeline. All code here is MIT licensed (see the [root LICENSE](../LICENSE)).

## Structure

```
scripts/
├── blender/    # runs inside Blender (bpy)
├── resolve/    # DaVinci Resolve scripting API
└── utils/      # standalone helpers, no 3D software needed
```

## Index

| Script | Software | What it does | Status |
|---|---|---|---|
| [`blender/droplet_generator.py`](blender/droplet_generator.py) | Blender 4.x / 5.x | Scatters non-overlapping water droplets over the selected mesh | 🚧 In progress |
| [`utils/new_project.py`](utils/new_project.py) | Python 3 | Creates a project folder with standard subfolders and README | ✅ Stable |
| `blender/batch_render.py` | Blender | Renders several cameras or scenes unattended | 📝 Idea |

**Status key:** ✅ Stable · 🚧 In progress · 🧪 Experimental · 📝 Idea

## Running a script

**Inside Blender:** open the **Scripting** workspace → **Open** the file → **Run Script** (▶ or `Alt + P`).

**Headless:**

```bash
blender -b path/to/scene.blend -P scripts/blender/<script>.py -- --option value
```

`-b` runs without UI, `-P` runs the script, and everything after `--` is passed to the script instead of Blender.

**Standalone utilities:**

```bash
python scripts/utils/new_project.py my-project-name
```

## Writing a new script

- Put it in the matching subfolder, named in `snake_case` by what it does.
- Start with a docstring: purpose, software and version, usage, author, license.
- Accept arguments instead of hard-coding paths; use `bpy.path.abspath("//")` for paths relative to the `.blend`.
- Don't change the user's scene unexpectedly, print clear progress, and fail early if a required object or camera is missing.
- Add a row to the index above and to the subfolder's README.

## Troubleshooting

| Problem | Likely fix |
|---|---|
| `blender: command not found` | Add Blender to your PATH or call it by full path |
| `No module named 'bpy'` | Blender scripts must run inside Blender (`blender -b ... -P script.py`), not plain `python` |
| Script ignores my arguments | Put `--` before your arguments |
| Render uses CPU, not GPU | Set the compute device in Preferences or in the script |
