from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

my_north_tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin Wiki-page.',
    image='ghcr.io/ptiringer/Wiki-page:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin Wiki-page.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'tiringer@cbs.mpg.de', 'name': 'Peter Tiringer'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='my_north_tool',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='wiki_page_my_north_tool', north_tool=my_north_tool
)
