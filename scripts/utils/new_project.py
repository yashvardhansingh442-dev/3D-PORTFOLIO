"""Create a new project folder with the standard subfolders.

Usage:
    python scripts/utils/new_project.py my-project-name
"""
import sys
from pathlib import Path

SUBFOLDERS = ["source", "renders", "exports", "references", "textures", "post"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python new_project.py <project-name>")
        sys.exit(1)

    root = Path(__file__).resolve().parents[2] / "projects" / sys.argv[1]
    if root.exists():
        print(f"Already exists: {root}")
        sys.exit(1)

    for name in SUBFOLDERS:
        (root / name).mkdir(parents=True)
        (root / name / ".gitkeep").touch()

    template = root.parent / "_template" / "README.md"
    if template.exists():
        (root / "README.md").write_text(template.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Created {root}")

if __name__ == "__main__":
    main()
