import os
from bs4 import BeautifulSoup

from utils.misc import find_file_in_dir, format_doc_file_name
from app import config
from utils.utils_markdown import html_to_md
from utils.doc_utils import update_doc, make_doc
from utils.colorized_cli_utils import console
# comon
project_dir = os.path.abspath(config["project_dir"])
board_columns = config["board_columns"]

def get_boards_paths(frontmatter):
    if "boards" not in frontmatter:
        console.print("[bold dark_orange3]WARNING:[/bold dark_orange3] The page is missing the required 'boards' key in the frontmatter")
        return None
    # get board file names from frontmatter            
    board_file_names = [f"{board}.board.md" for board in frontmatter["boards"]]

    # find board files in project directory
    board_paths = [find_file_in_dir(project_dir, board_file_name) for board_file_name in board_file_names]
    return board_paths



def update_board_columns(board_path, board_frontmatter, board_html, page_frontmatter):
    # parse board html
    soup = BeautifulSoup(board_html, "html.parser")
    # format doc expected file name
    page_file_name = format_doc_file_name(page_frontmatter["title"])
    status_node = soup.find(lambda tag: tag.string == page_frontmatter["status"].strip())

    # check if doc exist in any column
    if has_matching_link(soup, page_file_name, page_frontmatter["title"]):
      print("Document has a matching link")
    else:
      print("Document does not have a matching link")
      # check if column has an existing list
      if has_ul_before_header(status_node):
        print("status_node does not have child nodes or does not exist")
        
      else:
        # if the column has no list create one and insert the doc link as list item
        add_doc_to_column(soup, status_node, page_frontmatter["title"], page_file_name)

    # transform html to markdown
    board_body_md = str(html_to_md(soup.prettify()))
    # update board doc
    updated_board = make_doc(board_body_md, board_frontmatter)
    # update_doc(f"{project_dir}/bar.board.md", str(updated_board))
    update_doc(board_path, str(updated_board))
    

# init check if changed doc already exists in any column
def has_matching_link(soup, page_file_name, title):
    for a in soup.find_all('a'):
        if a.get('href') == f"{page_file_name}.md" or a.text == title:
            return True
    return False



# add link to doc to column
def add_doc_to_column(soup, column_node, doc_name, doc_file_name ):
    # new_list = soup.new_tag("ul")
    new_list_item = soup.new_tag("li")
    new_list_item.string = f"[{doc_name.strip()}](.md)" if doc_name == doc_file_name else f"[{doc_name.strip()}]({doc_file_name}.md)" 
    # new_list.append(new_list_item)
    column_node.insert_after(new_list_item)
    
# check if column header has ul 
def has_ul_before_header(status_node):
    for sibling in status_node.next_siblings:
        if sibling.name == 'ul':
            return True
        if sibling.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            return False
    return False

