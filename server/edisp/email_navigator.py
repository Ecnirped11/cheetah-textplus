from rich import print
from server.edisp.single import cprompt
from server.edisp.bulk import bulkmails
from rich.panel import Panel
from rich import box
from server.common_utils import choice_selector, clear_screen
import pyfiglet
from rich.console import Console


def print_email_banner(console: Console) -> None:
    clear_screen()
  
    banner = pyfiglet.figlet_format("path", font="ansi_shadow")
    console.print(banner, justify="center")
    
    description = ("[bold]Deliver personalized or bulk messages straight to your clients inboxes.\n[/bold]")
    ht = Panel(description , title="Smart Dispatch", border_style='white', box=box.DOUBLE )
    console.print(ht, justify="center")
    


def email_navigator(console: Console) -> None:
    
        print_email_banner(console)

        option = choice_selector(["Single message", "Bulk message", "Back to Home"])

        #if option == "Back to Home":
          
        if option == "Single message":
            cprompt.content_prompt("single", False)
        elif option == "Bulk message":
            selected_file = bulkmails.select_file(console,"/storage/emulated/0")
        