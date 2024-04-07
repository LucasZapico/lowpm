from templates import create_new_board, create_new_list, create_new_page

def handle_new(args):
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