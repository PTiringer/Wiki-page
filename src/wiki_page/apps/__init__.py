from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Columns,
    Filters,
    Menu,
    MenuItemCustomQuantities,
    MenuItemDefinitions,
    MenuItemHistogram,
    MenuItemOptimade,
    MenuItemTerms,
    MenuItemVisibility,
    SearchQuantities,
)

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
        menu=Menu(
            title='Filters',
            size='sm',
            items=[
                Menu(
                    title='Wiki Pages',
                    items=[
                        MenuItemTerms(search_quantity='results.eln.tags', show_input=False),
                        MenuItemTerms(search_quantity='results.eln.names', options=0),
                        MenuItemTerms(search_quantity='results.eln.descriptions', options=0),
                        MenuItemTerms(search_quantity='results.eln.lab_ids', options=0),
                    ],
                ),
                Menu(
                    title='To Do',
                    size='lg',
                    items=[
                        MenuItemTerms(
                            search_quantity=f'data.to_do.topic#{schema}',
                            options=10,
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.to_do.assignee#{schema}',
                            options=10,
                        ),
                        MenuItemHistogram(
                            x=Axis(search_quantity=f'data.to_do.deadline#{schema}')
                        ),
                    ],
                ),
                Menu(
                    title='User Defined Quantities',
                    size='xl',
                    items=[MenuItemCustomQuantities()],
                ),
                Menu(
                    title='Author / Origin / Dataset',
                    size='lg',
                    items=[
                        MenuItemTerms(search_quantity='authors.name', options=0),
                        MenuItemHistogram(x=Axis(search_quantity='upload_create_time')),
                        MenuItemTerms(
                            search_quantity='external_db',
                            options=5,
                            show_input=False,
                        ),
                        MenuItemTerms(search_quantity='datasets.dataset_name'),
                        MenuItemTerms(search_quantity='datasets.doi', options=0),
                    ],
                ),
                Menu(
                    title='Visibility / IDs / Schema',
                    items=[
                        MenuItemVisibility(),
                        MenuItemTerms(search_quantity='entry_id', options=0),
                        MenuItemTerms(search_quantity='upload_id', options=0),
                        MenuItemTerms(search_quantity='upload_name', options=0),
                        MenuItemTerms(search_quantity='results.material.material_id', options=0),
                        MenuItemTerms(search_quantity='datasets.dataset_id', options=0),
                        MenuItemDefinitions(),
                    ],
                ),
            ],
        ),
    ),
)
