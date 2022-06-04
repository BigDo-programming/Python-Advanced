# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
with open("text.txt") as file:
    index = 0
    while True:
        line = file.readline()

        if not line:
            break

        if index % 2 == 0:
            print(line)

        index += 1
