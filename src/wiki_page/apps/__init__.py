from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenu, FilterMenus, Filters, SearchQuantities

schema = 'wiki_page.schema_packages.schema_package.WikiPage'

app_entry_point = AppEntryPoint(
    name='Wiki Pages',
    description='Search app for wiki-style knowledge base entries.',
    app=App(
        label='Wiki Pages',
        path='wiki-pages',
        category='Experiment',
        description='Search wiki-style knowledge base entries.',
        readme=(
            'This page allows you to search **wiki-style pages** within NOMAD. '
            'It is intended for ELN-like knowledge base content with rich text '
            'summaries, tags, and structured To Do items.'
        ),
        search_quantities=SearchQuantities(include=[f'*#{schema}']),
        filters_locked={'section_defs.definition_qualified_name': schema},
        filters=Filters(exclude=['mainfile', 'entry_name', 'combine']),
        columns=Columns(
            selected=[
                'entry_name',
                f'data.summary#{schema}',
                'upload_create_time',
                'authors',
            ],
            options={
                'entry_name': Column(label='Title'),
                f'data.summary#{schema}': Column(label='Summary'),
                'upload_create_time': Column(label='Updated'),
                'authors': Column(),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'eln': FilterMenu(label='Electronic Lab Notebook'),
                'custom_quantities': FilterMenu(label='User Defined Quantities', size='l'),
                'author': FilterMenu(label='Author / Origin / Dataset', size='m'),
                'metadata': FilterMenu(label='Visibility / IDs / Schema'),
            }
        ),
    ),
)
