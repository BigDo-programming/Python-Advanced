def operate(symbol, first_number, *args):
    if symbol == "+":
        return sum(args) + first_number
    if symbol == "-":
        result = first_number
        for i in args:
            result -= i
        return result

    if symbol == "*":
        result = first_number
        for i in args:
            result *= i
        return result
    if symbol == "/":
        result = first_number
        for i in args:
            if i != 0:
                result /= i
        return result


print(operate("*", 3, 4))
