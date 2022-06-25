def shopping_cart(*args):
    result = []
    my_cart = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    for group_products in args:
        if group_products == 'Stop':
            break

        else:
            group, products = group_products

        if products not in my_cart[group]:
            if group == 'Pizza' and len(my_cart['Pizza']) < 4:
                my_cart[group].append(products)

            if group == 'Soup' and len(my_cart['Soup']) < 3:
                my_cart[group].append(products)

            if group == 'Dessert' and len(my_cart['Dessert']) < 2:
                my_cart[group].append(products)

    for key, value in sorted(my_cart.items(), key=lambda a: (-len(a[1]), a[0])):

        result.append(f"{key}:")

        for j in sorted(value):
            result.append(f' - {j}')
    if len(my_cart['Pizza']) > 0 or len(my_cart['Soup']) > 0 or len(my_cart['Dessert']) > 0:
        return '\n'.join(result)
    else:
        return "No products in the cart!"



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
