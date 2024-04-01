
def create_new_board(board_config=None):
    # load app configs
    lowpm_config = load_config()

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    lowpm_dir = lowpm_config["dir"]
    # default board config on empty call

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.board.md"
    )

    frontmatter = update_frontmatter(lowpm_config["frontmatter"], "type", "board")
  
    brd_config = {
        "template": board_config["template"] or template_path,
        "name": board_config["name"] or "new.list.md",
        "path": board_config['path'] or ".",
        "frontmatter": frontmatter
        
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

    print(brd_config["frontmatter"])
    print(template_content)

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

    lowpm_dir = lowpm_config["dir"]
    # default page config on empty call

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.page.md"
    )

    frontmatter = update_frontmatter(lowpm_config["frontmatter"], "type", "page")

    pg_config = {
        "template": page_config["template"] or template_path,
        "name": page_config["name"] or "new.md",
        "path": page_config['path'] or ".",
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

    print(pg_config["frontmatter"])
    print(template_content)

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

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    # directory to where templates are 
    lowpm_dir = lowpm_config["dir"]
  
    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", "template.page.md"
    )


    li_config = {
        "template": board_config["template"] or template_path,
        "name": board_config["name"] or "new.list.md",
        "path": board_config['path'] or ".",
        "frontmatter": lowpm_config["frontmatter"],
        
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

    print(li_config["frontmatter"])
    print(template_content)

    # Convert the frontmatter to a YAML string
    frontmatter_string = yaml.dump(li_config["frontmatter"])

    # Prepend the frontmatter to the markdown content
    merged_content = f"---\n{frontmatter_string}---\n\n{template_content}"

    # Create the new file
    new_file_path = os.path.join(li_config["path"], li_config["name"])
    with open(new_file_path, "w") as file:
        file.write(merged_content)

        
def create_new_el(el_config):
    # load app configs
    lowpm_config = load_config()

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    lowpm_dir = lowpm_config["dir"]
    print(el_config)
    template_type = el_config["type"]

    

    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", f"template.{template_type}.md"
    )

    frontmatter = update_frontmatter(lowpm_config["frontmatter"], "type", template_type)
  
    el_config = {
        "template": el_config["template"] if el_config and "template" in el_config else template_path,
        "name": el_config["name"] if el_config and "name" in el_config else f"new.{template_type}.md",
        "path": el_config["path"] if el_config and "path" in el_config else ".",
        "frontmatter": frontmatter
    }

    # Load the template
    try:
        with open(el_config["template"], "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Template file {el_config['template']} not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error reading template file {el_config['template']}: {e}")
        return

    print(el_config["frontmatter"])


    # Convert the frontmatter to a YAML string
    frontmatter_string = yaml.dump(li_config["frontmatter"])

    # Prepend the frontmatter to the markdown content
    merged_content = f"---\n{frontmatter_string}---\n\n{template_content}"

    # Create the new file
    new_file_path = os.path.join(li_config["path"], li_config["name"])
    with open(new_file_path, "w") as file:
        file.write(merged_content)
