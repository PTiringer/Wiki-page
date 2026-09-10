import os.path

from nomad.client import normalize_all, parse


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.ai_summary == '<p>Landing page for the wiki.</p>\n'
    assert entry_archive.data.description == '<p>Overview of the internal wiki page.</p>\n'
    assert entry_archive.data.test == 'Test value'
    assert '<p>Overview of the internal wiki page.</p>\n' in entry_archive.results.eln.descriptions
    assert '<p>Landing page for the wiki.</p>\n' in entry_archive.results.eln.descriptions
    assert 'wiki' in entry_archive.data.tags
    assert len(entry_archive.data.to_do) == 1
    assert entry_archive.data.to_do[0].topic == 'Publish editorial rules'
    assert entry_archive.data.to_do[0].assignee == 'Alice'
    assert entry_archive.data.to_do[0].status == 'In progress'
    assert entry_archive.metadata.entry_name == 'Home'
