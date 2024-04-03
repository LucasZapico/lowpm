from bs4 import BeautifulSoup

from utils.utils_markdown import get_frontmatter, html_to_md, md_to_html
from utils.logger import logger
from utils.doc_utils import update_doc, make_doc


def page_change_handler(path):
    page_frontmatter = get_frontmatter(path)
    html_content = md_to_html(path)
    # check file type 
    # check the page status is in the correct column on the board
    # parse the board markdown file and check if the page is in the correct column
    board_paths = get_boards_paths(page_frontmatter)

    board_foo = board_paths[0]

    board_foo_frontmatter = get_frontmatter(board_foo)
    # get the html content of the board doc
    board_foo_html = md_to_html(board_foo)
    
    soup = BeautifulSoup(board_foo_html, "html.parser")
    
    # get html node of the pages current status 
    status_node = soup.find(lambda tag: tag.string == page_frontmatter["status"])

    #  check if a given column has children
    if status_node and not any(n for n in status_node if n.name):
        print("status_node does not have child nodes or does not exist")
        # if empty append page as list element to column
        # new_list = soup.new_tag("ul")
        new_list_item = soup.new_tag("li")
        new_list_item.string = f"{page_frontmatter["title"]}.md"
        # new_list.append(new_list_item)
        status_node.append(new_list_item)
    else:
        print("status_node has child nodes")
        # check list of status nodes for page if empty append page as list element to column

        # chekc other list and remove if page is in it
        
    board_body_md = str(html_to_md(soup.prettify()))

    

    updated_board = make_doc(board_body_md, board_foo_frontmatter)
    
    # update_board(board_foo, updated_board)
    update_doc(f"{project_dir}/bar.board.md", str(updated_board))