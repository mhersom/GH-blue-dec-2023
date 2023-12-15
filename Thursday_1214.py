"""
Thursday Coursework 12.14
"""

#Intro to functions

def greet ():
    print('Hello, my dear!')
    
#line 1: def = define, function needs round brackets, end line with colon
#line 2: need single indented command 

greet()

#best practice to keep all functions at top of file

#Functions with Parameters
input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

def get_average(input_numbers): #input_numbers is a parameter
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)

get_average([5.0, 3.5, 7.8, 9.9, 10.0])
#this list is called an argument

#function with 2 paramaters
def print_letter_count(text, letter): #text and letter are the parameters
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
      
print_letter_count('Welcome', 'e')

print_letter_count('People say nothing is impossible, but I do nothing every day.', 'a')

#positional parameter - the order matters
#example (letter before text)

print_letter_count('e', 'Welcome')

#named arguments aka keyword arguments, can switch order
print_letter_count(text='Welcome', letter='e')
print_letter_count(letter='e', text='Welcome')

#default parameter values
print('Hello', 'How are you?', end='.', sep='-')

def print_letter_count1(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
print_letter_count1('How many letters a are here?')

def print_letter_count2(text='This is the default string to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
    
print_letter_count2()

#remember all positional arguments must appear before any named arguments

#name scopes

def show_truth():
    mysterious_var = 'Surprise!'
    print(mysterious_var)

#or

def show_truth1():
    print(mysterious_var1)
    
mysterious_var1 = 'Surprise!'
show_truth()

#or

def show_truth2():
    mysterious_var3 = 'New Surprise!' #local variable
    print(mysterious_var1)
    
mysterious_var2 = 'Surprise!' #global variable
print(mysterious_var2)
show_truth()
print(mysterious_var2)
#shadowing = can see variable outside of function. local vs. global variables
#avoid using global variables. usually do more harm than good

# the None value
# Functions can typically: 
# 1. Cause some effect
# 2. Return a meaningful value

print_return = print('Hello world')
print(print_return)

#none is used to describe null value or no value at all, it is NOT zero, it is NOT false

x = None
if x: 
    print('None is True')
elif x is False:
    print('None is False')
else: 
    print('None is not True, or False, None is just None')

x1 = None
if x1 is None:
    print('yes')
if x1 == None:
    print('it does')

# none is a value returned implicity by functions that don't return anything meaningful

def greet():
    print('hello!)
x = greet()
print(x)

#the return keyword

def get_average(input_numbers) : 
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    
print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')

#return value gives result and immediately exits function

def get_average(input_numbers) : 
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')

    get_average([2])
    
def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
        
print(is_first_last_equal([10, 20, 30, 40, 10]))
print(is_first_last_equal([10, 20, 30, 40, 50]))

def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False
        
print(is_first_last_equal([10, 20, 30, 40, 10]))
print(is_first_last_equal([10, 20, 30, 40, 50]))
print(is_first_last_equal([]))





    









    






