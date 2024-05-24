import os

def rename_report_file(directory, old_filename, new_filename):
    old_path = os.path.join(directory, old_filename)
    new_path = os.path.join(directory, new_filename)
    os.rename(old_path, new_path)
    return new_path

def get_latest_report_directory(base_directory, exclude=None):
    directories = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
    directories = [d for d in directories if d != exclude]
    directories.sort(reverse=True)  # Sort by name descending, latest first
    latest_directory = os.path.join(base_directory, directories[0]) if directories else None
    return latest_directory