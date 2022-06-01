def age_assignment(*args, **kwargs):
    result = []
    for i in sorted(args):

        if i[0] in kwargs:
            result.append(f"{i} is {kwargs[i[0]]} years old.")

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# def age_assignment(*args, **kwargs):
#     my_dict = {}
#     for i in args:
#         if i[0] in kwargs:
#             my_dict[i] = kwargs[i[0]]
# 
#     return my_dict
