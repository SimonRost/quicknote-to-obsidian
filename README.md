# 📝 Quick Note to Obsidian

A simple Python GUI tool to quickly jot down notes and save them as `.md` (Markdown) files directly into your Obsidian vault — or any other folder you choose.

I started using Obsidian a few months ago and often found myself wanting to quickly capture a short thought, a citation, a code snippet, or a project idea. But having to switch to Obsidian just to create a new note broke my workflow. So I built this tool to solve that — a minimal, always-ready note window that saves straight to my vault’s "inbox" for later processing.

This is great for quickly capturing thoughts, journal entries, or TODOs without opening a full editor.

---

## 📦 Features

- Clean and minimal Tkinter-based GUI
- Saves notes in Markdown format
- Automatically timestamps filenames
- Optional note titles (used in filename)
- Remembers your save location after first launch
- Keyboard shortcuts:
  - `Ctrl+S` — Save note
  - `Esc` — Close app
  - `Tab` — Jump from title to text field

---

## 🚀 How to Use

1. 🐍 Make sure you have **Python 3.6+** installed.
2. 🧾 Run `main.pyw`:
   ```bash
   python main.py
3. 📁 On first run, you'll be asked to choose a folder where your notes will be saved (e.g., an Obsidian vault).

4. 📝 Type your note and optionally a title.

5. 💾 Press Ctrl+S or click "Save Note" — the note will be saved as a .md file in the selected folder.

6. ✅ A config.json file will be created to remember your chosen folder for next time.

---

## 🎯 Add a Global Hotkey on Windows
You can launch this app with a custom keyboard shortcut in Windows:

**1. Create a shortcut:**
- Right-click on `main.pyw`.
- Choose **Send to → Desktop** (create shortcut).

**2. Configure the shortcut:**
- Right-click the new shortcut on your desktop and select **Properties**.
- In the **Target** field, make sure it looks like this:
`pythonw.exe "C:\path\to\quick-note-to-obsidian\main.pyw"`
  - If Python isn't in PATH note direct path to pythonw.exe:<br>`"C:\Users\YourUsername\AppData\Local\Programs\Python\Python312\pythonw.exe" "C:\full\path\to\your\project\main.pyw"`<br>
(Adjust the path to your Python installation if needed.)
**3. Assign a hotkey:**
- In the same Properties window, go to the **Shortcut** tab.
- Click the **Shortcut key** field and press your desired combo (e.g., `Ctrl + Alt + N`).
- Click **OK**.

Now you can launch the app instantly with your chosen hotkey.

---

## 🛠 Dependencies

Only uses Python's standard library:

- tkinter
- datetime
- os, re, json

No installation needed beyond Python itself.

---

## 🧠 File Naming Logic

Notes are saved as:
```text
YYYYMMDD_HHMMSS_Title.md
```
If no title is given:
```text
YYYYMMDD_HHMMSS_Title.md
```

---

## 💡 Tip for Developers

To reset or change your note folder, just delete config.json and restart the app.

## Project Structure
```bash
quick-note-to-obsidian/
├── main.pyw           # The application script
├── config.json       # Auto-generated on first run (not needed upfront)
└── README.md         # You're reading it
```

---

## 🗺️ Quick Note to Obsidian – Roadmap

 Ideas are grouped by feasibility and complexity.

### ✅ Likely Next Steps (Short-Term)

These features are realistic to implement soon and would enhance the core functionality:

- 🔲 **Note Log:**
Maintain a local `.json` or `.md` log of all saved notes, including timestamp, filename, and a content preview.

- 🔲 **Quick-Paste from Clipboard:**
  Automatically paste copied text into the app when it opens via the hotkey.

- 🔲 **Attach Files or Images:**
  Allow attaching images or other files to a note. Files can be copied to the vault and embedded using standard Markdown syntax.

- 🔲 **Basic Settings UI:**
  Add a minimal settings window to adjust save folder, filename format, and other configurable options. Also make a "dark-mode" available.

- 🔲 **Daily Note Auto-Routing**
  Add option to route all notes into a single daily file like `2025-05-26.md`.

- 🔲 **Note Categories / Tags**
  Implement an option to use a dropdown or input field to categorize notes (e.g., `idea`, `todo`, `quote`, `code`).
---

## 🚀 Ambitious Ideas (Long-Term)

Stretch goals that would require more development effort or third-party tools/libraries:

- 🔲 **Snipping Tool-Like Capture:**
  Let users take a screenshot and include it directly in a note, with image saved and referenced in Markdown.

- 🔲 **Voice Notes + Transcription:**
  Record short voice memos and transcribe them using a service like OpenAI Whisper or Google Speech-to-Text.

- 🔲 **Global “Quick Capture” Hotkey + Auto-Paste:**
  Select text in any app, hit the hotkey, and have that text automatically appear in the note window.

- 🔲 **Markdown Template Support:**
  Enable reusable templates for consistent note structures (e.g., meeting notes, journal, project ideas).

- 🔲 **Tag Autocomplete**
  Suggest tags based on existing notes or a user-defined tag list.

- 🔲 **Tray Icon Mode**
  Run the app in the system tray with quick access options and recent notes history.

---

If you have feature suggestions or would like to contribute, feel free to open an issue or submit a pull request!

---

## 📜 License

MIT License — free to use, modify, and share. See LICENSE file for details.
