import argparse


def create_parser():
    """create parser"""
    return argparse.ArgumentParser(description="LowPm CLI")


def create_subparser(parser) -> argparse.ArgumentParser:
    """subparser creator"""
    return parser.add_subparsers(dest="command")


def create_cmd(subparsers, command: str, cmd_help: str) -> argparse.ArgumentParser:
    """subparser creator"""

    return subparsers.add_parser(command, help=cmd_help)


cli_args = [
    {
        "command": "hello",
        "help": "A little greeting from Lowpm CLI",
        "response": "Welcome to Lowpm, a filesystem first project management tool...yes another one.\nUse [cyan]lowpm --help[/cyan] to see the available commands",
    },
    {
        "command": "check",
        "help": "sanity check the project",
        "response": "checking project...",
    },
    {
        "command": "init",
        "help": "Init lowpm in current directory",
        "response": "Lowpm is now watching this directory, it will sync boards, pages and lists. See the docs for logic and syntax for creaeting relationships",
    },
    {
        "command": "new",
        "help": "lowpm new [filename | path/filename] --template [template] --type [type] --title [title] --name [name] ",
        "response": "Creating new project...",
    },
]

NO_ARGS_FOUND = "[cyan bold]lowpm[/cyan bold] doesn recongize the command: {args.command}\n[bold]Common commands:[/bold]\n[cyan]lowpm init[/cyan]: inits a lowpm in current dir allowing project specific config\n[cyan]lowpm new ---type page | board | list[/cyan]: create a new doc from template\n[cyan]lowpm --help[/cyan]: to see the available commands"


def cmd_parser(args: str) -> str:
    """parse commands from cli"""
    for arg in cli_args:
        if args.command == arg["command"]:
            return arg["response"]

    return "[cyan bold]lowpm[/cyan bold] doesn recongize the command: {args.command}\n[bold]Common commands:[/bold]\n[cyan]lowpm init[/cyan]: inits a lowpm in current dir allowing project specific config\n[cyan]lowpm new ---type page | board | list[/cyan]: create a new doc from template\n[cyan]lowpm --help[/cyan]: to see the available commands"


def init_parser():
    """init cli parser"""

    main_parser = create_parser()
    subparsers = create_subparser(main_parser)
    # define commands

    # create subparser commands
    for arg in cli_args:
        create_cmd(subparsers, arg["command"], arg["help"])

    return main_parser


parser = init_parser()
