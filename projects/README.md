# Projects

One folder per project, named in `kebab-case`.

| Project | Category | Status |
|---|---|---|
| [redbull-drink](redbull-drink/) | Product visualization | ✅ Complete |
| [droplet-generator](droplet-generator/) | Procedural tool | 🚧 In progress |

## Add a new project

```bash
python scripts/utils/new_project.py my-project-name
```

This creates `source/`, `renders/`, `exports/`, `references/`, `textures/`, `post/` and a README copied from [`_template/`](_template/). Delete any subfolder the project doesn't need, then add a row to the table above and to the main [README](../README.md).
