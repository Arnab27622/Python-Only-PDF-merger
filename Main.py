# pdf_merger_with_progress.py

import PyPDF2
import os
import Sort_alphabetically
from Sort_by_size import sort_by_file_size
from Sort_by_modified_date import sort_files_by_modified_date
import logger_debugger
from Progress_indicator import (
    calculate_progress,
    update_progress_bar,
    display_percentage_completion,
    estimate_time_remaining,
    clear_previous_output,
    display_end_of_process_message,
)

try:
    # Set up logger
    logger = logger_debugger.setup_logger(__name__)

    # Create a PdfMerger object
    merger = PyPDF2.PdfMerger()

    # Change the directory to the directory where the files are
    direct = input("Enter the Directory where the PDFs are: ")
    os.chdir(f"{direct}")

    # Print the available sorting options
    print(
        "\nSort the PDFs of the directory:\n1. Alphabetically\n2. File Size\n3. Modification Date"
    )

    # Get the user's choice for sorting the PDF files
    sort_choice = int(input("\nEnter Your Choice: "))

    # Get a list of PDF files in the current directory
    pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

    # Check if there are any PDF files in the directory
    if not pdf_files:
        print("There are no PDFs in the Directory.")
        exit()

    # Sort the PDF files based on the user's choice
    if sort_choice not in {1, 2, 3}:
        print("Invalid choice. Exiting.")
        exit()

    if sort_choice == 1:
        print("\nChoice:\n1. Ascending Order\n2. Descending Order")
        ascend_choice = int(input("\nEnter your choice: "))

        if ascend_choice not in {1, 2}:
            print("Invalid choice. Exiting.")
            exit()

        if ascend_choice == 1:
            pdf_files = Sort_alphabetically.sort_filenames_ascending(pdf_files)
        else:
            pdf_files = Sort_alphabetically.sort_filenames_descending(pdf_files)

    elif sort_choice == 2:
        print("\nChoice:\n1. Ascending Order\n2. Descending Order")
        ascend_choice = int(input("\nEnter your choice: "))

        if ascend_choice not in {1, 2}:
            print("Invalid choice. Exiting.")
            exit()

        pdf_files = sort_by_file_size(pdf_files, reverse=(ascend_choice == 2))

    elif sort_choice == 3:
        print("\nChoice:\n1. Ascending Order\n2. Descending Order")
        ascend_choice = int(input("\nEnter your choice: "))

        if ascend_choice not in {1, 2}:
            print("Invalid choice. Exiting.")
            exit()

        pdf_files = sort_files_by_modified_date(
            pdf_files, ascending=(ascend_choice == 1)
        )

    # Print the available PDF files
    print("\nAvailable PDF files:")
    for index, pdf_file in enumerate(pdf_files, start=1):
        print(f"{index}. {pdf_file}")

    # Ask the user to select the PDFs they want to merge
    selected_indices = input(
        "Enter the indices of the PDFs you want to merge (comma-separated): "
    )
    selected_indices = [int(index) - 1 for index in selected_indices.split(",")]

    # Initialize progress variables
    num_merged = 0
    total_files = len(selected_indices)
    clear_previous_output()

    # Iterate over the selected PDFs and append them to the merger
    for index in selected_indices:
        # Ensure the index is valid
        if 0 <= index < len(pdf_files):
            # Provide the full path to the PDF file
            pdf_path = os.path.join(os.getcwd(), pdf_files[index])
            merger.append(pdf_path)
            num_merged += 1
            progress = calculate_progress(num_merged, total_files)
            clear_previous_output()
            print(
                update_progress_bar(progress),
                display_percentage_completion(progress),
                estimate_time_remaining(progress, average_time_per_file=2),
            )
        else:
            print(f"Invalid index: {index + 1}")

    # Enter the name of the output file
    output_pdf = input("Enter the desired name of the merged pdf: ")

    # Enter the desired directory to save the output_pdf file
    res_direct = input(
        f"Enter the directory where you want to save the {output_pdf}.pdf: "
    )
    os.chdir(f"{res_direct}")

    # Write the merged PDF to the output file
    merger.write(f"{output_pdf}.pdf")

    # Close the merger object
    merger.close()

    # Print a success message
    display_end_of_process_message()

except Exception as e:
    logger.error(f"An error occurred: {e}")