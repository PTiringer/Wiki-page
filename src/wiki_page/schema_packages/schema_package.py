from typing import TYPE_CHECKING

from nomad.datamodel.data import BasicElnCategory, EntryData
from nomad.datamodel.metainfo.eln import ElnBaseSection
from nomad.metainfo import Datetime, MSection, Quantity, SchemaPackage, Section, SubSection

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = SchemaPackage(name='wiki_page')


class WikiTodoItem(MSection):
    m_def = Section(
        label='To Do',
        a_eln=dict(properties=dict(order=['topic', 'assignee', 'deadline'])),
    )

    topic = Quantity(type=str, a_eln=dict(component='StringEditQuantity'))
    assignee = Quantity(type=str, a_eln=dict(component='StringEditQuantity'))
    deadline = Quantity(type=Datetime, a_eln=dict(component='DateTimeEditQuantity'))


class WikiPage(ElnBaseSection, EntryData):
    m_def = Section(
        categories=[BasicElnCategory],
        label='Wiki Page',
        a_eln=dict(
            lane_width='1200px',
            hide=['lab_id'],
            properties=dict(
                order=[
                    'name',
                    'summary',
                    'tags',
                    'to_do',
                ]
            ),
        ),
        a_template=dict(name='Untitled Wiki Page', tags=['wiki', 'knowledge-base']),
    )

    tags = Quantity(
        type=str,
        shape=['*'],
        description='Search tags for this wiki page.',
        a_eln=dict(component='StringEditQuantity'),
    )
    summary = Quantity(
        type=str,
        a_eln=dict(component='RichTextEditQuantity', props=dict(height=180)),
    )
    to_do = SubSection(
        section_def=WikiTodoItem,
        repeats=True,
        a_eln=dict(),
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if not self.tags:
            self.tags = ['wiki']
        elif 'wiki' not in self.tags:
            self.tags = [*self.tags, 'wiki']

        if archive.metadata and not archive.metadata.entry_name and self.name:
            archive.metadata.entry_name = self.name


m_package.__init_metainfo__()
