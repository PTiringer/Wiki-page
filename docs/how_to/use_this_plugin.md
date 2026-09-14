# Use Wiki Pages

## Write and organize content

Create pages using the [tutorial](../tutorial/tutorial.md), the registered example
upload, or the project's **New Wiki Page** button. Use `name` for the page title,
`description` for the main rich-text content, and `ai_summary` for a summary.
Both rich-text quantities are strings; YAML examples can contain HTML such as
`<p>...</p>`.

The summary is manually editable. Nothing in this plugin generates it, refreshes
it from the description, or contacts an AI model. Update it yourself when the
page's content changes.

Use `tags` to classify pages. Normalization supplies `['wiki']` when tags are
empty, or appends `wiki` if absent. The creation template and example use
`wiki` and `knowledge-base`; the extra tag is not mandatory.

## Manage To Dos

Each item in `to_do` has `topic`, `assignee`, `status`, and `deadline`. Add separate
items for separate tasks. Status defaults to `Not started` when omitted and must
use one of the three defined values, including capitalization.

```yaml
to_do:
  - topic: Check the instrument instructions
    assignee: Lab Ops
    status: In progress
    deadline: '2026-12-15T12:00:00+00:00'
```

Place this block under the entry's `data` section. These tasks are structured
page content: no emails, reminders, user-account assignments, or automatic status
changes are implemented. Mark a task `Done` manually when complete.

## Search

The **Wiki Pages** app locks results to the WikiPage schema and offers:

| Filter group | Use |
| --- | --- |
| Wiki Pages | ELN names, descriptions, and tags |
| To Do | Deadline histogram and topic, assignee, and status terms |
| User Defined Quantities | Search custom indexed quantities |
| Author / Origin / Dataset | Authors, upload creation time, external database, datasets and DOI |
| Visibility / IDs / Schema | Visibility and entry/upload/dataset/schema identifiers |

Results remain subject to NOMAD visibility permissions. Task filters narrow down
pages; open the page to inspect the matching task context. Do not assume combined
filters identify the same repeated task without checking the entry.

The default columns are **Title**, **Description**, **AI summary**, **Updated**,
and authors. The **Updated** column currently uses `upload_create_time`, so it is
not a last-edit timestamp. The Description column uses aggregated ELN descriptions,
which can include both the description and the supplied summary.

## Refresh and share

Save edits through NOMAD and wait for processing/indexing before checking search
results. Reprocess entries after relevant schema changes. Publishing and sharing
are handled through NOMAD upload permissions; the plugin does not implement a
separate access-control system.

Changing `name` does not unconditionally overwrite `metadata.entry_name`: the
plugin explicitly fills that metadata field only when it is empty. Check both
values if an existing search-result title differs from the edited page name.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Wiki Page schema is unknown | Package installation and schema entry-point activation in the running NOMAD environment. |
| Wiki Pages Explore app is absent | App entry-point activation and current deployment configuration. |
| New Wiki Page button is absent | The separate `nomad-FAIR` GUI customization and full GUI build. |
| Page missing from search | Processing/indexing, active filters, access permissions, and correct `data.m_def`. |
| Summary is empty | Enter it manually; no automatic summary generator is implemented. |
| Task assignee received no notification | Assignee is text only; the plugin sends no notifications. |
| Status rejected | Use exactly `Not started`, `In progress`, or `Done`. |
| Updated column seems unchanged | It is upload creation time, not page modification time. |
| Unexpected editor field ordering | The current ELN property order contains a `summarytags` typo; the display annotation has a separate valid order. |

The field-order issue is an existing implementation detail, not a required field:
do not add a `summarytags` quantity to your archive to work around it.
