def words_sorting(*args):
    sum_all_values = 0
    sorted_dict = {}
    for word in args:
        symbol_sum = 0
        for ch in word:
            symbol_sum += ord(ch)
        sorted_dict[word] = symbol_sum
        sum_all_values += symbol_sum

    if sum_all_values % 2 == 0:
        sorted(sorted_dict.items(), key=lambda item: item[1])
        data = ''
        for key, value in sorted(sorted_dict.items()):
            data += f"{key} - {value}" + '\n'

        return data.strip()

        # By keys in ascending order

    else:
        sorted(sorted_dict.items(), key=lambda item: item[1])
        data = ''
        for key, value in sorted_dict.items():
            data += f"{key} - {value}" + '\n'

        return data.strip()
        # By values in descending order

# ToDo 80/100
#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#     ))
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#     ))
