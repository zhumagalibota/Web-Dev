import math

# A
a = int(input())
b = int(input())

c = math.sqrt(a**2 + b**2)

print(c)


# B
num = int(input())

n = num + 1
p = num - 1

print("The next number for the number", num, "is", n, end=".\n")
print("The previous number for the number", num, "is", p, end=".")


# C
N = int(input())
K = int(input())

a_per_s = K // N

print(a_per_s)


# D
l = K % N

print(l)

# E 
v = int(input())
t = int(input())

s = v * t

mark = s % 109

print(mark)
