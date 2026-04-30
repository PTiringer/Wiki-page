def test_importing_app():
    from wiki_page.apps import app_entry_point

    assert app_entry_point.app.label == 'Wiki Pages'
    assert app_entry_point.app.path == 'wiki-pages'
    selected_columns = {
        column.search_quantity
        for column in app_entry_point.app.columns
        if column.selected
    }
    included_search_quantities = set(app_entry_point.app.search_quantities.include)

    assert 'results.eln.descriptions' in selected_columns
    assert 'results.eln.descriptions' in included_search_quantities
    assert 'results.eln.names' in included_search_quantities
    assert 'results.eln.tags' in included_search_quantities
    assert (
        'data.ai_summary#wiki_page.schema_packages.schema_package.WikiPage'
        in selected_columns
    )
