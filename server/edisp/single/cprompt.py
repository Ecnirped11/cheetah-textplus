from rich.prompt import Prompt
from rich.console import Console
from rich.progress import track
from server.edisp.sdispatch import EmailHandler
from server.common_utils import return_buffer
from yaspin import yaspin
import time

console = Console()

def content_prompt(send_type: str, mails_file,) -> None:
      subject = Prompt.ask("\n[bold][green]╾➤ [/green] Subject[/bold]")
      header = Prompt.ask("\n[bold][green]╾➤ [/green] Header[/bold]")
      if send_type == "single":
          to = Prompt.ask("\n[bold][green]╾➤ [/green] To[/bold]")
      else:
          console.print(
            "\n[bold][green]╾➤ [/green] To[/bold]: selected file"
            )
          
      message = Prompt.ask("\n[bold][green]╾➤ [/green] Message[/bold]")
  
      if send_type == "single":
          with yaspin(text='sending..' , color='cyan') as spinner:
              handler = EmailHandler(subject, header, to, message)
              time.sleep(1)
              spinner.ok('done!')
              handler.dispatch()
              return_buffer()
      elif send_type == "bulk":
          with open(mails_file, "r") as m_file:
              for mails in track(m_file , description='sending email...'):
                 handler = EmailHandler(subject, header, mails, message)
                 handler.dispatch()
                 time.sleep(1)
                  
                  
      
