#project -CRUD operations


from pathlib import Path
import os  #operating system
def readfileandfolder():
    try:
        p = Path('')
        items = list(p.rglob('*'))
        for index , item in enumerate(items):
            print(f'{index+1} - {item}')
    except Exception as e :
        print(e)




def create_file():
    readfileandfolder()
    try:
        #d:\file handling(project 1 )cc\main.py"
        file_name = input('Enter name on your file: ')
        p = Path (file_name)
        if p.exists():
            print('FILE ALREADY EXISTS')
        else:
            with open(file_name,'w') as file:
                content = input('Enter your file content: ')
                file.write(content)
                print('FILE ADDED!')
    except Exception as e:
        print(e)




def read_file():
    try:
        readfileandfolder()
        file_name = input('Enter name of your file: ')
        p = Path (file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print('FILE NOT FOUND!')
    except Exception as e:
        print(e)




def update_file():
    try:
        readfileandfolder()
        file_name = input('Enter name of your file: ')
        p = Path(file_name)
        if p.exists():
            print('Press 1 to overwrite the content')
            print('Press 2 to append new content')

            option = int(input('Enter your choice for updating a file: '))
            if option == 1:
                with open (file_name,'w') as file:
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED...')

            elif option == 2:
                with open (file_name,'a') as file:
                    content = input('Enter your content: ')
                    file.write(content)
                    print('CONTENT CHANGED...')
            else:
                print("INVALID INPUT")
        else:
            print("FILE DOES NOT EXISTS!")
    except Exception as e:
        print(e)




def delete_file():
    readfileandfolder()
    file_name = input('Enter name of your file: ')
    p = Path(file_name)
    if p.exists():
        os.remove(p)  #OS is removing path of that file completely from the system.
        print("FILE DELETED")
    else:
        print("FILE DOES NOT EXISTS!!")




def rename_file():
    readfileandfolder()
    file_name = input('Enter name of your file:')
    p = Path (file_name)
    if p.exists():
        new_file = input('Enter new name of your file:')
        p.rename(new_file)
        print('FILE RENAMED!')
    else: 
        print('FILE NOT FOUND!')




def create_folder():
    readfileandfolder()
    folder_name = input('Enter name of your folder:')
    p = Path(folder_name)
    if p.exists():
        print('FOLDER ALREADY EXISTS!')
    else:
        p.mkdir()  #mkdir = Make a new folder.
        print('FOLDER CREATED!')





def delete_folder():
    readfileandfolder()
    folder_name = input('Enter name of your folder:')
    p = Path(folder_name)
    if p.exists():
        p.rmdir()   #rmdir = deleted a folder
        print('FOLDER DELETED!')
    else:
        p.mkdir()   
        print('FOLDER NOT FOUND!')










def create_file_in_folder():
    readfileandfolder
    folder_name = input('Enter name of your folder:')
    file_name = input('Enter name of your file:')
    p = Path(file_name)
    if p.exists():
        print('FILE ALREADY EXISTS!')
    else:
        pass









while True:
    print("press 1 for create file")
    print("press 2 for reading file")
    print("press 3 for updating file")
    print("press 4 for deleting file")
    print("press 5 for renaming a file")
    print("press 6 for creating a folder")
    print("press 7 for deleting a folder")
    print("press 8 for create file in folder")
    print("Press 0 for existing....")
    

    option = int(input("Enter your choice:- "))
    if option == 1:
        create_file()

    if option == 2:
        read_file()

    if option == 3:
        update_file()

    if option == 4:
        delete_file()
    
    if option == 5:
        rename_file()
    
    if option == 6:
        create_folder()
    
    if option == 7:
        delete_folder()

    if option == 8:
        create_file_in_folder()

    if option == 0:
        break

    
