from typing import TYPE_CHECKING

from nomad.datamodel.data import BasicElnCategory, EntryData
from nomad.datamodel.metainfo.eln import ElnBaseSection
from nomad.metainfo import (
    Datetime,
    MEnum,
    MSection,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = SchemaPackage(name='wiki_page')

TODO_STATUSES = ['Not started', 'In progress', 'Done']


class WikiTodoItem(MSection):
    m_def = Section(
        label='To Do',
        label_quantity='topic',
        a_eln=dict(
            overview=True,
            properties=dict(order=['topic', 'assignee', 'status', 'deadline']),
        ),
    )

    topic = Quantity(type=str, a_eln=dict(component='StringEditQuantity'))
    assignee = Quantity(type=str, a_eln=dict(component='StringEditQuantity'))
    status = Quantity(
        type=MEnum(TODO_STATUSES),
        default='Not started',
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(suggestions=TODO_STATUSES),
        ),
    )
    deadline = Quantity(type=Datetime, a_eln=dict(component='DateTimeEditQuantity'))


class WikiPage(ElnBaseSection, EntryData):
    m_def = Section(
        categories=[BasicElnCategory],
        label='Wiki Page',
        a_display=dict(
            order=[
                'name',
                'description',
                'ai_summary',
                'tags',
                'test',
                'to_do',
            ],
            visible=dict(
                include=[
                    'name',
                    'description',
                    'ai_summary',
                    'tags',
                    'test',
                    'to_do',
                ]
            ),
        ),
        a_eln=dict(
            lane_width='1200px',
            hide=['lab_id', 'datetime'],
            properties=dict(
                order=[
                    'name',
                    'description',
		    'summary'
                    'tags',
                    'test',
                    'to_do',
                ],
                visible=dict(
                    include=[
                        'name',
                        'description',
                        'ai_summary',
                        'tags',
                        'test',
                        'to_do',
                    ]
                ),
            ),
        ),
        a_template=dict(
            name='Untitled Wiki Page',
            description='',
            ai_summary='',
            tags=['wiki', 'knowledge-base'],
            test='',
        ),
    )

    tags = Quantity(
        type=str,
        shape=['*'],
        description='Search tags for this wiki page.',
        a_eln=dict(component='StringEditQuantity'),
    )
    test = Quantity(
        type=str,
        description='Test field for checking wiki page editing.',
        a_display=dict(visible=True, editable=True),
        a_eln=dict(component='StringEditQuantity'),
    )
    description = Quantity(
        type=str,
        description='Description for this wiki page.',
        a_display=dict(visible=True, editable=True),
        a_eln=dict(
            component='RichTextEditQuantity',
            label='Description',
            props=dict(height=180),
        ),
    )
    ai_summary = Quantity(
        type=str,
        description='AI-generated summary for this wiki page.',
        a_display=dict(visible=True, editable=True),
        a_eln=dict(
            component='RichTextEditQuantity',
            label='AI summary',
            props=dict(height=180),
        ),
    )
    to_do = SubSection(
        section_def=WikiTodoItem,
        repeats=True,
        a_eln=dict(),
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        if self.description is None:
            self.description = ''
        if self.ai_summary is None:
            self.ai_summary = ''
        if self.test is None:
            self.test = ''

        super().normalize(archive, logger)

        if self.ai_summary and archive.results and archive.results.eln:
            if archive.results.eln.descriptions is None:
                archive.results.eln.descriptions = []
            if self.ai_summary not in archive.results.eln.descriptions:
                archive.results.eln.descriptions.append(self.ai_summary)

        if not self.tags:
            self.tags = ['wiki']
        elif 'wiki' not in self.tags:
            self.tags = [*self.tags, 'wiki']

        if archive.metadata and not archive.metadata.entry_name and self.name:
            archive.metadata.entry_name = self.name


m_package.__init_metainfo__()
