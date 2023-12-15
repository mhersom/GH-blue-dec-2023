"""
Wednesday Coursework
"""


#Intro Tuples - similar to lists, collections of multiple elements, created with round brackets

empty_tuple = ()

one_element_tuple_a = (1,)
one_element_tuple_b = 1, 

three_elements_tuple = 1, 2, 3
print(three_elements_tuple)

#mutability
#mutable = freely updated, ex: lists
#immutable = cannot freely update, ex: tuples, strings

user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980) #replaces John

#doesn't work with tuples
# user_date.append('teacher')
# del user_data[0]
# user_data [0] = 'Mark'

message = 'welcome'
message = 'Welcome'
# message [0] = 'w'

#tuples operations

user_data = ('John', 'American', 1964)
print(len(user_data))

user_data = ('John', 'American', 1964)
if 'American' in user_data: 
    print('This person comes from the US!')

user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)
    
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

#list are typically used with many values of same data type
#example: male_name = ('Adam', 'Jerry', 'Mark')
#example: berlin_temps = [13.0, 17.5, 12.0]

#tuples are typically used with you want to group together different data types but be tied together
# example: user_data = ('John', 'American', 1964)
# example: 
# first =5
# second =7
# first, second = second, first

#Tuples in lists
city_1 = ('London', 'UK', 8.98) #tuple
city_2 = ('Canberra', 'Australia', 0.4) #tuple
city_3 = ('Algiers', 'Algeria', 3.9) #tuple
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ', Country:', capital [1], 'Population:', capital [2])
    
#lists in tuples
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.6)
print(user_data)

