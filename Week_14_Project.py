"""
Week 14 Project
"""

#Use Case: Your company needs to learn about the files located on various machines. You have been asked to build a script that extracts 
#information such as the name and size about the files in the current working directory and stores it in a list of dictionaries.

import os

# Get the current working directory
cwd = os.getcwd()  # Get the current working directory

# Generate file information
directory = os.listdir(cwd)  # Get a list of files in the current working directory

files_list = []  # Initialize an empty list to store file information

# How to get the file name and size.
def get_file_info(file_path):
    file_name = os.path.basename(file_path)  # Extract the file name from the full path
    file_size = os.path.getsize(file_path)  # Get the size of the file
    file_info = {'File Name: ': file_name, 'File Size: ': file_size}  # Create a dictionary with file information
    files_list.append(file_info)  # Append the file information dictionary to the list
    print(files_list)  # Print the list of dictionaries after each file is processed

# Iterate through each file in the directory
for file_name in directory:
    file_path = os.path.join(cwd, file_name)  # Create the full path to each file
    get_file_info(file_path)  # Call the function to get file information for each file

# Print the list of dictionaries
for file_info in files_list:
    print(file_info)
