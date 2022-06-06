import json
from global_constants import *


def get_all_products():
    products = []
    with open("../db/products.txt", "r") as file:
        for line in file:
            products.append(json.loads(line.strip()))
        return products
