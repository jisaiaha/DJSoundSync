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

def get_or_prompt_serato_path():
	path = get_serato_path()
	if os.path.isdir(path):
		return path

	# Get default Music folder for the user
	music_folder = str(Path.home() / "Music")

	print("No Serato path found. Please select your _Serato_ folder.")
	root = tk.Tk()
	root.withdraw()
	selected_path = filedialog.askdirectory(
		title="Select your _Serato_ folder",
		initialdir=music_folder
	)

	if selected_path:
		set_serato_path(selected_path)
		print(f"[INFO] Saved Serato path: {selected_path}")
		return selected_path
	else:
		print("[ERROR] No folder selected. Exiting.")
		exit(1)
