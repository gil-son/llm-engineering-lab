from rich.console import Console
from rich.text import Text

def print_llm_result(prompt, response):
    """
    Print LLM prompt, response and token usage with colored formatting
"""
    console = Console()
    
    # Print prompt
    console.print(Text("USER PROMPT:", style="bold green"))
    console.print(Text(prompt, style="bold blue"), end="\n\n")
    
    # Print response
    console.print(Text("LLM RESPONSE:", style="bold green"))
    console.print(Text(response.content, style="bold blue"), end="\n\n")
    
    # Print token usage
    usage = response.response_metadata['token_usage']
    console.print(f"[bold white]Input tokens:[/bold white] [bright_black]{usage['prompt_tokens']}[/bright_black]")
    console.print(f"[bold white]Output tokens:[/bold white] [bright_black]{usage['completion_tokens']}[/bright_black]")
    console.print(f"[bold white]Total tokens:[/bold white] [bright_black]{usage['total_tokens']}[/bright_black]")
    console.print(f"[yellow]{'-'*50} [/yellow]")