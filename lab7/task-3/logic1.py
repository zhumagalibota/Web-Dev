#1
def cigar_party(cigars, is_weekend):
    return (cigars >= 40 and cigars <= 60) or (is_weekend and cigars >= 40)

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))

#2
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))

#3
def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))

#4
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

print(date_fashion(5, 10))
print(date_fashion(5, 2))
print(date_fashion(5, 5))

#5
def sorta_sum(a, b):
    result = a + b
    if 10 <= result <= 19:
        return 20
    return result

print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))

#6
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    return 1 <= n <= 10

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))

#7
def squirrel_play(temperature, is_summer):
    upper_limit = 90 if not is_summer else 100
    return 60 <= temperature <= upper_limit

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))

#8
def alarm_clock(day, vacation):
    if vacation:
        if day in [0, 6]:
            return 'off'
        else:
            return '10:00'
    else:
        if day in [0, 6]:
            return '10:00'
        else:
            return '7:00'

print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))

#9
def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8

print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
