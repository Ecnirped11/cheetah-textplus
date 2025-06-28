import questionary
import os


def clear_screen() -> None:
    if os.name == "nt":  # windows system.
        os.system("cls")
    else:  # unix based system.
        os.system("clear")


def choice_selector(choices: list[str]) -> str:
    return questionary.select("Select an option", choices=choices).ask() or ""


def return_buffer() -> None:
    print("\n")
    choice_selector(["Back"])
