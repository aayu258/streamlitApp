from pathlib import Path
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# ---------------- FUNCTIONS ---------------- #

def create_file():
    file_name = simpledialog.askstring("Input", "Enter file name")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():
        messagebox.showerror("Error", "File already exists!")

    else:
        content = simpledialog.askstring("Input", "Enter file content")

        with open(file_name, 'w') as file:
            file.write(content)

        messagebox.showinfo("Success", "File created successfully!")

# ---------------- READ FILE ---------------- #

def read_file():

    file_name = simpledialog.askstring("Input", "Enter file name")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        with open(file_name, 'r') as file:
            data = file.read()

        messagebox.showinfo("File Content", data)

    else:
        messagebox.showerror("Error", "File not found!")

# ---------------- UPDATE FILE ---------------- #

def update_file():

    file_name = simpledialog.askstring("Input", "Enter file name")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        option = simpledialog.askinteger(
            "Update",
            "Press 1 for overwrite\nPress 2 for append"
        )

        content = simpledialog.askstring(
            "Input",
            "Enter new content"
        )

        mode = 'w' if option == 1 else 'a'

        with open(file_name, mode) as file:
            file.write(content)

        messagebox.showinfo("Success", "File updated!")

    else:
        messagebox.showerror("Error", "File not found!")

# ---------------- DELETE FILE ---------------- #

def delete_file():

    file_name = simpledialog.askstring("Input", "Enter file name")

    if not file_name:
        return

    p = Path(file_name)

    if p.exists():

        os.remove(p)

        messagebox.showinfo("Success", "File deleted!")

    else:
        messagebox.showerror("Error", "File not found!")

# ---------------- RENAME FILE ---------------- #

def rename_file():

    old_name = simpledialog.askstring("Input", "Enter old file name")

    if not old_name:
        return

    p = Path(old_name)

    if p.exists():

        new_name = simpledialog.askstring(
            "Input",
            "Enter new file name"
        )

        p.rename(new_name)

        messagebox.showinfo("Success", "File renamed!")

    else:
        messagebox.showerror("Error", "File not found!")

# ---------------- CREATE FOLDER ---------------- #

def create_folder():

    folder_name = simpledialog.askstring(
        "Input",
        "Enter folder name"
    )

    if not folder_name:
        return

    p = Path(folder_name)

    if p.exists():

        messagebox.showerror(
            "Error",
            "Folder already exists!"
        )

    else:

        p.mkdir()

        messagebox.showinfo(
            "Success",
            "Folder created!"
        )

# ---------------- DELETE FOLDER ---------------- #

def delete_folder():

    folder_name = simpledialog.askstring(
        "Input",
        "Enter folder name"
    )

    if not folder_name:
        return

    p = Path(folder_name)

    if p.exists():

        p.rmdir()

        messagebox.showinfo(
            "Success",
            "Folder deleted!"
        )

    else:

        messagebox.showerror(
            "Error",
            "Folder not found!"
        )

# ---------------- GUI WINDOW ---------------- #

root = tk.Tk()

root.title("CRUD File Handling Project")

root.geometry("400x500")

title = tk.Label(
    root,
    text="CRUD File Handling",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

buttons = [

    ("Create File", create_file),
    ("Read File", read_file),
    ("Update File", update_file),
    ("Delete File", delete_file),
    ("Rename File", rename_file),
    ("Create Folder", create_folder),
    ("Delete Folder", delete_folder),

]

for text, command in buttons:

    btn = tk.Button(
        root,
        text=text,
        width=25,
        height=2,
        command=command
    )

    btn.pack(pady=10)

root.mainloop()