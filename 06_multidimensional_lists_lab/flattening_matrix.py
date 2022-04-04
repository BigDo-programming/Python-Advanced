import sys
from io import StringIO

input1 = """2
1, 2, 3
4, 5, 6"""

sys.stdin = StringIO(input1)


# Прост мой вариянт на задачата!
# my_list = []
# n = int(input())
# for _ in range(n):
#     numbers = input().split(', ')
#     for i in numbers:
#         my_list.append(int(i))
    
# print(my_list)

def read_matrix():
    n = int(input())
    
    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ') ]
        matrix.append(row)

    return(matrix)

matrix = read_matrix()
print(
    [x for row in matrix for x in row] # matrix comprehension - трябва да го схвана!!!
)