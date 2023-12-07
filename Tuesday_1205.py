"""
Tuesday 12 05 Coursework
"""

#Practicing Variables -must start with letter, uppercase/lowercase matter, cannot use from or global
greeting = 'Hello, friend!'
print (greeting)

greeting = 'Hi, everybody!'
print (greeting)

#Practicing Data Types: 'String',  Integer, floats are numbers with decimal, boolean (True = 1, False = 0)
#integer
age = 35

#float
speed1 = 4.5
speed2= 4.0
speed3= 4.

#boolaean is true or false (need capital letter)
am_i_ugly = True
am_i_ugly = False

#Numerical Representations 
#Underscores do not change numbers, but make it easier to read
#12052023 = 12_05_2023

#Scientific notations with floats
#3e-4 for small numbers, or 3e4 for big numbers

#Octal numbers start with 0o or 0O
print (0o123)

#hexadecimal numbers start with 0x or 0X
print (0x123)

#Operators
2 + 3
5 - 4
3 * 5

#standard divison, always float number
6 / 2
7 /2 

#integer divison, provides nearest lowest whole number
6 // 2 
7 // 2

#modulus divison, returns remaining left over after division
6 % 2
7 % 2

#power operator
2 ** 3

#Coding Exercise
income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
print ('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowntaxland!')
