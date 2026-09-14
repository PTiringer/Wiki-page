# Wiki Pages for NOMAD

`nomad-wiki-page` turns NOMAD entries into searchable knowledge-base pages.
It provides a **Wiki Page** schema with rich-text descriptions, summaries,
tags, and structured To Dos, plus a **Wiki Pages** Explore app.

Pages remain NOMAD entries: they belong to uploads and follow NOMAD's existing
editing and visibility rules. This is not a separate wiki server.

## What is included

- `WikiPage`: an ELN-style page with editable content and repeated To Do items.
- `Wiki Pages`: a search app at `wiki-pages`, in category `CBS`.
- `Wiki Pages Example Upload`: a sample Home page with content and tasks.

The **AI summary** field stores editable text. The plugin does not call an AI
service or generate summaries. Assignees are text labels, and deadlines do not
send reminders.

The project's customized NOMAD GUI also has a **New Wiki Page** button. That
button is implemented in the `nomad-FAIR` submodule, not in this Python package.

## Documentation

- [Tutorial](tutorial/tutorial.md): create, edit, and find a page.
- [Installation](how_to/install_this_plugin.md): install and deploy the package.
- [Usage](how_to/use_this_plugin.md): manage content, tasks, filters, and common issues.
- [Explanation](explanation/explanation.md): schema normalization and search behavior.
- [Reference](reference/references.md): fields, filters, identifiers, and source locations.
- [Contribute code](how_to/contribute_to_this_plugin.md).
- [Contribute documentation](how_to/contribute_to_the_documentation.md).
