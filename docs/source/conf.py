# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Team 3045'
copyright = '2024, GearGremlins'
author = 'GearGremlins'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'

html_title = "Team 3045 Docs"

html_logo = '_static/images/2024_Gear_Gremlin_logo.png'
html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#72a300",
        "color-brand-content": "#72a300",
    },
    "dark_css_variables": {
        "color-brand-primary": "#97D700",
        "color-brand-content": "#97D700",
    },
}
# -- Options for EPUB output
epub_show_urls = 'footnote'

# Custom CSS to change link colors
def setup(app):
    app.add_css_file('custom.css')

html_static_path = ['_static']
html_css_files = ['_static/custom.css', ]
