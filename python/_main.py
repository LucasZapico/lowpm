import argparse
import os
import sys
import yaml
from utils.config import load_config, check_and_create_project_dir
from app import initialize, config
from utils.colorized_util import console
# TODO: review, maybe consolidate the handlers into one file
from handlers.init_handler import handle_init
from handlers.cli_args import handle_new



def main():
    # preloading and initializing the app
    initialize()
    # Load the config file
    

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

    # init command
    init_parser = subparsers.add_parser("init", help="Init lowpm in current directory")
    init_parser.add_argument(
        "--global", "-g",   action="store_true",  help="Init lowpm globally in user's home directory"
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
    elif args.command == "init": 
      # handler for "init" command
      handle_init(args)
    elif args.command == "new":
      # handler for "new" command
      handle_new(args)

    else:
        console.print(f"[cyan bold]lowpm[/cyan bold] doesn recongize the command: {args.command}\n[bold]Common commands:[/bold]\n[cyan]lowpm init[/cyan]: inits a lowpm in current dir allowing project specific config\n[cyan]lowpm new ---type page | board | list[/cyan]: create a new doc from template\n[cyan]lowpm --help[/cyan]: to see the available commands")


if __name__ == "__main__":
    main()
