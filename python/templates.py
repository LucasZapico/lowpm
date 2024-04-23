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

def create_file_name(doc_type, name):
    if doc_type == "page":
        doc_name = f"new.md" if not name else f"{name}.md" 
    else:
        doc_name = f"new.{doc_type}.md" if not name else f"{name}.{doc_type}.md"
    return doc_name


    
def create_new_doc(doc_config=None):
    # load app configs
    lowpm_config = config
    project_dir = lowpm_config["project_dir"]
    doc_type = doc_config["type"]
    # get the full doc path
    doc_path = os.path.join(os.getcwd(), doc_config["name"])
    # get file name of doc
    doc_file_name = os.path.basename(doc_path)

    # Check if load_config() returned a dictionary
    if not isinstance(lowpm_config, dict):
        print("Error: load_config() did not return a dictionary.")
        return

    lowpm_dir = lowpm_config["dir"]

    # get the base config of frontmatter for all docs
    base_frontmatter = OrderedDict(lowpm_config["frontmatter"]["base"])
    # append the frontmatter for the specific doc type
    doc_frontmatter = (
        OrderedDict(lowpm_config["frontmatter"][doc_type])
        if lowpm_config["frontmatter"][doc_type]
        else None
    )

    frontmatter = doc_frontmatter
    
    # Define the path to the template
    template_path = os.path.join(
        project_root, lowpm_dir, "templates", f"template.{doc_type}.md"
    )

    # create doc name by type 
    doc_file_name = create_file_name(doc_type, doc_config["name"])

    # define final doc config
    final_config = {
        "template": doc_config["template"] or template_path,
        "name": doc_file_name,
        "path": doc_config["path"] or project_dir,
        "frontmatter": frontmatter,
    }

    # Load the template
    try:
        with open(final_config["template"], "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print(f"Template file {final_config['template']} not found.")
        return
    except yaml.YAMLError as e:
        print(f"Error reading template file {final_config['template']}: {e}")
        return

    # Convert the frontmatter to a YAML string
    frontmatter_string = yaml.dump(final_config["frontmatter"])

    # Prepend the frontmatter to the markdown content
    merged_content = f"---\n{frontmatter_string}---\n\n{template_content}"
    
    # check new direcoties is passed in path string
    # if not os.path.exists(doc_path):
    #     os.makedirs(doc_path)

    # Create the new file
    doc_path = os.path.join(final_config["path"], final_config["name"])

    if os.path.exists(doc_path):
      console.print(f'[bold  dark_orange3 ]WARNING:[/bold dark_orange3] The file [bold]{doc_path}[/bold] already exists')
    else:
      with open(doc_path, 'w') as file:
        file.write(merged_content)


