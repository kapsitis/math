import re
import sys


def replace_func(match):
    small_content = match.group(1)
    comment_content = match.group(5).strip()

    # Split comment content by lines and filter out key=value pairs
    lines = comment_content.split('\n')
    key_value_pairs = [line for line in lines if '=' in line]

    # Create new list elements from the key=value pairs
    new_elements = ['* ' + line.replace('=', ':') for line in key_value_pairs]

    # Remove the key=value lines from the comment
    remaining_comment_lines = [line for line in lines if line not in key_value_pairs]

    # Insert new list elements into <small> tag content
    updated_small_content = '<small>' + small_content.rstrip() + '\n' + '\n'.join(new_elements) + '\n\n</small>'

    # Reconstruct the comment without key=value pairs
    updated_comment = '<!--\n' + '\n'.join(remaining_comment_lines) + '\n-->'

    return updated_small_content + '\n\n' + updated_comment



def transform_markdown(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Regex to find "<small>...</small>" followed by "<!--...-->"
    pattern = re.compile(r'<small>((.|\n)*?)</small>((.|\n)*?)<!--((.|\n)*?)-->', re.MULTILINE)
    # Replacing using the defined function
    updated_content = re.sub(pattern, replace_func, content)

    with open(output_file, 'w') as file:
        file.write(updated_content)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        transform_markdown(input_path, output_path)
    else:
        print("Usage: python transform_comments.py input.md output.md")