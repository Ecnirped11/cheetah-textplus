# from rich import printpentities
from rich.console import Console
from server.main_navigator import main_navigator
# import os
# import pyfiglet


def main() -> None:
    console = Console()
    main_navigator(console)


if __name__ == "__main__":
    main()
[]