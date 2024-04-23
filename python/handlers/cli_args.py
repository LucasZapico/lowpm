from templates import create_new_doc
from utils.colorized_cli_utils import print_info

def handle_new(args):
    # Check the type argument
    print_info(f"Creating new document: {args.path}")
    
    if args.type not in ["board", "page", "list", None]:
        print(
            f"Invalid type: {args.type}. Type must be 'board', 'page', 'list', or None."
        )
        return

    config = {"template": args.template, "path": args.path, "name": args.name}

    # Check if the type is board, list, or page
    if args.type == "board":
        create_new_doc({**config, **{"type": "board"}})
    elif args.type == "list":
        create_new_doc({**config, **{"type": "list"}})
    elif args.type == "page":
        create_new_doc({**config, "type": "page"})
    else:
        # default to new page with new.md
        create_new_doc({**config, "type": "page"})