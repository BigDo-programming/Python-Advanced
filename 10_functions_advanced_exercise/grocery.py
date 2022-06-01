def grocery_store(**kwargs):
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x)):
        result.append(f"{key}: {value}")

    return '\n'.join([str(x) for x in result])


# def grocery_store(**kwargs):
#     return '\n'.join([f"{key}: {value}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x))])

print(grocery_store(
    pread=12,
    basta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))



