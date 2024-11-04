# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx
from sphinx.application import Sphinx
from docutils import nodes
from docutils.parsers.rst import Directive


project = "数据库实用入门"
copyright = "2024, Christopher Painter&#8209;Wakefield"
author = "Christopher Painter&#8209;Wakefield"
# release = "0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list[str] = [
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx_immaterial.theme_result",
    "sphinx_immaterial.kbd_keys",
    "sphinx_immaterial.graphviz",
    "myst_parser",
    "sphinx_togglebutton",
    "sphinx_immaterial",
]

# language = "zh-CN"

intersphinx_mapping = {
    "python": ("https://docs.python.org/zh-cn/3", None),
    "sphinx_docs": ("https://www.sphinx-doc.org/en/master", None),
    "MyST parser docs": ("https://myst-parser.readthedocs.io/en/latest", None),
}

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "furo"
html_theme = "sphinx_immaterial"
html_static_path = ["_static"]

# material theme options (see theme.conf for more information)
html_theme_options111 = {
    "font": {
        "text": "Roboto",  # used for all the pages' text
        "code": "Roboto Mono",  # used for literal code blocks
    },
    "site_url": "https://hellowac.github.io/practical_db_textbook-zh-cn/",
    "repo_url": "https://github.com/hellowac/practical_db_textbook-zh-cn/",
    "repo_name": "practical_db_textbook-zh-cn",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://hellowac.github.io/practical_db_textbook-zh-cn/",
    "repo_url": "https://github.com/hellowac/practical_db_textbook-zh-cn/",
    "repo_name": "practical_db_textbook-zh-cn",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        # "navigation.expand",
        "navigation.tabs",  #
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # BEGIN: version_dropdown
    "version_dropdown": True,
    # "version_info": [
    #     {
    #         "version": "https://sphinx-immaterial.rtfd.io",
    #         "title": "ReadTheDocs",
    #         "aliases": [],
    #     },
    #     {
    #         "version": "https://jbms.github.io/sphinx-immaterial",
    #         "title": "Github Pages",
    #         "aliases": [],
    #     },
    # ],
    # END: version_dropdown
    "toc_title_is_page_title": True,
    # BEGIN: social icons
    # "social": [
    #     {
    #         "icon": "fontawesome/brands/github",
    #         "link": "https://github.com/jbms/sphinx-immaterial",
    #         "name": "Source on github.com",
    #     },
    #     {
    #         "icon": "fontawesome/brands/python",
    #         "link": "https://pypi.org/project/sphinx-immaterial/",
    #     },
    # ],
    # END: social icons
}


# 创建自定义 Directive 类
class ActiveCodeDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True
    option_spec = {
        "language": str,
        "dburl": str,
    }

    def run(self):
        # 获取参数
        dburl = self.options.get("dburl", "")
        language = self.options.get("language", "plaintext")
        code_content = "\n".join(self.content)

        # 创建下载链接
        download_link = nodes.reference("", "sqlite3 file", refuri=dburl)

        # 创建节点
        code_node = nodes.literal_block(code_content, code_content)
        code_node["language"] = language  # 设置语言属性
        paragraph = nodes.paragraph(text="download: ")
        paragraph += download_link

        return [paragraph, code_node]


# 注册自定义 Directive
def setup(app: Sphinx):
    app.add_directive("activecode", ActiveCodeDirective)


# 使用自定义 Directive
"""
.. activecode::
    :language: sql
    :dburl: /_static/textbook.sqlite3

    SELECT * FROM fruit_stand;

"""
