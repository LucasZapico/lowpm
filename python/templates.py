import shutil
import os
import yaml
from utils.config import load_config, project_root


def update_frontmatter(frontmatter, key, value):
    frontmatter_dict = frontmatter
    frontmatter_dict[key] = value
    return frontmatter_dict


def create_new_board(board_config=None):
    # load app configs
    lowpm_config = load_config()
    project_dir = lowpm_config["project_dir"]

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    lowpm_dir = lowpm_config["dir"]

    base_frontmatter = lowpm_config["frontmatter"]["base"]
    board_frontmatter = (
        lowpm_config["frontmatter"]["board"]
        if lowpm_config["frontmatter"]["board"]
        else None
    )

    frontmattter = (
        {**base_frontmatter, **board_frontmatter}
        if board_frontmatter
        else base_frontmatter
    )

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.board.md"
    )

    frontmatter = update_frontmatter(base_frontmatter, "type", "board")

    el_type = board_config["type"]

    brd_config = {
        "template": board_config["template"] or template_path,
        "name": board_config["name"] or f"new.{el_type}.md",
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
    with open(new_file_path, "w") as file:
        file.write(merged_content)


def create_new_page(page_config=None):
    # load app configs
    lowpm_config = load_config()

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return
    base_frontmatter = lowpm_config["frontmatter"]["base"]
    page_frontmatter = (
        lowpm_config["frontmatter"]["page"]
        if lowpm_config["frontmatter"]["page"]
        else None
    )

    frontmattter = (
        {**base_frontmatter, **page_frontmatter}
        if page_frontmatter
        else base_frontmatter
    )

    lowpm_dir = lowpm_config["dir"]
    project_dir = lowpm_config["project_dir"]

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.page.md"
    )

    frontmatter = update_frontmatter(base_frontmatter, "type", "page")

    el_type = page_config["type"]

    pg_config = {
        "template": page_config["template"] or template_path,
        "name": page_config["name"] or "new.md",
        "path": page_config["path"] or project_dir,
        "frontmatter": frontmatter,
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

    with open(new_file_path, "w") as file:
        file.write(merged_content)


def create_new_list(list_config=None):
    # load app configs
    lowpm_config = load_config()
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

    frontmatter = (
        {**base_frontmatter, **list_frontmatter}
        if list_frontmatter
        else base_frontmatter
    )

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.page.md"
    )

    el_type = list_config["type"]

    li_config = {
        "template": list_config["template"] or template_path,
        "name": list_config["name"] or f"new.{el_type}.md",
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
    with open(new_file_path, "w") as file:
        file.write(merged_content)


# TODO: consolidate into single function that takes,
