def shopping_list(budget, **kwargs):
    data = ""
    count = 0
    if budget >= 100:
        for key, value in kwargs.items():
            if count == 5:
                break
            price = value[0] * value[1]

            if budget >= price and budget > 0:
                budget -= price
                count += 1

                data += f"You bought {key} for {price:.2f} leva." + "\n"
    else:
        data = "You do not have enough budget."

    return data.strip()

# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
