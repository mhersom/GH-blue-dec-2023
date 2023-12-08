"""
Thursday Coursework - 12/7
"""

#Practicing If Statements, indent with 4 spaces
#user_age = int(input(‘What is your age? ‘))
#if user_age > 30: 
#    print (‘You are over 30 years old’)
#    print (‘Sorry, you do not qualify’)
#if user_age == 30: 
#    print (‘You are exactly 30 years old’)
#    print (‘You will need to meet additional conditions to qualify’)
#else:
#    print (‘You are 30 years old or younger’)
#    print (‘Congratulations, you qualify!’)

#Practicing Logical Operators and Conditions
#Password = input(‘Do you know the secret password? ‘)
#If password !=  ‘--secret’:
#    print(‘not correct’)
#Else: 
#    Print(‘correct password’)
#
#if True:
#    print(‘Condition met’)
#if False:
#    print (‘Condition met’)
#
#if 2 == 2:
#    print(‘true’)
#
#if 1 == 2:
#   print(‘true’)
#
#if 2 == 2.0:
#    print(‘true’)

#joining multiple conditions (and,  nor, not)
#Priorities: not, and, or
#User_age = int(input(‘What is your age? ‘)
#User_country = input(‘What is your country? ‘)
#If user_age <25 and user_country == ‘Germany’:
#    Print(‘You can apply for a German student exchange program’)
#Else:
#    Print(‘Sorry, you do not qualify’)
#
#User_country = input(‘What is your country?’)
#If user_country == ‘Sweden’ or user_country == ‘Denmark’ or user_country – ‘Norway’:
#    Print(‘You can apply for a Scandinavian student exchange program’)
#Else: 
#    Print(‘Sorry, you do not qualify’)
#
#User_country = input(‘Where do you come from? ‘)
#If not user_country == ‘Germany’:
#    Print (‘you are not from Germany!’)
#Else: 
#    Print(‘You are from Germany’)

#user_age = int(input(‘What is your age?’)
#User_country = input(‘What is your country?’)
#If not user_country == ‘Germay’ and user_age < 25 or \
#user_country == ‘Germany’ and user_age < 23:
#    Print(‘You qualify!’)
#Else: 
#    Print(‘You don\’t qualify!’)

#Nest If
#Answer_a = input(‘Do you like traveling? y/n: ‘)
#If answer answer_a == ‘y’:
#    Print(‘Good!’)
#Else:
#    Print(‘Sorry to hear that!’)

#Answer_a = input(‘Do you like traveling? y/n: ‘)
#If answer answer_a == ‘y’:
#    Answer_b = input(‘Do you like Asia? y/n: ‘)
#    if answer_b == ‘y’:
#        Print(‘Excellent! You can win a ticket to Thailand!’)
#    Else:
#        Print(‘Sorry to hear that!’)
#Else:
#    Print(‘Sorry to hear that!’)

#Coding Exercise
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
	 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
    print('You can get a refund.')
else:
    print('You cannot get a refund.')

