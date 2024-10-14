import subprocess

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def create_second_file_path(first_file_path):
    # Remove the last 3 characters (".md") and append "2.md" instead
    return first_file_path[:-3] + "2.md"

def run_diff_on_file_pairs(file_pairs):
    for first_file, second_file in file_pairs:
        try:
            result = subprocess.run(['diff', first_file, second_file], capture_output=True, text=True)
            if result.stdout:
                print(f"Difference between {first_file} and {second_file}:\n{result.stdout}")
            else:
                print(f"No differences found between {first_file} and {second_file}.")
        except FileNotFoundError:
            print(f"File not found: {second_file}å")

def main(input_file):
    file_paths = read_input_file(input_file)
    file_pairs = [(path, create_second_file_path(path)) for path in file_paths]

    run_diff_on_file_pairs(file_pairs)

if __name__ == '__main__':
    input_file_path = 'resources/input_files.csv'  # replace with the path to your input file
    main(input_file_path)