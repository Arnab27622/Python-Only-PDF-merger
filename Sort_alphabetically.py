def sort_filenames_ascending(file_list):
    # This function sorts filenames alphabetically in ascending order.
    # It takes a list of filenames as an argument and sorts it in-place.
    file_list.sort()  # Sort filenames in ascending order
    return file_list


def sort_filenames_descending(file_list):
    # This function sorts filenames alphabetically in descending order.
    # It takes a list of filenames as an argument and sorts it in-place.
    file_list.sort(reverse=True)  # Sort filenames in descending order
    return file_list