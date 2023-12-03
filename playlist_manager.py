import sys
from utils.command_handler import handle_command_line_args

def main():
    handle_command_line_args(sys.argv[1:])

if __name__ == "__main__":
    main()