import requests
import sys
import re
import json
import configparser
import argparse

def replace_tex_by_id(text,id_dict):
    count = 1  # skaitītājs unikālu id veidošanai
    pattern_block = re.compile(r"\$\$[^\$]+\$\$") # meklējam visas block latex formulas
    formulas_block = pattern_block.findall(text)
    for formula in formulas_block:
        current_id = "§id{}§".format(count)
        id_dict[current_id] = formula
        # aizstāj formulu tikai 1 reizi
        text = text.replace(formula, current_id, 1)
        count +=1

    pattern = re.compile(r"\$[^\$]+\$") # meklējam visas inline latex formulas
    formulas = pattern.findall(text)
    for formula in formulas:
        current_id = "§id{}§".format(count)
        id_dict[current_id] = formula
        # aizstāj formulu tikai 1 reizi
        text = text.replace(formula, current_id, 1)
        count +=1
    return text


def replace_id_by_tex(text,id_dict):
    for key in id_dict:
        formula = id_dict[key]
        text = text.replace(key, formula, 1)
    return text

def add_newlines_around_solution(text):
    # Add new lines before '# #'
    text = re.sub(r'(?<!\n)(# #)', r'\n\1', text)
    return text


def format_small_tags(text):
    # Add new lines inside <small> tags and before the <small> tag
    def format_inside_small(match):
        content = match.group(2).strip().replace(' * ', '\n* ')
        return f"\n<small>\n{content}\n</small>"

    text = re.sub(r'(<small>)(.*?)(</small>)', format_inside_small, text, flags=re.DOTALL)
    return text


# Read problems one by one from Markdown file "filepath"
def extract_sections_from_md(filepath):
    section_titles = []
    current_section = None
    sections = []
    title = "NA"

    heading_re = re.compile(r'^#\s+<lo-sample/>\s+(.*)')

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            m = heading_re.match(line)
            if m:
                new_title = m.group(1)
                # append the previous (title, current_section)
                if current_section is not None:
                    sections.append((title, current_section))
                title = new_title
                current_section = ''
            elif current_section is not None:
                # before seeing the first title, we do not append anything
                current_section += line
    # Append the last (title, current_section)
    if current_section:
        sections.append((title, current_section))
    return sections

def main():
    parser = argparse.ArgumentParser(description="Translate problem texts from a Markdown file.")
    parser.add_argument("file_path", help="Path to the Markdown file")
    parser.add_argument("output_file", help="Path to the output Markdown file")
    args = parser.parse_args()

    # Extracting problem text from Markdown file
    problem_text = extract_sections_from_md(args.file_path)

    if problem_text:
        try:
            id_dict = dict()
            translated_sections = []

            for title, text in problem_text:
                configParser = configparser.RawConfigParser()
                configFilePath = 'C:/Users/eliz_/Documents/math/src/site/problembase/scripts/translation-script/credentials.txt'
                configParser.read(configFilePath)
                client_id = configParser.get('your-config', 'client_id')
                system_id = configParser.get('your-config', 'system_id')
                service_url = configParser.get('your-config', 'service_url')
                text2 = replace_tex_by_id(text, id_dict)
                response = requests.post(
                    service_url,
                    headers={'Content-Type': 'application/json', 'client-id': client_id},
                    json={
                        'appID': 'TechChillDemo',
                        'systemID': system_id,
                        'text': text2,  # Ensure proper serialization
                        'options': 'alignment,markSentences,tagged'
                    }
                )
                response.raise_for_status()
                translated_text = response.json().get('translation', 'No translation found')
                translated_text2 = replace_id_by_tex(translated_text, id_dict)
                translated_text2 = add_newlines_around_solution(translated_text2)
                translated_text2 = format_small_tags(translated_text2)
                translated_sections.append((title, translated_text2))

            with open(args.output_file, "w", encoding='utf-8') as file:
                for title, translated_text2 in translated_sections:
                    file.write(f"# <lo-sample/> {title}\n{translated_text2}\n")

            print("Translated text has been written to", str(args.output_file))
        except requests.HTTPError as e:
            print("HTTP Error:", e.response.status_code)
            print("Error details:", e.response.content)
        except ValueError as e:
            print("Value Error:", e)
    else:
        print("Problem text not found in Markdown file.")

if __name__ == "__main__":
    main()

# Example usage:
# python translate-md.py ../../lv-vol-2024/content.md content-vol-2024-eng.md