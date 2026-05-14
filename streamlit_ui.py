from pathlib import Path
import os
import streamlit as st

st.title("CRUD File Handling Project")

# ---------------- READ FILES/FOLDERS ---------------- #

def readfileandfolder():
    p = Path('.')
    items = list(p.rglob('*'))
    return items

# Sidebar menu
menu = [
    "Create File",
    "Read File",
    "Update File",
    "Delete File",
    "Rename File",
    "Create Folder",
    "Delete Folder"
]

choice = st.sidebar.selectbox("Select Operation", menu)

# Show existing files/folders
st.subheader("Existing Files & Folders")
items = readfileandfolder()

for item in items:
    st.write(item)

# ---------------- CREATE FILE ---------------- #

if choice == "Create File":

    st.header("Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("File already exists!")

        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("File Created Successfully!")

# ---------------- READ FILE ---------------- #

elif choice == "Read File":

    st.header("Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():

            with open(file_name, 'r') as file:
                st.text(file.read())

        else:
            st.error("File Not Found!")

# ---------------- UPDATE FILE ---------------- #

elif choice == "Update File":

    st.header("Update File")

    file_name = st.text_input("Enter file name")

    update_type = st.radio(
        "Choose Update Type",
        ["Overwrite", "Append"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            mode = 'w' if update_type == "Overwrite" else 'a'

            with open(file_name, mode) as file:
                file.write(content)

            st.success("File Updated Successfully!")

        else:
            st.error("File Not Found!")

# ---------------- DELETE FILE ---------------- #

elif choice == "Delete File":

    st.header("Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():

            os.remove(p)

            st.success("File Deleted Successfully!")

        else:
            st.error("File Not Found!")

# ---------------- RENAME FILE ---------------- #

elif choice == "Rename File":

    st.header("Rename File")

    old_name = st.text_input("Enter old file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(old_name)

        if p.exists():

            p.rename(new_name)

            st.success("File Renamed Successfully!")

        else:
            st.error("File Not Found!")

# ---------------- CREATE FOLDER ---------------- #

elif choice == "Create Folder":

    st.header("Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("Folder already exists!")

        else:
            p.mkdir()

            st.success("Folder Created Successfully!")

# ---------------- DELETE FOLDER ---------------- #

elif choice == "Delete Folder":

    st.header("Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            p.rmdir()

            st.success("Folder Deleted Successfully!")

        else:
            st.error("Folder Not Found!")