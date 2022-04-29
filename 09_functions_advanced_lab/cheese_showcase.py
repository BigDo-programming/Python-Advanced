def sorting_cheeses(**kwargs):
    cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for key, value in cheeses:
        result += key + '\n'
        sorted_value = sorted(value, reverse=True)
        result += '\n'.join([str(x) for x in sorted_value])
        result += '\n'
    result = result.strip()
    return result


# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
