import markdown
import os
from bs4 import BeautifulSoup
import yaml
import frontmatter
import html2text

from utils.utils_markdown import get_frontmatter, html_to_md, md_to_html
from utils.logger import logger
from utils.misc import find_file_in_dir
from utils.config import load_config
from utils.doc_utils import update_doc, make_doc
from utils.misc import format_doc_file_name
from handlers.page import page_change_handler
from app import config

project_dir = os.path.abspath(config["project_dir"])
board_columns = config["board_columns"]

def handle_change(path):
    page_frontmatter = get_frontmatter(path)
    html_content = md_to_html(path)

    doc = {
        "frontmatter": page_frontmatter,
        "html": html_content,
        "path": path,
        "title": page_frontmatter["title"],
        "file_name": format_doc_file_name(page_frontmatter["title"])
    }

    if path.endswith(".md"):
        logger.info(f"Markdown file {path} has been modified")

        
        if path.endswith(".board.md"):
            # handle board
            logger.info(f"The file {path} is a board markdown file")
        elif path.endswith(".list.md"):
            # handle list
            logger.info(f"The file {path} is a list markdown file")
        else:
            logger.info("foo")
            # check if frontmatter has required keys
            if not check_page_frontmatter(page_frontmatter):
                logger.info(f"The file {path} missing required frontmatter keys for lowpm to work")
            # default to handling as page
            logger.info(f"The file {path} is a page markdown file")
            # if page has board key check that backlink exist on board in correct column

            page_change_handler(doc)

            

        
        # print(html_content)


# check if markdown frontmatter has "board", and "status" 
def check_page_frontmatter(frontmatter):
    if "boards" not in frontmatter:
        logger.info(f"The frontmatter in {frontmatter["title"]} does not have a board, missing 'boards' array")
        return False
    elif "status" not in frontmatter:
        logger.info(f"The frontmatter in {frontmatter["title"]} does not have a board, missing 'status' key")
        return False
    else:
        return True
