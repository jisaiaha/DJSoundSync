import json
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

CONFIG_FILE = "config.json"

def create_config_if_missing():
	if not os.path.exists(CONFIG_FILE):
		with open(CONFIG_FILE, "w") as f:
			json.dump({}, f, indent=4)

def load_config():
	create_config_if_missing()
	with open(CONFIG_FILE, "r") as f:
		return json.load(f)

def save_config(config):
	create_config_if_missing()
	with open(CONFIG_FILE, "w") as f:
		json.dump(config, f, indent=4)

def get_serato_path():
	config = load_config()
	return config.get("seratoLibraryPath", "")

def set_serato_path(path):
	config = load_config()
	config["seratoLibraryPath"] = path
	save_config(config)

def is_valid_serato_folder(path):
	subcrates_path = os.path.join(path, "Subcrates")
	if not os.path.isdir(subcrates_path):
		return False

	# Check for at least one .crate file
	for filename in os.listdir(subcrates_path):
		if filename.endswith(".crate"):
			return True

	return False

def get_or_prompt_serato_path():
	path = get_serato_path()
	if os.path.isdir(path) and is_valid_serato_folder(path):
		return path

	# Prompt user with default Music folder as starting point
	music_folder = str(Path.home() / "Music")
	print("No valid Serato path found. Please select your _Serato_ folder.")
	root = tk.Tk()
	root.withdraw()
	while True:
		selected_path = filedialog.askdirectory(
			title="Select your _Serato_ folder",
			initialdir=music_folder
		)

		if not selected_path:
			print("[ERROR] No folder selected. Exiting.")
			exit(1)

		if is_valid_serato_folder(selected_path):
			set_serato_path(selected_path)
			print(f"[INFO] Saved Serato path: {selected_path}")
			return selected_path
		else:
			print("[red]That folder doesn't contain a valid Serato Subcrates folder. Please try again.[/red]")

