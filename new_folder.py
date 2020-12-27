from os import walk, mkdir, path
from shutil import copyfile

keep_images = []
def create_folder(name):
    if path.isdir(name):
        print("This directory already exist.")
        return
    else:
        mkdir(name)
        print(name + " directory created.")

def seperate_path(path):
    my_string = str(path)
    total_path = ""
    while my_string.find("/") != -1:
        i = my_string.find("/")
        total_path += my_string[:i+1]
        my_string = my_string[i+1:]
        create_folder(total_path)

    create_folder(total_path+my_string)

def new_directory_creation():
    with open("used_images.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            keep_images.append(line)

    print("New folder creation ...")

    create_folder("new_uploads")
    tempor = []

    for root, dirs, files in walk("uploads"):
        root = root.replace("\\", "/")
        if len(files) > 0:
            actual_dir = root.replace("uploads/", "")
            for file in files:
                test = file.find(".")
                extension = file[test:]
                tempor.append(file[:test])
                matching = [s for s in tempor if file[:test] in s]

                file_with_path = root + "/" + file
                
                if file_with_path in keep_images:
                           
                    seperate_path(root.replace("uploads/", "new_uploads/"))
                    for match in matching:
                        origin_file = root + "/" + match + extension
                        dest_file = "new_uploads/" + actual_dir + "/" + match + extension
                        copyfile(origin_file, dest_file)
                        print(actual_dir + "/" + match + extension + " file created.")