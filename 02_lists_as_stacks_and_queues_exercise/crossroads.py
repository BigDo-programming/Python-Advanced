import sys
from io import StringIO

input1 = """10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END"""

input2 = """9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END"""

# sys.stdin = StringIO(input1)
sys.stdin = StringIO(input2)

from collections import deque

cars = deque()
green_light = int(input())
free_window = int(input())

passed_cars = 0
crash_happened = False

while not crash_happened:
    line = input()
    if line == "END":
        break
    if line == "green":
        current_green_light = green_light
        while cars and current_green_light > 0:
            car = cars.popleft()
            if current_green_light >= len(car) or current_green_light + free_window >= len(car):
                passed_cars += 1
                current_green_light -= len(car)
            else:
                print("A crash happened!")
                print(f"{car} was hit at {car[current_green_light+free_window]}.")
                crash_happened = True
                break
    else:
        cars.append(line)
if not crash_happened:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")

# ToDo - da q resha sam