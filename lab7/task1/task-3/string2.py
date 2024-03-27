#1
def double_char(string):
    result = ''
    for char in string:
        result += char * 2
    return result

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))

#2
def count_code(string):
    count = 0
    for i in range(len(string) - 3):
        if string[i:i+2] == 'co' and string[i+3] == 'e':
            count += 1
    return count

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))

#3
def count_hi(string):
    return string.count('hi')

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))

#4
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

#5
def cat_dog(string):
    return string.count('cat') == string.count('dog')

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))

#6
def xyz_there(string):
    for i in range(len(string) - 2):
        if string[i:i+3] == 'xyz' and (i == 0 or string[i-1] != '.'):
            return True
    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
