from rich import print
from config_manager import get_or_prompt_serato_path

def main():
	print("[bold green]DJ Sound Sync CLI[/bold green]")
	serato_path = get_or_prompt_serato_path()
	print(f"[cyan]Using Serato folder:[/cyan] {serato_path}")

	# TODO: Parse crates and display them here

if __name__ == "__main__":
	main()
