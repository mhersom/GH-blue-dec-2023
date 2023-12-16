"""
Friday Course Work
"""

#Intro to Exceptions
#syntax error and value error are exceptions. 
#Exception is an event whic occurs during the execution of a program that disrupts the normal flow of the program instructions.
#raises exception and stops program

#helps handle exceptions
try:    
    value = int(input('Enter an integer: '))  #Code that could raise exception
    print('The inverse of', value, 'is', 1/value)
except: 
    print('You did not provide a number, so I will not calculate the inverse') #code that handles the exception
    
#what about when a zero is provided? Zero division error
try:    
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError: 
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible. Sorry.')
    
#helping to cover other exceptions
try: 
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1/value)
except ValueError: 
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible. Sorry.')
except:
    print('Something strange happened here, sorry.')
    
#exception hirearchy
#base exceptions (top level))
#exception - system exist - keyboard interrupt - next level
#under exceptions -> arithmetic error - lookup error - type error - value error
#under arthimetic - zero division error
#under lookcup -> index error and key error (lists or dictionaries)


#SystemExit
import sys

user_name = input("What is your name? ")
if user_name == '':
    print('Empty name? I cannot work with that. I am closing the program. Bye!')
    sys.exit()
print('Hello', user_name)
print('Let us get started...')

#keyboard interrupt - user inputs something to intterup system
#can press the interrupt kernal button to stop

#index error
#programming _languages = ['Java', 'Python', 'C++']
#print(programming_languages[10])
#index error since there aren't 10 elements

#key error
#ages = {'Jim': 30, 'Pam': 28, 'Kevin':33}
#ages['Michael']
#would generate key error since Michael isn't in dictionary

#type error
#age = input('What is your age? ')
#print('In 10 years, you will be', age + 10)
#input generates string, so calc wouldn't work, needs to be integer.

#value error
#age = (int(input('What is your age? '))
#iff someone puts something in that isn't a number (ex: a)

#propogating exceptions
def get_day(user_info):
    day = int(input('What is the day of your birthday? '))
    user_info.append(day)
    
def get_month(user_info):
    month = int(input('What is the month of your birthday? '))
    user_info.append(month)
    
def get_year(user_info):
    year = int(input('What is the year of your birthday? '))
    user_info.append(year)

def get_user_bday(user_info):
        try:   #this applies to the above sections when gathering inputs because exceptions are propgated through functions
            get_day(user_info)
            get_month(user_info)
            get_year(user_info)
            print('So your birthday is', user_info)
        except ValueError:
            print('You entered incorrect data. Bye!')

print('Hi, I will collect some info about your birthday!')
user_info = []
get_user_bday(user_info)

#assertion exceptions
#assertions are assumptions in our program that should always be true

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number!'
    return 1/number
calculate_inverse(5)
#assertion error would generate if used 0

#use assersions when:
#1. for debugging/testing code
#2. for documenting your code

#do not use assertions when:
#1. validate user input with assertions
#2. handle assertion errors in try...except
    
    
    
    
    
    
    