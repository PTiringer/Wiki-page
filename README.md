# Wiki-page

Wiki-style knowledge base plugin for NOMAD.

## What it provides

- A `Wiki Pages` Explore app at `wiki-pages`
- A `WikiPage` schema package for ELN-style wiki entries
- An example upload with a sample wiki home page

The schema is designed to feel like the built-in ELN editor while adding wiki-oriented
fields such as a slug, page type, rich text body, sidebar, related pages, and repeated
content sections.

## Development

```sh
git clone https://github.com/PTiringer/Wiki-page.git
cd Wiki-page/Wiki-page
uv pip install -e '.[dev]'
pytest tests/apps/test_app.py tests/schema_packages/test_schema_package.py
```

## Plugin entry points

This package publishes three NOMAD plugin entry points:

- schema package: `wiki_page.schema_packages:schema_package_entry_point`
- app: `wiki_page.apps:app_entry_point`
- example upload: `wiki_page.example_uploads:example_upload_entry_point`
