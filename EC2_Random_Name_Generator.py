"""
EC2 Random Name Generator
"""

import random
import string

def unique_names(number_instances, department_name):
    instance_names = []
    
    for _ in range(number_instances):

        # Generate random characters and numbers that will be included in the unique name.
        random_char = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
         
        # Create a unique EC2 name using the department name and random characters
        instance_name = department_name + '_' + random_char
        instance_names.append(instance_name) 
    return instance_names

def main():
    # Allow the user to input how many EC2 instances they want names for
    number_instances = int(input('How many EC2 instances do you want? '))
    
    # Allow the user to input the name of their department
    department_name = input('What department do you work for? ')
    
    # Generate unique EC2 Instance names
    unique_names_list = unique_names(number_instances, department_name)
    
    # Output the unique names
    print("\nGenerated unique EC2 Instance names:")
    final_names = "\n".join(unique_names_list)
    print(final_names)

if __name__ == "__main__":
    main()

