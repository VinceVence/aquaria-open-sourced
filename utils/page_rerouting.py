import shutil
import os

def move_files(src_dir, dst_dir):
    # Create destination directory if it doesn't exist
    os.makedirs(dst_dir, exist_ok=True)

    # Check if source directory exists and is a directory
    if not os.path.isdir(src_dir):
        print(f"Source directory {src_dir} does not exist or is not a directory")
        return

    # Get a list of all file names in the source directory
    files = os.listdir(src_dir)

    for file_name in files:
        # Construct full file path
        source = os.path.join(src_dir, file_name)
        destination = os.path.join(dst_dir, file_name)
        
        # Check if source file exists and is a file
        if not os.path.isfile(source):
            print(f"Source file {source} does not exist or is not a file")
            continue

        try:
            # Move the file to the destination directory
            shutil.move(source, destination)
            print(f"Successfully moved {source} to {destination}")
        except Exception as e:
            print(f"Error occurred while moving file {source} to {destination}: {e}")


