
stack = []
n = int(input())
for i in range(n):
    data = input()
    data_split = data.split()
    action = data_split[0]
    if action == "1":
        number = int(data_split[1])
        stack.append(number)
    elif action == "2":
        if len(stack) > 0:
            stack.pop()
    elif action == "3":
        if len(stack) > 0:
            print(max(stack))
    elif action == "4":
        if len(stack) > 0:
            print(min(stack))

reversed_numbers = []

for i in range(len(stack)):
    if len(stack) > 0:
        reversed_numbers.append(str(stack.pop()))
print(", ".join(reversed_numbers))
