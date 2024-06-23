import os


# Define a function called 'sort_files_by_modified_date' that takes in a list of files and an optional 'ascending' parameter
def sort_files_by_modified_date(files_list, ascending=True):
    """
    Sorts the list of files based on their modification date.

    Args:
        files_list (list): List of file paths.
        ascending (bool, optional): Whether to sort in ascending order.
                                    Defaults to True.

    Returns:
        list: Sorted list of file paths.
    """
    # Sort files based on modification time
    sorted_files = sorted(
        files_list, key=lambda f: os.path.getmtime(f), reverse=not ascending
    )

    # Return the sorted list of files
    return sorted_files
