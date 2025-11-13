import os
import pathlib
import google.generativeai as genai
from PIL import Image
import sys
from dotenv import load_dotenv
import traceback
from functools import cmp_to_key
import re

# This class converts screenshots into Markdown
# Some PDF documents are easier to analyze if we 
# make screenshots and then do OCR on the image. 
# (Extracting text from the PDF would also work, but 
# this does not preserve markup - bullet lists, tables, etc.)
class GeminiOCR:
    gemini_api_key = "NA"
    gemini_model = "NA"

    def __init__(self, gemini_api_key, gemini_model): 
        self.gemini_api_key = gemini_api_key
        self.gemini_model = gemini_model


    def summarize_images_in_directory(self, api_key: str, input_dir: str):
        try:
            genai.configure(api_key=self.gemini_api_key)
            print("Gemini API configured successfully.")
        except Exception as e:
            print(f"Error configuring the Gemini API: {e}")
            print("Please ensure your API key is valid.")
            return

        model = genai.GenerativeModel(self.gemini_model)
        print(f"Using model: {model.model_name}")

        prompts = [
            """Convert the screenshot into Markdown. 
            If there is any text outside a table, create English H2 headings
            followed by text in Russian.
            Convert math formulas into LaTeX and enclose them in-between $ 
            (inline formulas), or $$ (larger formulas).
            Start and terminate your Markdown with three backquotes (```). 

            Add Yaml front-matter listing all values from table under 
            "Источники и прецеденты использования", if present.
            Property names in English; values in Russian original. 
            Sample output: 
            ```
            ---
            book:
              author:Lastname1 A., Lastname2 B. (replace by "Автор")
              year:1970  (the value of "Год издания")
              title:     (replace by "Название")
              publisher: (replace by "Издательство")
              edition:   (replace by "Издание")
            chapter:
              (more values, if any)
            ---
            ## Solution 

            Russian text from under "Решение".

            ## Hint 

            Russian text from under "Подсказка".

            ## Answer 

            Russian text from under "Ответ".            
            ```

            If the entire screenshot is a table, create only the Yaml front-matter.
            If there are images in the screenshot, insert names 
            ![]({problemnum}A.png), ![]({problemnum}B.png)
            """,
            
            """Convert the screenshot of problem number {problemnum} into Markdown.
            Start and terminate your Markdown with three backquotes (```). 
            Convert math formulas into LaTeX and enclose them in-between $ (inline formulas), 
            or $$ (larger formulas). Your output should be a Yaml front-matter 
            followed by Markdown like this:
            ```
            ---
            problemID: {problemnum}
            difficulty: 3   (replace by the number from screenshot following "Сложность")
            suggestedGrade: 6,7,8   (replace by the number(s) in screenshot after "Классы")
            domain:Comb     (always "Comb")
            questionType:NA (always "NA")
            subdomain:NA    (always "NA")
            topic:NA        (always "NA")
            
            (Add any to Yaml values from table under "Источники и прецеденты использования", 
            if present. Property names in English; values in Russian original.)

            book:
              author:Lastname1 A., Lastname2 B. (replace by "Автор")
              year:1970  (replace by "Год издания")
              title:     (replace by "Название")
              publisher: (replace by "Издательство")
              edition:   (replace by "Издание")
            chapter:
              (more values, if any)
            ---
            # <lo-sample/> {problemnum}

            ... text that was under caption "Условие" ...
            
            ## Solution 

            Russian text from under "Решение".

            ## Hint 

            Russian text from under "Подсказка".

            ## Answer 

            Russian text from under "Ответ".
            ```

            If there are images in the screenshot, insert names 
            ![]({problemnum}A.png), ![]({problemnum}B.png), etc.
            """
        ]


        input_path = pathlib.Path(input_dir)
        if not input_path.is_dir():
            print(f"Error: The specified input path '{input_dir}' is not a valid directory.")
            return

        png_files = list(input_path.glob('*.png'))

        def compare_paths(a, b):
            def problem_num(s):
                try:
                    image_name = s.name
                    return int(re.match(r"^(\d+)", image_name).group(1))
                except Exception:
                    return float('inf')
            na, nb = problem_num(a), problem_num(b)
            if na < nb:
                return -1
            if na > nb:
                return 1
            return (a > b) - (a < b)

        png_files = sorted(png_files, key=cmp_to_key(compare_paths))



        print(f"Found {len(png_files)} PNG images to process.")
        count = 0
        for image_path in png_files:

            count += 1
            # Terminate, if too many images are processed
            if count > 1: 
                break
            try:
                img = Image.open(image_path)

                
                image_name = image_path.name
                problem_number = int(re.match(r"^(\d+)", image_name).group(1))
                prompt_num = 0 if image_name.endswith("A.png") else 1
                system_prompt = prompts[prompt_num]
                system_prompt = system_prompt.format(problemnum=problem_number)

                print(f"\nProcessing image: {image_path.name} with prompt# {prompt_num}...")

                contents = [prompts[prompt_num], img]
                response = model.generate_content(contents)
                summary_text = response.text

                # Remove framing from the response
                if summary_text.startswith("```markdown\n"):
                    summary_text = summary_text[10:]
                if summary_text.startswith("```"):
                    summary_text = summary_text[3:]
                if summary_text.endswith("\n```"):
                    summary_text = summary_text[:-4]
                if summary_text.endswith("```"):
                    summary_text = summary_text[:-3]

                output_filename = image_path.with_suffix('.md')
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(summary_text.strip())

                print(f"Successfully created summary: {output_filename.name}")

            except Exception as e:
                print(f"An error occurred while processing {image_path.name}")
                traceback.print_exc()
                print("Skipping this file.")

        print("\nProcessing complete.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gemini_ocr.py <input_dir>")
        sys.exit(1)
    
    directory_path = sys.argv[1]

    load_dotenv()
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    gemini_model = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')

    geminiOcr = GeminiOCR(gemini_api_key, gemini_model)
    geminiOcr.summarize_images_in_directory(gemini_api_key, directory_path)
