# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0. Before you print the result, replace  with "@" and reverse the order of the words.

# def replace_ch(text):
#     symbols = ["-", ",", ".", "!", "?"]
#
#     for symbol in symbols:
#         text = text.replace(symbol, "@")
#
#     return text.strip()
#
#
# with open("text.txt") as file:
#     index = 0
#     while True:
#         line = file.readline()
#
#         if not line:
#             break
#
#         if index % 2 == 0:
#             line = (replace_ch(line))
#             print(" ".join(line.split()[::-1]))
#
#         index += 1



def replace_ch(text):
    symbols = ["-", ",", ".", "!", "?"]

    for symbol in symbols:
        text = text.replace(symbol, "@")

    return text.strip()

with open("text.txt") as file:

    for i, char in enumerate(file):
        if i % 2 == 0:
            string = replace_ch(char)
            print(' '.join(string.split()[::-1]))