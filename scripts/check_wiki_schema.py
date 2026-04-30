from wiki_page.schema_packages.schema_package import WikiPage


def main() -> None:
    print('WikiPage loaded from:', WikiPage.__module__)
    print('Visible/order fields:')
    print(WikiPage.m_def.m_annotations['eln'].properties.order)
    print('Known wiki fields:')
    print(
        [
            name
            for name in WikiPage.m_def.all_properties
            if name in ['description', 'ai_summary', 'tags', 'test', 'summary']
        ]
    )

    for name in ['description', 'ai_summary', 'test', 'summary']:
        prop = WikiPage.m_def.all_properties.get(name)
        print()
        print(name)
        if prop is None:
            print('  missing')
            continue
        print('  component:', prop.m_annotations.get('eln').component)
        print('  display:', prop.m_annotations.get('display'))


if __name__ == '__main__':
    main()
