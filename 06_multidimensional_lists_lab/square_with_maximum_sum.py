import sys
from io import StringIO

input1 = """3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0"""

sys.stdin = StringIO(input1)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    # n,m = map(int, input().split(', ')

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return(matrix)


matrix = read_matrix()


def get_sum_of_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix(matrix,sub_matrix_size):

    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_of_submatrix(matrix, 0, 0, sub_matrix_size)

    for row_index in range(len(matrix) - sub_matrix_size + 1):
        for column_index in range(len(matrix[row_index]) - sub_matrix_size + 1):
            current_sum = get_sum_of_submatrix(
                matrix, row_index, column_index, sub_matrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = column_index

    return(best_row_index,best_column_index)


def print_result(coordinates,size):
    (row_index,col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix,row_index,col_index,size))


sub_matrix_size = 2
print_result(get_best_submatrix(matrix,sub_matrix_size), sub_matrix_size)


# sums = []
# n = len(matrix)
# m = len(matrix[0])

# for r in range(n - 1):
#     for c in range(m - 1):
#         current_sum = matrix[r][c] +\
#             matrix[r][c + 1] +\
#             matrix[r + 1][c] +\
#             matrix[r + 1][c + 1]
#         sums.append((
#             current_sum,
#             r,
#             c,
#         ))
# print(sums)
