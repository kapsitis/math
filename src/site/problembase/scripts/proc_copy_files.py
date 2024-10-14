import os
import shutil

def move_and_overwrite(src, dest):
    """Moves a source file to a destination, overwriting the destination."""
    try:
        shutil.move(src, dest)
        print(f"Moved and overwrote {dest} with {src}")
    except FileNotFoundError:
        print(f"Source file not found: {src}")
    except Exception as e:
        print(f"An error occurred while moving {src} to {dest}: {e}")

def main(input_file):
    with open(input_file, 'r') as file:
        for dest_file in file:
            dest_file = dest_file.strip() # Strip newline and spaces
            # Determine the corresponding source file
            if dest_file.endswith(".md"):
                src_file = dest_file[:-3] + "2.md"
                # Move the source file to the destination
                move_and_overwrite(src_file, dest_file)

if __name__ == '__main__':
    input_file_path = 'resources/input_files.csv'  # Replace with the path to your input file
    main(input_file_path)