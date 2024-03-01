import os
import shutil

def copy_png_files(src_directory, dest_directory):
    """
    Copies all PNG files from src_directory and its subdirectories to dest_directory, overwriting any existing files with the same name.
    """

    # Ensure the destination directory exists, if not, create it
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.endswith(".png"):
                # Path of the source file
                src_file_path = os.path.join(root, file)
                
                # Path of the destination file
                dest_file_path = os.path.join(dest_directory, file)
                
                # Copy the file, overwriting any existing file with the same name
                shutil.copy(src_file_path, dest_file_path)
                print(f"Copied: {src_file_path} to {dest_file_path}")

if __name__ == "__main__":
    # Root directory containing the PNG files and subdirectories
    src_directory = '.'
    
    # Target directory where PNG files will be copied
    dest_directory = 'myimages'
    
    copy_png_files(src_directory, dest_directory)

    print("All PNG files have been copied successfully.")