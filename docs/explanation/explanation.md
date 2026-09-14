# How Wiki Pages works

## A knowledge base built from entries

A wiki page is an archive whose `data` section is a `WikiPage`. The class derives
from NOMAD's `ElnBaseSection` and `EntryData`, reusing ELN editing, normalization,
and entry infrastructure. Repeated `WikiTodoItem` subsections hold tasks.

```text
YAML/JSON archive or ELN editor
  → WikiPage data
  → schema normalize()
  → ELN results and archive metadata
  → NOMAD indexing
  → Wiki Pages Explore app
```

There is no wiki-specific scraper, database, or registered custom parser.
Standard NOMAD archive parsing handles the YAML and JSON files.

## Schema annotations

The schema's annotations select rich-text editors for the description and
summary, string editors for tags and task text, an enum editor for status, and
a date/time editor for deadlines. Display annotations list visible page fields.
The schema hides inherited `lab_id` and `datetime` in its ELN presentation and
requests a wide editing lane.

A creation template supplies an untitled name, empty content, and initial tags.
Templates are not the same as normalization defaults: data created through other
routes can start with different values.

## Normalization

`WikiPage.normalize()` performs these operations:

1. Replace missing `description`, `ai_summary`, and `test` values with empty strings.
2. Run inherited ELN normalization.
3. Append a nonempty summary to `results.eln.descriptions` if not already present
   and the ELN results section exists.
4. Ensure the local `tags` array contains `wiki`.
5. Fill an empty `metadata.entry_name` from `name` when metadata is present.

The inherited ELN normalizer supplies standard results such as names and
descriptions. The plugin's extra summary aggregation makes supplied summaries
available alongside descriptions to ELN-based search.

Tag enforcement occurs after the inherited normalization call. The local archive
is guaranteed to contain the `wiki` tag after this method; do not infer that all
result tags were regenerated after that assignment in the same pass.

Normalization does not generate summaries, send notifications, calculate task
progress, or rewrite an existing entry title unconditionally.

## Search app

The app declares relevant schema and ELN search quantities and locks the
`section_defs.definition_qualified_name` filter to the WikiPage qualified name.
A `wiki` tag alone is not sufficient to include an unrelated entry.

The app configures result columns and menus; NOMAD performs the indexing and
search, applies permissions, and renders the results. To Dos remain nested content
inside each page rather than independent entries.

The column labelled Updated reads `upload_create_time`. It describes the upload,
not the latest content edit. The AI summary field's label describes intended use,
not an implemented AI service.

## Plugin versus project GUI

This Python package registers the schema, app, and example upload. The project
also changes NOMAD's GUI in its separate `nomad-FAIR` repository. Its creation
button creates an upload, writes `home.archive.json`, waits for processing, and
opens the resulting entry. It initializes the title from local time and user
identity and supplies the tags `wiki` and `knowledge-base`.

Keeping this distinction matters during deployment: a Python plugin update cannot
replace compiled GUI assets. The file-upload workflow remains usable without the
custom creation button.

## Retained template code

The source tree still contains parser, normalizer, action, and NORTH-tool template
modules. They are not among the three registered plugin entry points. Their
presence does not make them supported wiki operations, scheduled jobs, or active
NORTH tools.
