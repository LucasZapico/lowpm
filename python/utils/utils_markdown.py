import frontmatter
from markdownify import markdownify as md
import markdown

# take path to markdown file and return frontmatter
def get_frontmatter(path):
    if path.endswith(".md"):
        with open(path, "r") as file:
            doc = frontmatter.load(file)
            return doc.metadata


# take in raw html and return markdown
# TODO: validate
def html_to_md(html):
    
    # h.ul_item_mark = '-'
    return md(html, heading_style="ATX", bullets="-")
    

# take in markdown path and get the html content
def md_to_html(path):
    if path.endswith(".md"):

        with open(path, "r") as file:
            doc = frontmatter.load(file)
            html_content = markdown.markdown(doc.content)
            return html_content