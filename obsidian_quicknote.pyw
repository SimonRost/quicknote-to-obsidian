import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import datetime
import os
import re
import json

CONFIG_FILE = "config.json"

def get_notes_folder():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
            folder = config.get("notes_folder", "").strip()
            if folder and os.path.isdir(folder):
                return folder
        except Exception as e:
            messagebox.showerror("Config Error", f"Error reading config file:\n{e}")

    # Ask user for folder
    folder = filedialog.askdirectory(title="Select your notes folder")
    if not folder:
        messagebox.showerror("No folder selected", "You must select a folder to save notes.")
        raise SystemExit()

    # Save it to config.json
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump({"notes_folder": folder}, f, indent=4)
    except Exception as e:
        messagebox.showerror("Save Error", f"Could not save config:\n{e}")
        raise

    return folder

NOTES_FOLDER = get_notes_folder()

def save_note():
    title = title_entry.get().strip()
    content = text_area.get("1.0", tk.END).strip()
    if not content:
        status_label.config(text="Note is empty, not saving.", fg="red")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if title:
        safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')
        filename = f"{timestamp}_{safe_title}.md"
    else:
        filename = f"{timestamp}_quicknote.md"
    filepath = os.path.join(NOTES_FOLDER, filename)

    os.makedirs(NOTES_FOLDER, exist_ok=True)

    with open(filepath, "w") as f:
        f.write(content)

    folder_name = os.path.basename(NOTES_FOLDER)
    display_path = os.path.join(folder_name, filename)
    status_label.config(text=f"Saved to {display_path}", fg="green")

    # Clear the fields
    title_entry.delete(0, tk.END)
    text_area.delete("1.0", tk.END)


# Create GUI
root = tk.Tk()
root.title("Quick Note to Obsidian")
root.geometry("500x400")
root.attributes('-topmost', True)

title_frame = tk.Frame(root)
title_frame.pack(fill=tk.X, padx=10, pady=(10, 0))

title_entry = tk.Entry(title_frame, font=("Arial", 10))
title_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 16))

text_area = scrolledtext.ScrolledText(root, width=58, height=15, font=("Arial", 10))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_area.focus()

status_label = tk.Label(root, text="Ready", fg="black")
status_label.pack(pady=(0, 5))

save_button = tk.Button(root, text="Save Note (Ctrl+S)", command=save_note)
save_button.pack(pady=5)

root.bind('<Control-s>', lambda event: save_note())
root.bind('<Escape>', lambda event: root.destroy())
title_entry.bind('<Tab>', lambda event: text_area.focus())

root.mainloop()
