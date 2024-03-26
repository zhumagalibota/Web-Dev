#A
a = 2
b = 5

for num in range(a, b + 1):
    if num % 2 == 0:
        print(num, end=" ")

#B
a, b, c, d = 2, 5, 0, 2

for num in range(a, b + 1):
    if num % d == c:
        print(num, end=" ")

#C
a, b = 2, 8

for num in range(a, b + 1):
    if int(num ** 0.5) ** 2 == num:
        print(num, end=" ")

#D
x = int(input())
d = int(input())

x_str = str(x)

count = 0

for digit in x_str:
    if int(digit) == d:
        count += 1

print(count)

#E
x = int(input())

x_str = str(x)

sum_digits = 0

for digit in x_str:
    sum_digits += int(digit)
print(sum_digits)

#F
x = input()

reversed_number = ''

for digit in x:
    reversed_number = digit + reversed_number
print(int(reversed_number))

#G
x = int(input())

for divisor in range(2, x + 1):
    if x % divisor == 0:
        print(divisor)
        break

#H
x = 32
for divisor in range(1, x + 1):
    if x % divisor == 0:
        print(divisor)

#I
x = 32
count = 0
for divisor in range(1, int(x ** 0.5) + 1):
    if x % divisor == 0:
        count += 1
        if divisor != x // divisor:
            count += 1
print(count)

#J
total_sum = 0

for _ in range(100):
    num = int(input())
    total_sum += num
print(total_sum)


#K
N = int(input())

total_sum = 0
for _ in range(N):
    num = int(input())
    total_sum += num
print(total_sum)

#L
binary_number = input()

decimal_number = int(binary_number, 2)
print(decimal_number)

#M
N = int(input())

zeros_count = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        zeros_count += 1
print(zeros_count)
