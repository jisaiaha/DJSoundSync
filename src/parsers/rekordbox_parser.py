import xml.etree.ElementTree as ET
from typing import List, Dict
from models import Library, Folder, Playlist


def load_rekordbox_xml_library(xml_path: str) -> Library:
	"""
	Parses a Rekordbox XML export into a folder-based Library structure.
	Each <NODE> of Type 0 becomes a Folder, and Type 1 becomes a Playlist.
	"""

	tree = ET.parse(xml_path)
	root = tree.getroot()

	# Build TrackID → file path lookup
	track_lookup: Dict[str, str] = {}
	collection = root.find("COLLECTION")

	if collection is not None:
		for track_elem in collection.findall("TRACK"):
			track_id = track_elem.get("TrackID")
			location = track_elem.get("Location")
			if track_id and location and location.startswith("file://localhost/"):
				path = location.replace("file://localhost/", "").replace("%20", " ")
				track_lookup[track_id] = path

	# Recursive function to convert <NODE> → Folder/Playlist
	def parse_node(node: ET.Element) -> Folder:
		folder_name = node.get("Name", "Unnamed")
		folder = Folder(name=folder_name)

		for child in node.findall("NODE"):
			node_type = child.get("Type")
			child_name = child.get("Name", "Unnamed")

			if node_type == "0":
				# Subfolder
				folder.subfolders.append(parse_node(child))

			elif node_type == "1":
				# Playlist
				track_filepaths = []
				for track_ref in child.findall("TRACK"):
					key = track_ref.get("Key")
					if key and key in track_lookup:
						track_filepaths.append(track_lookup[key])
				playlist = Playlist(name=child_name, trackFilepaths=track_filepaths)
				folder.playlists.append(playlist)

		return folder

	# Start at top-level <PLAYLISTS>
	root_folders: List[Folder] = []
	playlists_elem = root.find("PLAYLISTS")

	if playlists_elem is not None:
		for top_node in playlists_elem.findall("NODE"):
			if top_node.get("Type") == "0":  # Must be a folder
				root_folders.append(parse_node(top_node))

	return Library(folders=root_folders, allTracks={})
