# Contribute to the plugin

## Set up development

From the Wiki-page checkout:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
```

Install the package in a compatible NOMAD environment so its entry points are
registered. Merely setting `PYTHONPATH` is not equivalent to installation.
The parent project uses Python 3.12; the package declares Python `>=3.10` and
NOMAD `>=1.4.1`. Archive-parsing tests also need NOMAD's system libraries,
including libmagic.

## Choose the right component

Edit `schema_packages/schema_package.py` for page fields, task fields, editor
annotations, or normalization. Edit `apps/__init__.py` for search columns and
menus. Update example content when user-facing fields change.

The New Wiki Page button and project navigation are GUI changes in `nomad-FAIR`.
Do not add a Python action merely to change a GUI button. Template action,
parser, normalizer, and NORTH modules are not registered features of this plugin.

## Verify changes

Run from the plugin root:

```sh
python -m pytest tests/schema_packages tests/apps -q
ruff check .
ruff format . --check
```

The schema test checks the supplied archive's content, ELN description aggregation,
wiki tag, task fields, and entry title. App tests check app identity and deadline
and status widgets. Broader template tests remain in the repository and may need
separate setup; they are not proof that those template components are active.

For schema changes, verify both archive parsing and editing in NOMAD. For search
changes, process representative entries and check the indexed quantities and
filters in the actual app. Unit checks alone do not establish browser layout,
permissions, or live search behavior.

Existing source issues, including the `summarytags` annotation typo, may cause
lint or presentation discrepancies. Separate those from your change and report
them; documentation updates do not silently change runtime behavior.

## Deliver an update

Update the [reference](../reference/references.md), tutorial, and example upload
when changing fields or defaults. Build the docs with `mkdocs build --strict`.
Commit and push the plugin, then update its revision in the parent distribution.
Follow [Installation](install_this_plugin.md) to rebuild the running image.

Declare new dependencies in `pyproject.toml` and ensure they are installed in the
deployment image, whose plugin layer uses `--no-deps`. Keep virtual environments,
generated documentation, and private wiki content out of commits.
