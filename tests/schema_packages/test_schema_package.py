import os.path

from nomad.client import normalize_all, parse


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.summary == '<p>Landing page for the wiki.</p>\n'
    assert 'wiki' in entry_archive.data.tags
    assert len(entry_archive.data.to_do) == 1
    assert entry_archive.data.to_do[0].topic == 'Publish editorial rules'
    assert entry_archive.data.to_do[0].assignee == 'Alice'
    assert entry_archive.metadata.entry_name == 'Home'
