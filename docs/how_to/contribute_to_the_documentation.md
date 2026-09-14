# Contribute to the documentation

The site uses MkDocs with Material. Markdown pages are in `docs/`, navigation
and extensions in `mkdocs.yml`, and appearance overrides in `docs/theme` and
`docs/stylesheets`.

## Install tools

For a full development environment, install the package's dev extra:

```sh
python -m pip install -e '.[dev]'
```

For documentation-only work without NOMAD:

```sh
python -m pip install mkdocs 'mkdocs-material==8.1.1' pymdown-extensions mkdocs-click
```

Run subsequent commands from the plugin root.

## Preview and validate

```sh
python -m mkdocs serve
```

Open the local URL printed by MkDocs and inspect the navigation, tables, and YAML
examples. Stop the preview with Ctrl+C. Build before committing:

```sh
python -m mkdocs build --strict
```

The default output is `site/`; it is generated content, not a documentation source.
A local build does not publish anything. Inspect the repository's documentation
deployment workflow before changing publishing behavior.

## Organize content

- Tutorial: a complete first-page workflow.
- How-to guides: concrete editing, installation, filtering, and troubleshooting tasks.
- Explanation: schema normalization, indexing, and the boundary between plugin and GUI.
- Reference: exact identifiers, types, status values, fields, and search configuration.

Use relative links between pages. Add new pages to `mkdocs.yml` and validate their
local assets and code examples. Use synthetic page content and example deadlines,
not private laboratory notes or real task assignments.

Check claims against the implementation. In particular, do not describe the
AI summary field as an automatic generator, the Updated column as last-edit time,
or the assignee field as a user reference. When documentation exposes an existing
code issue, describe it accurately and keep unrelated code fixes separate.
