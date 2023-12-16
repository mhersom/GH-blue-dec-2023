"""
Thursday Course Coding Exercise
"""


def unique(input_list=[]):
    # Create an empty list to store unique elements
    unique_list = []

    # Iterate through each element in the input list
    for x in input_list:
        # Check if the element is not already in the unique_list
        if x not in unique_list:
            # If not, add the element to the unique_list
            unique_list.append(x)

    # Return the final list containing unique elements
    return unique_list

