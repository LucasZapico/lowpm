from bs4 import BeautifulSoup
import os

from app import config
from utils.utils_markdown import get_frontmatter, html_to_md, md_to_html
from utils.logger import logger
from utils.doc_utils import update_doc, make_doc
from utils.misc import format_doc_file_name
from handlers.board import get_boards_paths
from handlers.board import update_board_columns, get_boards_paths

# comon

project_dir = os.path.abspath(config["project_dir"])
board_columns = config["board_columns"]

def page_change_handler(page):

    page_frontmatter = page["frontmatter"]
    html_content = page["html"]
    page_file_name = page["file_name"]
    page_path = page["path"]
    page_title = page["title"]
    
    # check file type 
    # check the page status is in the correct column on the board
    # parse the board markdown file and check if the page is in the correct column
    board_paths = get_boards_paths(page_frontmatter)

    for board_path in board_paths:
        board_frontmatter = get_frontmatter(board_path)
        # get the html content of the board doc
        board_html = md_to_html(board_path)
        update_board_columns(board_path, board_frontmatter, board_html, page_frontmatter )

    