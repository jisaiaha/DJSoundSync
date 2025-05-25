import argparse
from rich import print

def main():
	parser = argparse.ArgumentParser(description="CrateSync – Sync Serato and Rekordbox libraries")
	parser.add_argument("--version", action="version", version="CrateSync v0.1")
	args = parser.parse_args()

	print("[bold green]DJ Sound Sync CLI started![/bold green]")
	# More commands will go here

if __name__ == "__main__":
	main()
