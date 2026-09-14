# Create your first wiki page

You need a NOMAD installation with the plugin installed and an account with
permission to create and edit uploads. See [Installation](../how_to/install_this_plugin.md)
if the Wiki Page schema is unavailable.

## 1. Create a page

Save this synthetic example as `home.archive.yaml`:

```yaml
data:
  m_def: wiki_page.schema_packages.schema_package.WikiPage
  name: Lab knowledge base
  description: |
    <p>Shared instructions for preparing and reviewing laboratory documentation.</p>
  ai_summary: |
    <p>A starting point for documentation and review tasks.</p>
  tags:
    - wiki
    - documentation
  to_do:
    - topic: Review the equipment guide
      assignee: Documentation Team
      status: Not started
      deadline: '2026-12-01T09:00:00+00:00'
```

Create a NOMAD upload, add the file, and let processing finish. The schema is
provided by the installed plugin; there is no need for an embedded `definitions`
block. The summary above is supplied by the author, not generated automatically.

Alternatively, select **Wiki Pages Example Upload** in NOMAD's example-upload
interface if it is available. Its Home page includes two sample tasks; their
dates and content are illustrative and should be replaced.

## 2. Edit the content

Open the entry and use its ELN editor. Set a descriptive name and edit the
**Description** and **AI summary** rich-text fields. Add tags that make sense
for your team. The `wiki` tag is ensured during normalization.

The current schema also exposes a **test** field for checking editor behavior.
It is not required for writing a page and has no special operational meaning.

Save using the NOMAD editor's controls and allow processing to complete.
Editing requires appropriate permissions and an editable upload.

## 3. Track a task

Add a To Do item with a topic, assignee, status, and deadline. Status is one of:

- `Not started`
- `In progress`
- `Done`

The assignee is a string, not a NOMAD user reference. Setting it does not grant
access or notify that person. A deadline is a date/time value; use an explicit
timezone in archive files to avoid ambiguity.

## 4. Find the page

Open **Explore → Wiki Pages** (category `CBS`). Search or filter using the
Wiki Pages menu and inspect the To Do filters for topic, assignee, status, and
deadline. Results are wiki entries, not individual task records.

Select the page to inspect its content. If it is missing, check processing status,
visibility, and active filters. Adding a `wiki` tag to an unrelated schema does
not make it a WikiPage entry.

## Optional: use the project creation button

In the customized NOMAD GUI, **New Wiki Page** creates a new upload and a
`home.archive.json` entry, then opens it. Its initial name includes the browser's
local date/time and your user name. Rename it to describe the page's subject.
If the button is unavailable, the file-upload route above works without that
GUI customization.
