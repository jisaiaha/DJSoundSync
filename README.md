# CrateSync

CrateSync is a command-line tool (with a planned GUI) for synchronizing DJ libraries between **Serato DJ** and **Rekordbox**. It ensures that your **track lists, cue points, and especially playlists/crates** are consistent across both platforms — so your set prep isn't locked into one software.

---

## 🎯 Core Goals

- Sync **crates/playlists** between Serato and Rekordbox
- Detect and add missing tracks between libraries
- Sync **cue points** and later loops
- Allow one-way or two-way sync
- Prepare for GUI functionality later

---

## 📁 What It Syncs

| Feature            | CLI Version | GUI Version |
|-------------------|-------------|-------------|
| **Crates/Playlists** | 🔜        | ✅          |
| Track list        | ✅          | ✅          |
| Cue points        | 🔜          | ✅          |
| Loops             | ❌          | ✅          |
| Metadata (BPM, Key, etc.) | ❌    | ✅          |
| Smart sync options | ❌         | ✅          |

---

## 🔨 Tech Stack

- Python 3
- `mutagen` – read/write audio metadata
- `sqlite3` – access Rekordbox database
- `rich` – formatted CLI output (optional)
- Future: GUI using `tkinter`, `PyQT`, or `Electron`

---

## 🗓️ Development Timeline

| Phase | Timeline | Milestone |
|-------|----------|-----------|
| ✅ Project Setup | Week 1 | Repo, venv, CLI entry point |
| 🔄 Serato Parser | Week 2 | Parse crates, track metadata |
| 🧠 Rekordbox Reader | Week 3 | Read playlists from SQLite |
| 🧮 Diff Crates/Tracks | Week 4 | Compare playlists and files |
| 🔁 Sync Tracks | Week 5 | Add missing tracks to each library |
| 📦 Sync Crates | Week 6 | Recreate playlists from one to the other |
| 🎯 Cue Point Sync | Week 7 | One-way cue sync (S → R or R → S) |
| 🧪 Finalize CLI | Week 8 | Wrap commands, test, document |
| 🎨 GUI Phase Begins | End of Summer | Build user interface on top |

---

## 🧠 Future Ideas

- Conflict resolution for playlist/cue changes
- Color-coded cue point support
- Smart crate mapping (e.g., genre folders)
- Backup/export before sync
- Cross-platform support (Windows/macOS/Linux)

---

## 🙋 Who It’s For

- DJs switching between Serato & Rekordbox
- CDJ users who prep in both environments
- DJs building backup rigs with consistent libraries

---

## 🧪 Status

**🚧 CLI in development. Crate and cue point sync are top priorities. GUI coming late summer.**

---

## 📜 License

MIT – free to use, modify, and remix.
