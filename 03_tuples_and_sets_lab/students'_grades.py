import sys
from io import StringIO

input1 = """7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00"""

sys.stdin = StringIO(input1)

students_grades = {}

n = int(input())
for _ in range(n):
    name, grade = input().split()
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name] += [float(grade)]


for name, grade in students_grades.items():
    print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in grade)} (avg: {sum(grade) / len(grade):.02f})")




# students_grades = {}
# n = int(input())
# for i in range(n):
#     name, grade = input().split()
#     if name not in students_grades:
#         students_grades[name] = []
#     students_grades[name].append(float(grade))
#
# for name, grade in students_grades.items():
#     print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in grade)} (avg: {sum(grade) / len(grade):.02f})")

# def avg(values):
#     return sum(values) / len(values)
#
# n = int(input())
#
# students_records = {}
#
# for _ in range(n):
#     name, grade_string = input().split()
#     grade = float(grade_string)
#
#     if name not in students_records:
#         students_records[name] = []
#     students_records[name].append(grade)
#
# for name, grades in students_records.items():
#     average_grade = avg(grades)
#     grades_string = ' '.join(str(f'{x:.2f}') for x in grades)
#     print(f'{name} -> {grades_string} (avg: {average_grade:.2f})')
