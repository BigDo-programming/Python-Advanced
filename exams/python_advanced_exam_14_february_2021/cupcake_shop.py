# def stock_availability(inventory, delivery_or_sell, *args):
#     if delivery_or_sell == "delivery":
#         return inventory + list(args)
#     if not args:
#         return inventory[1:]
#
#     if isinstance(args[0], int):
#         count = args[0]
#         return inventory[count:]
#
#     sold_item = set(args)
#     return [x for x in inventory if x not in sold_item]


def stock_availability(inventory_list, delivery_or_sell, *args):

    if delivery_or_sell == "delivery":
        return inventory_list+list(args)

    if not args:
        return inventory_list[1:]

    if isinstance(args[0], int):
        return inventory_list[args[0]:]

    if isinstance(args[0], str):
        return [x for x in inventory_list if x not in args]

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

# def stock_availability(inventory: list, delivery_or_sell, *args: str):
#     if delivery_or_sell == "delivery":
#         for i in args:
#             inventory.append(i)
#         return inventory
#
#     if delivery_or_sell == "sell":
#         if len(args) > 0:
#             word = str(args[0])
#
#             if word.isalpha():
#                 while word in inventory:
#                     inventory.remove(word)
#             if word.isdigit():
#                 for k in range(int(word)):
#                     inventory.pop(0)
#         else:
#             inventory.pop(0)
#         return inventory
