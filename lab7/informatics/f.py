#A
def min(a, b, c, d):
    min_val = a
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    if d < min_val:
        min_val = d
    return min_val

a, b, c, d = map(int, input().split())
print(min(a, b, c, d))

#B
def power(a, n):
    return a ** n

a, n = map(float, input().split())
print(power(a, int(n)))

#C
def xor(x, y):
    return (x and not y) or (not x and y)

x, y = map(int, input().split())
print(int(xor(x, y)))


