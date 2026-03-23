# Wiki-page

Wiki-style knowledge base plugin for NOMAD.

## What it provides

- A `Wiki Pages` Explore app at `wiki-pages`
- A `WikiPage` schema package for ELN-style wiki entries
- Added functionalities: To Dos, with topic, assignee and deadline
- An example upload with a sample wiki home page
- Modified filter menues

The schema is designed to feel like the built-in ELN editor while adding new functionalities such as To Do items.

## Development

```sh
clone into packages folder:
git clone https://github.com/PTiringer/Wiki-page.git 
```

if needed include the packages in the config file: nomad.yaml \
        - "wiki_page.schema_packages:schema_package_entry_point"\
        - "wiki_page.apps:app_entry_point" \
        - "wiki_page.example_uploads:example_upload_entry_point"\
in pyproject.toml:\
   "nomad-wiki-page"

## Plugin entry points

This package publishes three NOMAD plugin entry points:

- schema package: `wiki_page.schema_packages:schema_package_entry_point`
- app: `wiki_page.apps:app_entry_point`
- example upload: `wiki_page.example_uploads:example_upload_entry_point`
