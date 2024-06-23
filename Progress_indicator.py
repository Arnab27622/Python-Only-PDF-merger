# pdf_merger_progress.py


def calculate_progress(num_merged, total_files):
    """Calculate the percentage completion."""
    return (num_merged / total_files) * 100


def update_progress_bar(progress, bar_length=20):
    """Update the progress bar string."""
    completed_length = int(progress / 100 * bar_length)
    bar = "[" + "=" * completed_length + " " * (bar_length - completed_length) + "]"
    return bar


def display_percentage_completion(progress):
    """Display the percentage completion."""
    return f"Progress: {progress:.2f}%"


def estimate_time_remaining(progress, average_time_per_file):
    """Estimate the time remaining."""
    remaining_files = 100 - progress
    remaining_time = remaining_files * average_time_per_file
    return f"Estimated time remaining: {remaining_time:.2f} seconds"


def clear_previous_output():
    """Clear the previous output."""
    # Implementation depends on the terminal environment
    pass


def display_end_of_process_message():
    """Display the end-of-process message."""
    print("PDFs merged successfully!")