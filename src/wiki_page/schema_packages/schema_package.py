from typing import TYPE_CHECKING

from nomad.datamodel.data import BasicElnCategory, EntryData
from nomad.datamodel.metainfo.eln import ElnBaseSection
from nomad.metainfo import MEnum, MSection, Quantity, Reference, SchemaPackage, Section, SectionProxy, SubSection

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = SchemaPackage(name='wiki_page')


class WikiSection(MSection):
    m_def = Section(
        label='Wiki Section',
        a_eln=dict(properties=dict(order=['title', 'anchor', 'content'])),
    )

    title = Quantity(type=str, a_eln=dict(component='StringEditQuantity'))
    anchor = Quantity(
        type=str,
        description='Stable identifier that can be used as an in-page anchor.',
        a_eln=dict(component='StringEditQuantity'),
    )
    content = Quantity(
        type=str,
        a_eln=dict(component='RichTextEditQuantity', props=dict(height=260)),
    )


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
                    'slug',
                    'page_type',
                    'tags',
                    'body',
                    'sidebar',
                    'related_pages',
                    'sections',
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
    slug = Quantity(
        type=str,
        description='Short URL-style identifier for this page.',
        a_eln=dict(component='StringEditQuantity'),
    )
    page_type = Quantity(
        type=MEnum('article', 'guide', 'reference', 'faq'),
        default='article',
        a_eln=dict(component='EnumEditQuantity'),
    )
    body = Quantity(
        type=str,
        a_eln=dict(component='RichTextEditQuantity', props=dict(height=520)),
    )
    sidebar = Quantity(
        type=str,
        description='Optional rich text block for callouts or navigation links.',
        a_eln=dict(component='RichTextEditQuantity', props=dict(height=220)),
    )
    related_pages = Quantity(
        type=Reference(SectionProxy('WikiPage')),
        shape=['*'],
        a_eln=dict(component='ReferenceEditQuantity'),
    )
    sections = SubSection(
        section_def=WikiSection,
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
