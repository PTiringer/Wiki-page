def test_importing_app():
    from wiki_page.apps import app_entry_point

    assert app_entry_point.app.label == 'Wiki Pages'
    assert app_entry_point.app.path == 'wiki-pages'


def test_deadline_filter_uses_datetime_widget():
    from wiki_page.apps import app_entry_point, schema

    deadline_filter = app_entry_point.app.menu.items[1].items[0]

    assert deadline_filter.type == 'histogram'
    assert deadline_filter.title == 'Deadline'
    assert deadline_filter.x.search_quantity == f'data.to_do.deadline#{schema}'
    assert deadline_filter.show_statistics is False
