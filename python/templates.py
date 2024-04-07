import shutil
import os
import yaml
from utils.config import load_config, project_root
from collections import OrderedDict
from utils.colorized_util import console
from app import config

def update_frontmatter(frontmatter, key, value):
    frontmatter_dict = frontmatter
    frontmatter_dict[key] = value
    return frontmatter_dict


def create_new_board(board_config=None):
    # load app configs
    lowpm_config = config
    project_dir = lowpm_config["project_dir"]

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    lowpm_dir = lowpm_config["dir"]

    base_frontmatter = OrderedDict(lowpm_config["frontmatter"]["base"])
    board_frontmatter = (
        OrderedDict(lowpm_config["frontmatter"]["board"])
        if lowpm_config["frontmatter"]["board"]
        else None
    )

    frontmatter_with_type = update_frontmatter(base_frontmatter, "type", "baord")

    if board_frontmatter:
        frontmatter_with_type.update(board_frontmatter)
    
    frontmatter = frontmatter_with_type
    
    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.board.md"
    )

    frontmatter = update_frontmatter(base_frontmatter, "type", "board")

    el_type = board_config["type"]

    brd_config = {
        "template": board_config["template"] or template_path,
        "name": f"new.{el_type}.md" if not board_config["name"] else f"{board_config["name"]}.{el_type}.md",
        "path": board_config["path"] or project_dir,
        "frontmatter": frontmatter,
    }

    # Load the template
    try:
        with open(brd_config["template"], "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Template file {brd_config['template']} not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error reading template file {brd_config['template']}: {e}")
        return

    # Convert the frontmatter to a YAML string
    frontmatter_string = yaml.dump(brd_config["frontmatter"])

    # Prepend the frontmatter to the markdown content
    merged_content = f"---\n{frontmatter_string}---\n\n{template_content}"

    # Create the new file
    new_file_path = os.path.join(brd_config["path"], brd_config["name"])

    if os.path.exists(new_file_path):
      console.print(f'[bold  dark_orange3 ]WARNING:[/bold dark_orange3] The file [bold]{new_file_path}[/bold] already exists')
    else:
      with open(new_file_path, 'w') as file:
        file.write(merged_content)


def create_new_page(page_config=None):
    # load app configs
    lowpm_config = config

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return
    base_frontmatter = OrderedDict(lowpm_config["frontmatter"]["base"])
    page_frontmatter = (
        OrderedDict(lowpm_config["frontmatter"]["page"])
        if lowpm_config["frontmatter"]["page"]
        else None
    )

    # add doc type to frontmatter
    frontmatter_with_type = update_frontmatter(base_frontmatter, "type", "page")

    if page_frontmatter:
        frontmatter_with_type.update(page_frontmatter)
    frontmatter = frontmatter_with_type    
    # update frontmatter name 
    if page_config["name"]:
        frontmatter = update_frontmatter(frontmatter, "title", page_config["name"])

    lowpm_dir = lowpm_config["dir"]
    project_dir = lowpm_config["project_dir"]

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.page.md"
    )

    pg_config = {
        "template": page_config["template"] or template_path,
        "name": f"new.md" if not page_config["name"] else f"{page_config["name"]}.md" ,
        "path": page_config["path"] or project_dir,
        "frontmatter": frontmatter
    }

    # Load the template
    try:
        with open(pg_config["template"], "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Template file {pg_config['template']} not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error reading template file {pg_config['template']}: {e}")
        return

    # Convert the frontmatter to a YAML string
    frontmatter_string = yaml.dump(pg_config["frontmatter"])

    # Prepend the frontmatter to the markdown content
    merged_content = f"---\n{frontmatter_string}---\n\n{template_content}"

    # Create the new file
    new_file_path = os.path.join(pg_config["path"], pg_config["name"])
    console.print(f"new page path: {new_file_path}")
    if os.path.exists(new_file_path):
      console.print(f'[bold  dark_orange3 ]WARNING:[/bold dark_orange3] The file [bold]{new_file_path}[/bold] already exists')
    else:
      with open(new_file_path, 'w') as file:
        file.write(merged_content)

    


def create_new_list(list_config=None):
    # load app configs
    lowpm_config = config
    project_dir = lowpm_config["project_dir"]

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    # directory to where templates are
    lowpm_dir = lowpm_config["dir"]

    base_frontmatter = lowpm_config["frontmatter"]["base"]
    list_frontmatter = (
        lowpm_config["frontmatter"]["list"]
        if lowpm_config["frontmatter"]["list"]
        else None
    )

    frontmatter_with_type = update_frontmatter(base_frontmatter, "type", "list")

    if list_frontmatter:
        frontmatter_with_type.update(list_frontmatter)

    frontmatter = frontmatter_with_type

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.page.md"
    )

    el_type = list_config["type"]

    li_config = {
        "template": list_config["template"] or template_path,
        "name": f"new.{el_type}.md" if not list_config["name"] else f"{list_config["name"]}.{el_type}.md",
        "path": list_config["path"] or project_dir,
        "frontmatter": frontmatter,
    }

    # Load the template
    try:
        with open(li_config["template"], "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Template file {li_config['template']} not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error reading template file {li_config['template']}: {e}")
        return

    # Convert the frontmatter to a YAML string
    frontmatter_string = yaml.dump(li_config["frontmatter"])

    # Prepend the frontmatter to the markdown content
    merged_content = f"---\n{frontmatter_string}---\n\n{template_content}"

    # Create the new file
    new_file_path = os.path.join(li_config["path"], li_config["name"])
    
    if os.path.exists(new_file_path):
      console.print(f'[bold  dark_orange3 ]WARNING:[/bold dark_orange3] The file [bold]{new_file_path}[/bold] already exists')
    else:
      with open(new_file_path, 'w') as file:
        file.write(merged_content)


# TODO: consolidate into single function that takes,
