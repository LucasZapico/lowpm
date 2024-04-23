from rich.console import Console

console = Console()

def print_error(message: str, *err):
    tag = Text("ERROR:", style="bold red")
    console.print(tag, message, *err)

def print_info(message: str, *args):
    tag = Text("INFO:", style="bold cyan")
    console.print(tag, message, *args)

def print_warning(message: str, *args):
    tag = Text("WARNING:", style="bold yellow")
    console.print(tag, message, *args)

def print_success(message: str, *args):
    tag = Text("SUCCESS:", style="bold green")
    console.print(tag, message, *args)