from rich import print
from config_manager import get_or_prompt_serato_path, get_or_prompt_rekordbox_db_path, get_or_prompt_rekordbox_xml_path
from parsers.rekordbox_parser import load_rekordbox_xml_library
from models import Folder

def print_folder(folder: Folder, indent: int = 0):
	prefix = "    " * indent
	print(f"{prefix}[Folder] {folder.name}")
	for pl in folder.playlists:
		print(f"{prefix}  └─ [Playlist] {pl.name} ({len(pl.trackFilepaths)} tracks)")
	for sub in folder.subfolders:
		print_folder(sub, indent + 1)

def main():
	print("[bold green]DJ Sound Sync CLI[/bold green]")
	serato_path = get_or_prompt_serato_path()
	rekordbox_db = get_or_prompt_rekordbox_db_path()

	print(f"[cyan]Using Serato folder:[/cyan] {serato_path}")
	print(f"[cyan]Using Rekordbox database:[/cyan] {rekordbox_db}")

	rb_xml = get_or_prompt_rekordbox_xml_path()
	rb_lib = load_rekordbox_xml_library(rb_xml)

	print("[bold cyan]Rekordbox Folder/Playlist Structure:[/bold cyan]")
	for folder in rb_lib.folders:
		print_folder(folder)

if __name__ == "__main__":
	main()
