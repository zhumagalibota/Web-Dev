#1
def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - (big * 5) <= small

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))

#2
def no_teen_sum(a, b, c):
    def fix_teen(n):
        if n in [13, 14, 17, 18, 19]:
            return 0
        return n

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

#3
def make_chocolate(small, big, goal):
    big_needed = goal // 5

    if big_needed <= big:
        remaining_small_needed = goal - (big_needed * 5)
        if small >= remaining_small_needed:
            return remaining_small_needed
    return -1

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))


#4
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    return a + b + c

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))


#5
def round_sum(a, b, c):
    def round10(num):
        return (num + 5) // 10 * 10

    return round10(a) + round10(b) + round10(c)

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))

#6
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    return a + b + c

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))

#7
def close_far(a, b, c):
    if abs(a - b) <= 1:
        return abs(a - c) >= 2 and abs(b - c) >= 2
    elif abs(a - c) <= 1:
        return abs(a - b) >= 2 and abs(c - b) >= 2
    return False

print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
