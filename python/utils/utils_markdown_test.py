import pytest
from utils.utils_markdown import md_to_html, get_frontmatter, html_to_md
from utils.colorized_cli_utils import print_info
from utils.config import project_root

test_doc_path = f"{project_root}/test/test_utils_markdown_test.md"


## take path to markdown file and return frontmatter
def test_get_frontmatter():
    """test: function to get frontmatter from markdown file"""
    print_info("--- test: parse frontmatter from md ---")
    frontmatter = get_frontmatter(test_doc_path)
    print_info(frontmatter)
    assert frontmatter == {"title": "test md doc"}


# ## take in raw html and return markdown
## TODO: (discovery) three \n after h1 ???
# # TODO: validate
def test_html_to_md():
    """test: function to convert html to markdwon"""
    print_info("--- test: function to convert html to markdwon ---")
    html = html_to_md("<h1>Hello</h1>\n<p>I'm a test md doc</p>")
    print_info(repr(html))
    print_info(repr(f"# Hello\n\n\nI'm a test md doc\n\n"))
    assert repr(html) == repr("# Hello\n\n\nI'm a test md doc\n\n")


# take in markdown path and get the html content
def test_md_to_html():
    """test: function to convert markdown to html"""
    print_info("--- test: function to convert markdown to html ---")
    content = md_to_html(test_doc_path)
    assert content == f"<h1>Hello</h1>\n<p>I'm a test md doc</p>"
