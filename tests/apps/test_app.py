def test_importing_app():
    from wiki_page.apps import app_entry_point

    assert app_entry_point.app.label == 'Wiki Pages'
    assert app_entry_point.app.path == 'wiki-pages'
