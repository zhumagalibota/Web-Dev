#A
a = int(input())
b = int(input())

max_number = max(a, b)

print(max_number)

#B
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

# C
test_answer = int(input())
student_answer = int(input())

if student_answer == 1:
    if test_answer == 1:
        print("YES")
    else:
        print("NO")
else:
    if test_answer == 1:
        print("NO")
    else:
        print("YES")

#D
x = int(input())

if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)


#E
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(1)
elif num1 < num2:
    print(2)
else:
    print(0)

