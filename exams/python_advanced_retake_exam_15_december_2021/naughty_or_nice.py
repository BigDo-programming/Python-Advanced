def temp_numbers(temp_dict):
    temp = []
    for k in temp_dict.values():
        temp.extend(k)
    return temp


def naughty_or_nice_list(kids: list, *args, **kwargs):
    santa_claus_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": [],
    }
    temp_dict = {}

    for i in args:
        number, status = i.split("-")
        if status not in temp_dict:
            temp_dict[status] = []
        temp_dict[status] += [int(number)]

    temp = temp_numbers(temp_dict, )
    print(temp)
    for j in kids:
        kids_numbers = j[0]
        name = j[1]
        for key, value in temp_dict.items():

            if kids_numbers in value:
                santa_claus_dict[key] += [name]
        if kids_numbers not in temp:
            santa_claus_dict["Not found"].append(name)

    print(santa_claus_dict)

    #         if number in kids_numbers:
    #             santa_claus_dict[status] += [name]
    #         else:
    #             not_found.add(name)
    #
    # for name in santa_claus_dict.values():
    #     print(name)
    # #     not_found.(name)
    # # print(not_found)
    #
    #
    # for kid_name, status in kwargs.items():
    #     for key, value in santa_claus_dict.items():
    #         if kid_name in value:
    #             santa_claus_dict[key].remove(kid_name)
    #             santa_claus_dict[status] += [kid_name]
    #
    # print(santa_claus_dict)
    # # print(not_found)

#
# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
# def naughty_or_nice_list(kids: list, *args, **kwargs):
#     santa_claus_dict = {
#         "Nice": [],
#         "Naughty": [],
#         "Not found": [],
#     }
#     not_found = set()
#
#     for i in args:
#         number, status = i.split("-")
#         for j in kids:
#             kids_numbers = str(j[0])
#             name = j[1]
#
#             if number in kids_numbers:
#                 santa_claus_dict[status] += [name]
#             else:
#                 not_found.add(name)
#     for kid_name, status in kwargs.items():
#         for key, value in santa_claus_dict.items():
#             if kid_name in value:
#                 santa_claus_dict[key].remove(kid_name)
#                 santa_claus_dict[status] += [kid_name]
#
#     print(santa_claus_dict)
