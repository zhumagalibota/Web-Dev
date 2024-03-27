#1
def hello_name(name):
    return "Hello " + name + "!"

print(hello_name('Bob'))    
print(hello_name('Alice'))  
print(hello_name('X'))      

#2
def make_out_word(out, word):
    return out[:2] + word + out[2:]

print(make_out_word('<<>>', 'Yay'))     
print(make_out_word('<<>>', 'WooHoo')) 
print(make_out_word('[[]]', 'word'))   

#3
def first_half(str):
    return str[:len(str)//2]

print(first_half('WooHoo'))     
print(first_half('HelloThere')) 
print(first_half('abcdef'))     

#4
def non_start(a, b):
    return a[1:] + b[1:]

print(non_start('Hello', 'There'))  
print(non_start('java', 'code'))    
print(non_start('shotl', 'java'))   

#5
def make_abba(a, b):
    return a + b + b + a

print(make_abba('Hi', 'Bye'))      
print(make_abba('Yo', 'Alice'))    
print(make_abba('What', 'Up'))     

#6
def extra_end(str):
    return str[-2:] * 3

print(extra_end('Hello'))  
print(extra_end('ab'))     
print(extra_end('Hi'))     

#7
def without_end(str):
    return str[1:-1]

print(without_end('Hello'))  
print(without_end('java'))   
print(without_end('coding')) 

#8
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags('i', 'Yay'))     
print(make_tags('i', 'Hello'))   
print(make_tags('cite', 'Yay'))  

#9
def first_two(str):
    return str[:2]

print(first_two('Hello'))     
print(first_two('abcdefg'))   
print(first_two('ab'))        

#10
def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

print(combo_string('Hello', 'hi'))     
print(combo_string('hi', 'Hello'))     
print(combo_string('aaa', 'b'))        
