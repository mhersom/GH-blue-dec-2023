"""
Wednesday Coursework Continued  - 12.13
"""

#dictionaries - used to store key value pairs

emails = {
    'Anne Stahl': 'astahl@gmail.com'
    'Peter Small': 'peters@gmail.com'
    'Mark Steel': 'mark@steel.com'
}

print (emails['Mark Steel'])

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pajaro'
}

print(spanish_animals['bird'])

#keys must be unique
#keys must be immutable

#dictionary operations

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

grades('Anne') = 'A' #can update this way
print (grades)

grades.update({'John':'A'}) #can also update this way
print(grades)

#check number of key value pairs in dictionary
len(grades) 

#check if given key is presnet in dictionary
if 'John' in grades:
    print('John got:', grades['John'])
    
#delete key
del grades['John']
print(grades)

#iterate a dictionary
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for el in grades:
    print(el)
    
for el in grades.keys():
    print(el)el

for el in grandes.values():
    print(el)
    
for person, grade in grades.items():
    print(person, 'got', grade)grade
    
#Coding exercise
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        break
    if user_input in sample_dict:
        print ('Translation:', sample_dict[user_input])
    else:
        print('No match!')
 
print('Bye!')

