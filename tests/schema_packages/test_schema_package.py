import os.path

from nomad.client import normalize_all, parse


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.slug == 'home'
    assert entry_archive.data.page_type == 'guide'
    assert 'wiki' in entry_archive.data.tags
    assert entry_archive.metadata.entry_name == 'Home'
