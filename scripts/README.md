# 🛠 Scripts & Automation

Python scripts and helpers that automate repetitive parts of my 3D pipeline: batch rendering, scene setup, cleanup, and file handling. Everything here is MIT licensed (see the [root LICENSE](../LICENSE)).

---

## 📑 Table of Contents

1. [Folder Structure](#-folder-structure)
2. [Requirements](#-requirements)
3. [Script Index](#-script-index)
4. [How to Run a Script](#-how-to-run-a-script)
5. [Script Details](#-script-details)
6. [Writing a New Script](#-writing-a-new-script)
7. [Troubleshooting](#-troubleshooting)
8. [License](#-license)

---

## 🗂 Folder Structure

```
scripts/
├── README.md          # You are here
└── batch_render.py    # Render multiple cameras/scenes in one run
```

Scripts live directly in this folder. If it grows past about 10 scripts, group them into subfolders (for example `blender/` and `utils/`) and update the index below.

---

## 📋 Requirements

- **Blender 5.0+**: all scripts run in Blender's built-in Python
- No extra pip packages are needed for Blender scripts; they only use `bpy` and the standard library. Any script that needs additional packages lists them in its own header.

---

## 📚 Script Index

| Script | Software | What it does | Status |
|---|---|---|---|
| [`batch_render.py`](batch_render.py) | Blender | Renders multiple cameras or scenes in one run | 🚧 Planned |
| _add next script_ | — | — | 📝 Idea |

**Status key:** ✅ Stable · 🚧 In progress / planned · 🧪 Experimental · 📝 Idea

> Keep this table updated whenever you add, rename, or remove a script.

---

## ▶️ How to Run a Script

### Option 1: Inside Blender (interactive)

1. Open Blender and switch to the **Scripting** workspace
2. Click **Open** and choose the script from `scripts/`
3. Click **Run Script** (▶) or press `Alt + P` in the text editor

Use this when you want to test a script on the scene you currently have open.

### Option 2: Headless from the command line (no UI)

```bash
blender -b path/to/scene.blend -P scripts/<script>.py
```

| Flag | Meaning |
|---|---|
| `-b` | Background mode, no UI |
| `-P` | Run the given Python script |
| `--` | Everything after this is passed to the script, not to Blender |

**Passing arguments to a script**

```bash
blender -b scene.blend -P scripts/batch_render.py -- --output ./renders --samples 128
```

This is the right choice for long renders, batch jobs, and running on another machine.

### Option 3: As a one-off from the Python console

```python
exec(open("scripts/<script>.py").read())
```

---

## 🔍 Script Details

Add one block per script in this format so the README stays useful as the folder grows.

### `batch_render.py`

**Purpose:** Render several cameras, scenes, or frame ranges in a single run, so long jobs can run unattended.

**Usage**

```bash
blender -b scene.blend -P scripts/batch_render.py -- \
    --output ./renders \
    --samples 128 \
    --cameras Cam_Hero Cam_Detail \
    --format PNG
```

**Arguments**

| Argument | Default | Description |
|---|---|---|
| `--output` | `./renders` | Folder where rendered files are saved |
| `--samples` | scene value | Cycles sample count override |
| `--cameras` | all cameras | Space-separated camera names to render |
| `--format` | `PNG` | Output format (`PNG`, `JPEG`, `OPEN_EXR`) |
| `--frame-start` / `--frame-end` | scene range | Frame range for animations |

**Notes**

- Uses the GPU device set in the `.blend` file's Cycles settings
- Output files are named `<scene>_<camera>_<frame>`
- _Update this block to match the final script._

---

## ✍️ Writing a New Script

### Checklist

- [ ] Put it directly in `scripts/` (or a subfolder once the folder grows)
- [ ] Use `snake_case` file names that describe what it does (`batch_render.py`, not `script1.py`)
- [ ] Add the header docstring below
- [ ] Accept arguments instead of hard-coding paths
- [ ] Add a row to the [Script Index](#-script-index) and a block under [Script Details](#-script-details)
- [ ] Test it both interactively and headless (Blender scripts)

### Header template

```python
"""
<script_name>.py

Purpose:  One-line description of what this script does.
Software: Blender 5.0+
Usage:    blender -b scene.blend -P scripts/<script_name>.py -- --option value
Author:   Yash
License:  MIT
"""

import sys
import argparse

import bpy


def parse_args():
    # Blender passes its own flags first; only read what comes after "--"
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else []

    parser = argparse.ArgumentParser(description="Describe the script")
    parser.add_argument("--output", default="./renders", help="Output folder")
    parser.add_argument("--samples", type=int, default=None, help="Cycles samples")
    return parser.parse_args(argv)


def main():
    args = parse_args()
    # ... your logic here ...


if __name__ == "__main__":
    main()
```

### Good habits

- **Don't hard-code absolute paths.** Use arguments or paths relative to the `.blend` file (`bpy.path.abspath("//")`).
- **Don't modify the user's scene unexpectedly.** Restore settings you change, or work on a copy.
- **Print clear progress messages** so headless runs are easy to follow.
- **Fail loudly and early** if a required camera, collection, or object is missing.

---

## 🩺 Troubleshooting

| Problem | Likely fix |
|---|---|
| `blender: command not found` | Add Blender to your PATH, or call it by full path (e.g. `/path/to/blender`) |
| `ModuleNotFoundError: No module named 'bpy'` | The script must run inside Blender. Use `blender -b ... -P script.py`, not plain `python` |
| Script ignores my arguments | Make sure there's a `--` before your arguments on the command line |
| Render uses CPU instead of GPU | Set the compute device in Blender's Preferences, or set it in the script before rendering |
| Output folder is empty | Check the output path is writable and that cameras are named exactly as passed |

---

## 📄 License

All code in this folder is released under the [MIT License](../LICENSE). Use it, change it, and share it freely.
