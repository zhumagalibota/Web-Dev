#1
def sleep_in(weekday, vacation):
    return not weekday or vacation

print(sleep_in(False, False)) 
print(sleep_in(True, False))   
print(sleep_in(False, True))  

#2
def diff21(n):
    diff = abs(n - 21)
    if n > 21:
        return diff * 2
    else:
        return diff

print(diff21(19)) 
print(diff21(10))  
print(diff21(21))  

#3
def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

print(near_hundred(93)) 
print(near_hundred(90))  
print(near_hundred(89)) 

#4
def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

print(near_hundred(93))  
print(near_hundred(90))  
print(near_hundred(89))  

#5
def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)

print(monkey_trouble(True, True))   
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))  

#6
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6)) 
print(parrot_trouble(True, 7)) 
print(parrot_trouble(False, 6)) 

#7
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)

print(pos_neg(1, -1, False)) 
print(pos_neg(-1, 1, False)) 
print(pos_neg(-4, -5, True))

#8
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

print(front_back('code'))
print(front_back('a'))   
print(front_back('ab'))  

#9
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2)) 

#10
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

print(makes10(9, 10)) 
print(makes10(9, 9))  
print(makes10(1, 9))  

#11
def not_string(s):
    if s.startswith("not"):
        return s
    else:
        return "not " + s

print(not_string('candy')) 
print(not_string('x'))     
print(not_string('not bad')) 

#12
def front3(str):
    front = str[:3]
    return front * 3

print(front3('Java'))       
print(front3('Chocolate')) 
print(front3('abc'))       
