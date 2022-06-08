# Write a program that reads a text file, inserts line numbers in front of each line,
# and counts all the letters and punctuation marks. The result should be written to another text file.
#
#
# def count(text):
#     punctuation_marks = {"-", ",", ".", "!", "?", "'", ":", ";", "_", "-", '"', "..."}
#     count_ch = 0
#     count_symbol = 0
#
#     for word in text.split():
#         count_ch += len(word)
#
#         for ch in word:
#             if ch in punctuation_marks:
#                 count_symbol += 1
#
#     return f"{text} ({count_ch - count_symbol})({count_symbol})"
#
#
# with open("text.txt") as file, open("output.txt", "w") as result:
#     index = 1
#
#     while True:
#         line = file.readline().strip()
#
#         if not line:
#             break
#
#         line = count(line)
#
#         data = f"Line {index}: {line}"
#         result.write(data)
#         result.write("\n")
#
#         index += 1
from string import punctuation


def count(text):
    punctuation_marks = set(list(punctuation))
    count_ch = 0
    count_symbol = 0

    for ch in text:
        if ch.isalpha():
            count_ch += 1
        elif ch in punctuation_marks:
            count_symbol += 1

    return f"{text} ({count_ch})({count_symbol})"


with open('text.txt') as file, open('output.txt','w') as output_file:
    for index, line in enumerate(file):
        line = count(line.strip())
        output_file.write(f"Line {index + 1}: {line}")
        output_file.write("\n")
