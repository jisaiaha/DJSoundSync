from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Playlist:
	name: str
	trackFilepaths: List[str]  # Full absolute paths to tracks
	
@dataclass
class Folder:
	name: str
	subfolders: List["Folder"] = field(default_factory=list)
	playlists: List[Playlist] = field(default_factory=list)

@dataclass
class Library:
	folders: List[Folder]
	allTracks: Dict[str, dict]  # path → track metadata