import sys
from utils import CommandHandler

def main():
    command_handler = CommandHandler()
    command_handler.handle_command_line_args(sys.argv[1:])

if __name__ == "__main__":
    main()