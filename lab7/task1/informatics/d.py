#A
N = int(input())

i = 1
while i ** 2 <= N:
    print(i ** 2)
    i += 1

#B
n = int(input())

divisor = 2
while n % divisor != 0:
    divisor += 1
print(divisor)

#C
N = int(input())

power_of_two = 1
while power_of_two <= N:
    print(power_of_two, end=' ')
    power_of_two *= 2

#D
N = int(input())

power_of_two = 1

while power_of_two < N:
    power_of_two *= 2

if power_of_two == N:
    print("YES")
else:
    print("NO")

#E
N = int(input())

k = 0

power_of_two = 1

while power_of_two < N:
    power_of_two *= 2
    k += 1
print(k)
