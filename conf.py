# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Fortran Programming Language"
copyright = ""
author = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "myst_parser",
    "sphinx_panels",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [
    "_templates",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    "_static",
]

html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "favicons" : [
        {
            "rel": "icon",
            "href": "images/favicon.ico",
        },
    ],
    "show_prev_next": False,
    "page_sidebar_items": [],
    "nosidebar": True,
    "footer_items": ["copyright"],
    # "navbar_align": "left",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "icon_links": [
        {
            "name": "Discourse",
            "url": "https://fortran-lang.discourse.group/",
            "icon": "fab fa-discourse",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/fortranlang",
            "icon": "fab fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/fortran-lang",
            "icon": "fab fa-github",
        },
        {
            "name": "RSS",
            "url": "https://fortran-lang.org/news.xml",
            "icon": "fas fa-rss",
        },
    ]
}

html_sidebars = {
    "*": [],
    "learn/**": [],
    "news/**": ['postcard.html', 'recentposts.html', 'archives.html']
}

html_permalinks = False

html_title = "Fortran Programming Language"

html_logo = "_static/images/fortran-logo-256x256.png"

html_baseurl = "https://awvwgk.github.io/fortran-lang.org/"

html_copy_source = False

master_doc = 'index'

panels_add_bootstrap_css = False

blog_path = "news"
blog_post_pattern = "_posts/*/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

def hide_h1_on_index_pages(app, pagename, templatename, context, doctree):
    if pagename in ["index", "learn", "compilers", "community", "packages"]:
        app.add_css_file("css/hide_h1.css")

def setup(app):
    app.connect('html-page-context', hide_h1_on_index_pages)
