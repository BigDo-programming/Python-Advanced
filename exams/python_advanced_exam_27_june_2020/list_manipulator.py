def list_manipulator(list_, command1, command2, *args):
    if command1 == "add":
        if command2 == "beginning":
            for i in args[::-1]:
                list_.insert(0, i)
            return list_
        else:
            for i in args:
                list_.append(i)
            return list_
    if command1 == "remove":
        if command2 == "beginning":
            if args:
                n = int(*args)
                for i in range(n):
                    list_.pop(0)
                return list_
            else:
                list_.pop(0)
                return list_
        else:
            if args:
                n = int(*args)
                for i in range(n):
                    list_.pop()
                return list_
            else:
                list_.pop()
                return list_





print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
