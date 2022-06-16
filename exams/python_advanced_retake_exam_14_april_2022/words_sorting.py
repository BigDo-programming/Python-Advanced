def words_sorting(*args):
    my_dict = {}
    for word in args:
        value = 0
        for i in word:
            value += ord(i)

        my_dict[word] = value
    my_sum = sum(my_dict.values())
    result = []
    if my_sum % 2 == 0:
        for words, score in sorted(my_dict.items(), key=lambda a: a[0]):
            result.append(f"{words} - {score}")
    else:
        for words, score in sorted(my_dict.items(), key=lambda a: -a[1]):
            result.append(f"{words} - {score}")

    # sorted(my_dict.items(), key=lambda a: a[0]) if my_sum % 2 == 0 else sorted(my_dict.items(),key=lambda a: -a[1])
    return '\n'.join(result)

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
