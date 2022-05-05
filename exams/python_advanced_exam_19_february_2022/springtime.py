def start_spring(**kwargs):
    data = ''
    my_dict = {}
    for key, value in kwargs.items():
        if value not in my_dict:
            my_dict[value] = []
        my_dict[value] += [key]
    # my_dict_ = dict(sorted(my_dict.items(), key=lambda kv: (kv[0],kv[1])))
    my_dict = dict(sorted(my_dict.items(), key=lambda kv: (-len(kv[1]), kv[0])))
    # sorted(my_dict.items(),key=lambda x: len(x))
    for key, value in my_dict.items():

        data += f"{key}:" + "\n"
        for i in sorted(value):
            data += f"-{i}" + "\n"
    return data.strip()



# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
#
# print(start_spring(**example_objects))
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))

# The collections sorted by their number of elements in descending order.
# o If two or more collections have the same number of elements in them, return them in ascending order (alphabetically) by the type's name.
