#!/usr/bin/python3

from partOne import list_files
from partTwo import unmatch_finder
from new_folder import new_directory_creation

def sql_lines(path):
    line1 = "DELETE FROM `wp_postmeta` WHERE `post_id` = (SELECT `ID` FROM `wp_posts` WHERE `guid` = \"{}\");\n".format(path)
    line2 = "DELETE FROM `wp_posts` WHERE `guid` = \"{}\";\n".format(path)
    return line1, line2


unmatched_list = unmatch_finder(list_files("uploads"), "./used_images.txt")
print("Path exemple : https://yourdomain.com/wp-content/")
started_path = input("Please, enter the path (see exemple above) : ")

print("STEP 3")
print("SQL file creation ...")

with open("script.sql", "w", encoding="utf-8") as sql_file:

    for file_path in unmatched_list:
        full_path = started_path + file_path
        line_one, line_two = sql_lines(full_path)
        sql_file.write(line_one)
        sql_file.write(line_two)
    
print("\nDone.\nYou can find script.sql\n")
print("STEP 4\n")
new_directory_creation()
print("\nYou can find your new directory name : new_uploads")