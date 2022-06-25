def naughty_or_nice_list(kids, *args, **kwargs):
    nice = []
    naughty = []
    for command in args:
        num, status = command.split('-')
        num = int(num)
        name = None
        is_unique = False
        for kids_number, kids_name in kids:
            if num == kids_number and is_unique:
                is_unique = False
                break
            if num == kids_number:
                is_unique = True
                name = kids_name
        if is_unique:
            kids.remove((num, name))
            if status == 'Nice':
                nice.append(name)
            else:
                naughty.append(name)
    for kid_name, status in kwargs.items():
        is_unique = False
        number = None
        for kids_number, kids_name in kids:
            if kid_name == kids_name and is_unique:
                is_unique = False
                break

            if kid_name == kids_name:
                is_unique = True
                number = kids_number

        if is_unique:
            kids.remove((number, kid_name))
            if status == 'Nice':
                nice.append(kid_name)
            else:
                naughty.append(kid_name)
    not_found = [x for _, x in kids]
    result = ''
    if nice:
        result += f"Nice: {', '.join([str(x) for x in nice])}\n"
    if naughty:
        result += f"Naughty: {', '.join([str(x) for x in naughty])}\n"
    if not_found:
        result += f"Not found: {', '.join([str(x) for x in not_found])}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
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
# print(naughty_or_nice_list(
#     [
#
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
#
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))

