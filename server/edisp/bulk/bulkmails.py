import os
import questionary
from rich.console import Console
from server.edisp.single import cprompt

def select_file(console:Console, start_path: str) -> None:
    current_path = os.path.abspath(start_path)
    console.print(
        f"[bold]\n📄 Please select a [green]`.txt`[/green] file to send as your message[/bold]\n"
      )
    while True:
      try:
          entries = [".."] + os.listdir(current_path)
          entries = sorted(entries, key=lambda x: (not os.path.isdir(os.path.join(current_path, x)), x))
  
          selected = questionary.select(
              f"Current directory: {current_path}",
              choices=entries
          ).ask()
  
          if selected is None:
              print("Selection cancelled.")
              return None
  
          selected_path = os.path.join(current_path, selected)
  
          if os.path.isdir(selected_path):
              current_path = os.path.abspath(selected_path)
          else:
              selected_file = os.path.abspath(selected_path)
              if selected_file.endswith(".txt"):
                  console.print(
                    f"\n[bold]file selected: [grey]{selected_file}[/grey][/bold]\n"
                  )
                  cprompt.content_prompt("bulk", selected_file)
              else:
                console.print(
                    f"[bold red]Only `.txt` files are allowed. Please choose a valid `.txt` file from the list[/bold red]"
                  )
      except PermissionError:
          break
              

