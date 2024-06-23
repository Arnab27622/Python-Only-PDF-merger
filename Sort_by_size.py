import os


# Define a function called 'sort_by_file_size' that takes in a list of files and an optional 'reverse' parameter
def sort_by_file_size(file_list, reverse=False):
    # Create a list of tuples, where each tuple contains a file and its size
    file_size_list = [(file, os.path.getsize(file)) for file in file_list]

    # Sort the list of tuples based on file size, using the 'key' parameter to specify the sorting criteria
    # The 'reverse' parameter determines whether the sorting order is descending (True) or ascending (False)
    sorted_files = sorted(file_size_list, key=lambda x: x[1], reverse=reverse)

    # Extract the filenames from the sorted list of tuples
    sorted_file_names = [file[0] for file in sorted_files]

    # Return the sorted list of filenames
    return sorted_file_names
