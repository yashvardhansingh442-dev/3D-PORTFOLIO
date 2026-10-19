# Blender Scripts

Python scripts that run inside Blender (`bpy`).

## How to run
1. Open Blender, go to the **Scripting** workspace
2. Open the `.py` file and click **Run Script**

## Scripts
| Script | What it does |
|---|---|
| [`droplet_generator.py`](droplet_generator.py) | Scatters non-overlapping water droplets over the selected mesh. Used in [droplet-generator](../../projects/droplet-generator/) |

## Conventions
- One script per task, named by action: `batch_render.py`, `apply_palette.py`
- A docstring at the top explaining what it does and any settings to change
- Tested on Blender version: 4.x / 5.x
