# Reference

## Package identifiers

| Identifier | Value |
| --- | --- |
| Python distribution | `nomad-wiki-page` |
| Import package | `wiki_page` |
| Parent submodule path | `packages/wiki-page` |
| Schema package name | `wiki_page` |
| Wiki schema | `wiki_page.schema_packages.schema_package.WikiPage` |
| Task schema | `wiki_page.schema_packages.schema_package.WikiTodoItem` |
| Explore app path | `wiki-pages` |
| Explore app label/category | `Wiki Pages` / `CBS` |

## Registered entry points

| ID | Purpose |
| --- | --- |
| `wiki_page.schema_packages:schema_package_entry_point` | Load the schema package |
| `wiki_page.apps:app_entry_point` | Register the Explore app |
| `wiki_page.example_uploads:example_upload_entry_point` | Register Wiki Pages Example Upload |

No console script, API endpoint, action, custom parser, or standalone normalizer
is registered in this package's `pyproject.toml`. Wiki normalization is a method
on the schema, invoked by NOMAD's metainfo normalization.

## WikiPage fields

| Field | Type | Editor/meaning |
| --- | --- | --- |
| `name` | Inherited string | Page name |
| `description` | String | Main rich text; `RichTextEditQuantity` |
| `ai_summary` | String | Editable summary; `RichTextEditQuantity`; no automatic generation |
| `tags` | String array | Search tags; `StringEditQuantity` |
| `test` | String | Editor test field; `StringEditQuantity` |
| `to_do` | Repeated WikiTodoItem | Structured tasks |

The creation template sets `name` to `Untitled Wiki Page`, sets description,
summary, and test to empty strings, and sets tags to `['wiki', 'knowledge-base']`.
During normalization, empty tags become `['wiki']` and missing text fields become
empty strings.

The current display order is name, description, AI summary, tags, test, and To Dos.
The separate ELN property-order list has an existing concatenated `summarytags`
entry; it is not a real quantity. Inherited `lab_id` and `datetime` are hidden in
the ELN annotation.

## WikiTodoItem fields

| Field | Type/default | Meaning |
| --- | --- | --- |
| `topic` | String | Item label and task subject |
| `assignee` | String | Free-text assignee, not an account reference |
| `status` | Enum; `Not started` | One of `Not started`, `In progress`, `Done` |
| `deadline` | NOMAD Datetime | Deadline date and time |

To Do overview presentation is enabled, with topic, assignee, status, and deadline
in that order. No task field sends notifications or changes upload permissions.

## Search configuration

Let `SCHEMA` denote `wiki_page.schema_packages.schema_package.WikiPage`.

| Purpose | Quantity |
| --- | --- |
| Locked schema filter | `section_defs.definition_qualified_name = SCHEMA` |
| Title column | `entry_name` |
| Description column | `results.eln.descriptions` |
| AI summary column | `data.ai_summary#SCHEMA` |
| Updated column | `upload_create_time` |
| Authors column | `authors` |
| Task deadline | `data.to_do.deadline#SCHEMA` |
| Task topic | `data.to_do.topic#SCHEMA` |
| Task assignee | `data.to_do.assignee#SCHEMA` |
| Task status | `data.to_do.status#SCHEMA` |

Replace `SCHEMA` with the full qualified name when using the schema-specific
quantity identifiers. Included search quantities are `*#SCHEMA` and
`results.eln.names`, `results.eln.descriptions`, and `results.eln.tags`.
The app excludes the filter controls `mainfile`, `entry_name`, and `combine`.
This does not remove `entry_name` from the result columns.

Deadline uses a histogram menu item; task text/status use terms menu items.
The status menu requests three options. Additional author, dataset, visibility,
ID, and schema filters are listed in the [usage guide](../how_to/use_this_plugin.md).

## Example upload and source map

The example upload targets `example_uploads/getting_started`, containing a
`home.archive.yaml` and README. The example data are illustrative.

| Location under `src/wiki_page/` | Responsibility |
| --- | --- |
| `schema_packages/schema_package.py` | Fields, editor/display annotations, normalization |
| `schema_packages/__init__.py` | Schema entry point |
| `apps/__init__.py` | Explore filters, columns, and locked schema |
| `example_uploads/__init__.py` | Example-upload registration |
| `example_uploads/getting_started/` | Example content |

`actions/`, `north_tools/`, `parsers/`, and `normalizers/` contain retained template
code not registered as wiki features. The custom creation button is instead in
`nomad-FAIR/gui/src/components/nav/NewWikiPageButton.js`.
