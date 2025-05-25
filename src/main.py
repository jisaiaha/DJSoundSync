from rich import print
from config_manager import get_or_prompt_serato_path, get_or_prompt_rekordbox_db_path

def main():
	print("[bold green]DJ Sound Sync CLI[/bold green]")
	serato_path = get_or_prompt_serato_path()
	rekordbox_db = get_or_prompt_rekordbox_db_path()

	print(f"[cyan]Using Serato folder:[/cyan] {serato_path}")
	print(f"[cyan]Using Rekordbox database:[/cyan] {rekordbox_db}")

	# TODO: Parse crates and display them here

if __name__ == "__main__":
	main()
