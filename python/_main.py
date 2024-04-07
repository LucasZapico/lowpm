import argparse
import os
import sys
import yaml
from utils.config import load_config, check_and_create_project_dir
from templates import create_new_board, create_new_list, create_new_page
from app import initialize
from utils.colorized_util import console

def main():
    # preloading and initializing the app
    initialize()
    # Load the config file
    config = load_config()    

    if not config:
        print("Exiting...")
        return

    # parse arguments from CLI
    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    # hello command
    hello_parser = subparsers.add_parser(
        "hello", help="A little greeting from Lowpm CLI"
    )

    new_parser = subparsers.add_parser("new", help="New project")
    new_parser.add_argument("--template", help="Path to unqiue template")
    new_parser.add_argument("--type", help="Type, board, list, page")
    new_parser.add_argument("--name", help="Name of the new project")
    new_parser.add_argument("--path", help="Path where the new project will be created")

    args = parser.parse_args()

    # Now you can access the values with args.new, args.template, args.name, args.path
    # Add your logic here
    if args.command == "hello":
        print(
            "Welcome to Lowpm, a filesystem first project management tool...yes another one. Use lowpm --help to see the available commands"
        )
    elif args.command == "new":
        # Check the type argument
        if args.type not in ["board", "page", "list", None]:
            print(
                f"Invalid type: {args.type}. Type must be 'board', 'page', 'list', or None."
            )
            return

        config = {"template": args.template, "path": args.path, "name": args.name}

        # Check if the type is board, list, or page
        if args.type == "board":
            create_new_board({**config, **{"type": "board"}})
        elif args.type == "list":
            create_new_list({**config, **{"type": "list"}})
        elif args.type == "page":
            create_new_page({**config, "type": "page"})
        else:
            # default to new page with new.md
            create_new_page({**config, "type": "page"})

    else:
        console.print(f"[cyan bold]lowpm[/cyan bold] doesn recongize the command: {args.command}\n[bold]Common commands:[/bold]\n[cyan]lowpm init[/cyan]: inits a lowpm in current dir allowing project specific config\n[cyan]lowpm new ---type page | board | list[/cyan]: create a new doc from template\n[cyan]lowpm --help[/cyan]: to see the available commands")


if __name__ == "__main__":
    main()
