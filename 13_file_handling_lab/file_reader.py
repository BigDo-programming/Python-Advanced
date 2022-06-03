file = open("numbers.txt")

# Variant 1
# result = 0
# for line in file:
#     result += int(line)
# print(result)

# Variant 2
print(
    sum(
        [int(line) for line in file]
    )
)
