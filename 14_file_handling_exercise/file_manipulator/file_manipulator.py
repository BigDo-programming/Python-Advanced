# Create a program that will receive commands until the command "End". The commands can be:
# 1."Create-{file_name}" - Creates the given file with an empty content. If the file already exists,
# remove the existing text in it (as if the file is created again)
# 2."Add-{file_name}-{content}" - Append the content and a new line after it.
# If the file does not exist, create it, and add the content
# 3."Replace-{file_name}-{old_string}-{new_string}" -
# Open the file and replace all the occurrences of the old string with the new string.
# If the file does not exist, print: "An error occurred"
# 4."Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

import sys
from io import StringIO
import os
from os import path

input1 = """Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End"""

input2 = """Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
End"""

input3 = """Delete-random.txt
Delete-file.txt
End"""


# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
# sys.stdin = StringIO(input3)


def create_file(name):
    with open(name, "w") as c_file:
        return c_file


def add_content(name, string):
    with open(name, "a") as a_file:
        a_file.write(string)
        a_file.write("\n")
        return a_file


def replace_content(name, old_string, new_string):
    with open(name, "r") as r_file:
        content = r_file.read().replace(old_string, new_string)
    with open(name, "w") as w_file:
        w_file.write(content)


def delete_file(name):
    os.remove(name)


while True:
    command = input()
    if command == "End":
        break

    command_split = command.split("-")
    action = command_split[0]
    file_name = command_split[1]

    if action == "Create":
        create_file(file_name)

    elif action == "Add":
        text = command_split[2]
        add_content(file_name, text)

    elif action == "Replace":
        old_text = command_split[2]
        new_text = command_split[3]

        if path.exists(file_name):
            replace_content(file_name, old_text, new_text)

        else:
            print("An error occurred")

    elif action == "Delete":
        if path.exists(file_name):
            delete_file(file_name)

        else:
            print("An error occurred")

# while True:
#     command = input()
#     if command == "End":
#         break
#
#     command_split = command.split("-")
#     action = command_split[0]
#     file_name = command_split[1]
#
#     if action == "Create":
#         open(file_name, "w").close()
#
#     elif action == "Add":
#
#         text = command_split[2]
#         with open(file_name, "a") as a_file:
#             a_file.write(text)
#             a_file.write("\n")
#
#     elif action == "Replace":
#
#         old_text = command_split[2]
#         new_text = command_split[3]
#         if path.exists(file_name):
#
#             with open(file_name, "r+") as r_file:
#                 content = r_file.read().replace(old_text, new_text)
#                 r_file.seek(0)
#                 r_file.truncate()
#                 r_file.write(content)
#
#
#         else:
#             print("An error occurred")
#
#     elif action == "Delete":
#         if path.exists(file_name):
#             os.remove(file_name)
#         else:
#             print("An error occurred")
