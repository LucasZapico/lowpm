import argparse
import os
import sys
import yaml
from utils.config import load_config, check_and_create_project_dir
from app import initialize, config
from utils.colorized_cli_utils import console

# TODO: review, maybe consolidate the handlers into one file
from handlers.init_handler import handle_init
from handlers.cli_args import handle_new
from watchers import watch_directory
from rich import print

def main():
    print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
    # preloading and initializing the app
    initialize()
    # Load the config file

    if not config:
        print("Exiting...")
        return

    # parse arguments from CLI
    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    ##
    ## "hellow" command
    ##
    hello_parser = subparsers.add_parser(
        "hello", help="A little greeting from Lowpm CLI"
    )

    # temp: handling watch
    wath_parser = subparsers.add_parser("watch", help="Watch a directory for changes")

    ##
    ## "init" command
    ##
    init_parser = subparsers.add_parser("init", help="Init lowpm in current directory")
    init_parser.add_argument(
        "--global",
        "-g",
        action="store_true",
        help="Init lowpm globally in user's home directory",
    )

    ##
    ## "new" command
    ##
    new_parser = subparsers.add_parser("new", help="lowpm new [filename | path/filename] --template [template] --type [type] --title [title] --name [name] ")
    new_parser.add_argument('path', nargs='?', default=os.getcwd(), help="Path to create the new project")
    new_parser.add_argument(
        "--template", "-tplt", help="Path to unqiue template"
    )
    new_parser.add_argument(
        "--type", "-tp", help="Type, board, list, page"
    )
    new_parser.add_argument(
        "--title", "-tile", help="title of doc in frontmatter"
    )
    new_parser.add_argument(
        "--name", "-n", help="Name of the new project"
    )
    # new_parser.add_argument(
    #     "--path",
    #     "-p",
    #     help="Path where the new project will be created",
    # )

    args = parser.parse_args()

    # Now you can access the values with args.new, args.template, args.name, args.path
    # Add your logic here
    if args.command == "hello":
        print(
            "Welcome to Lowpm, a filesystem first project management tool...yes another one.\nUse [cyan]lowpm --help[/cyan] to see the available commands"
        )
    elif args.command == "watch":
        watch_directory(config["project_dir"])
    elif args.command == "init":
        # handler for "init" command
        handle_init(args)
    elif args.command == "new":
        # handler for "new" command
        handle_new(args)

    else:
        print(
            f"[cyan bold]lowpm[/cyan bold] doesn recongize the command: {args.command}\n[bold]Common commands:[/bold]\n[cyan]lowpm init[/cyan]: inits a lowpm in current dir allowing project specific config\n[cyan]lowpm new ---type page | board | list[/cyan]: create a new doc from template\n[cyan]lowpm --help[/cyan]: to see the available commands"
        )


if __name__ == "__main__":
    main()
