# Install and deploy

## Install the Python package

The distribution is named `nomad-wiki-page`, while Python imports use
`wiki_page`. The package requires Python `>=3.10` and `nomad-lab>=1.4.1`.
The parent distribution workspace uses Python 3.12.

For a standalone installation:

```sh
git clone https://github.com/PTiringer/Wiki-page.git
cd Wiki-page
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install .
```

Install into the environment used by NOMAD. Copying source files without
installing the package does not register its entry points.

The package registers three components:

```text
wiki_page.schema_packages:schema_package_entry_point
wiki_page.apps:app_entry_point
wiki_page.example_uploads:example_upload_entry_point
```

NOMAD discovers these through installed package metadata. If your installation
restricts plugin entry points with an include/exclude configuration, ensure these
IDs are allowed while preserving the other components your deployment needs.
There are no wiki-specific server credentials or source-connection settings.

## Use the distribution workspace

The project tracks the plugin at `packages/wiki-page`. Its parent `pyproject.toml`
contains the `nomad-wiki-page` dependency with a workspace source. Initialize
submodules from the distribution root:

```sh
git submodule update --init --recursive
```

The deployment image must install the plugin in the NOMAD environment. This
project's deployment script copies `packages/wiki-page` into the image and
installs it with the other local plugins. Its `--no-deps` installation assumes
the base image already provides the required dependencies.

## Deploy updates

1. Commit and push changes in the Wiki-page repository.
2. Commit and push the new `packages/wiki-page` revision in the parent distribution
   repository to the deployment branch.
3. From the sibling `test_deployment` directory, run:

   ```sh
   ./deploy.sh update
   ```

The script defaults to branch `stable` and checkout `/opt/nomad-oasis`.
Keep image building enabled. `update` fetches repository changes; `start` does not.
Reprocess affected entries after schema or normalization changes so generated
archive/search content can be refreshed.

## Deploy GUI features

The **New Wiki Page** button and project-specific navigation changes live in
`nomad-FAIR`. To update them, commit and push that submodule, update its revision
in the parent repository, and use a full image build. Installing this Python
package alone does not add a custom navigation button to an arbitrary NOMAD GUI.

## Verify

Process the [tutorial archive](../tutorial/tutorial.md), check the rich-text
fields and tasks, and open the Wiki Pages Explore app. Confirm the expected entry
is visible under your current access settings. If the schema or app is missing,
check the installed package, enabled entry points, and running service/image versions.
