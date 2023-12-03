import sys
from modules import PlaylistManager
from config.config import action_mapping

def display_help():
    print("Usage: python playlist_manager.py <action> <name>")
    print("\nAvailable actions:")
    for action, method_name in action_mapping.items():
        print(f"  - {action}: {method_name}")

def handle_command_line_args(args):
    if not args:
        display_help()
        sys.exit(1)

    action = args[0]

    # Instantiate PlaylistManager
    playlist_manager = PlaylistManager()

    method_name = action_mapping.get(action)

    if method_name:
        action_function = getattr(playlist_manager, method_name, None)

        if action_function and callable(action_function):
            action_function(*args[1:])
        else:
            print(f"Unsupported action: {action}")
            sys.exit(1)
    else:
        print(f"Unknown action: {action}")
        display_help()
        sys.exit(1)