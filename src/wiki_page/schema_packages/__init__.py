from nomad.config.models.plugins import SchemaPackageEntryPoint


class WikiPageSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from wiki_page.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = WikiPageSchemaPackageEntryPoint(
    name='WikiPageSchemaPackage',
    description='Schema package for wiki-style ELN pages.',
)
