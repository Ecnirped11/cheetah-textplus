from rich import print
from server.common_utils import choice_selector, clear_screen
import pyfiglet
from rich.console import Console


def print_sms_banner(console: Console) -> None:
    clear_screen()
    banner = pyfiglet.figlet_format("CH . SMS", font="ansi_shadow")
    console.print(banner, justify="center")
    
   
    console.print(
        "[bold green]Deliver SMS straight to your clients inboxes.\n[/bold green]",
        justify="center",
    )


def sms_navigator(console: Console) -> None:
    while True:
        print_sms_banner(console)

        option = choice_selector(["Single SMS", "Bulk SMS", "Back to Home"])

        if option == "Back to Home":
            break
        elif option == "Single SMS":
            print(
                "[bold yellow]Single SMS functionality is not implemented yet.[/bold yellow]"
            )
        elif option == "Bulk SMS":
            print(
                "[bold yellow]Bulk SMS functionality is not implemented yet.[/bold yellow]"
            )
