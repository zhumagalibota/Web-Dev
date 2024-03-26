#1 Say hello world with python
print("Hello, World!")

#2 python if-else
n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#3 arithmetic operators
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

#4 python division
a = int(input())
b = int(input())

print(a // b)
print(a / b)

#5 loops
n = int(input())

for i in range(n):
    print(i ** 2)

#6 write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))

#7 print a function
n = int(input())

for i in range(1, n + 1):
    print(i, end="")

#8 list comprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

print(coordinates)

#9 find the runner up score
n = int(input())
scores = list(map(int, input().split()))

unique_scores = sorted(set(scores), reverse=True)

runner_up_score = unique_scores[1]

print(runner_up_score)

#10 nested list
n = int(input())

students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key=lambda x: x[1])

second_lowest_grade = sorted(set(score for name, score in students))[1]

second_lowest_students = [name for name, score in students if score == second_lowest_grade]

for student in sorted(second_lowest_students):
    print(student)
