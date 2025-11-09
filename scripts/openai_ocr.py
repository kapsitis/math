import os
import pathlib
import sys
import traceback
from dotenv import load_dotenv
from PIL import Image
import openai
import base64
import re

# This class converts screenshots into Markdown using OpenAI's Vision API
class OpenAIOCR:
    openai_api_key = "NA"
    openai_model = "NA"

    def __init__(self, openai_api_key, openai_model):
        self.openai_api_key = openai_api_key
        self.openai_model = openai_model
        openai.api_key = openai_api_key

    # Helper: Convert image to base64-encoded bytes for OpenAI API
    def encode_image_to_base64(self, image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    def summarize_images_in_directory(self, input_dir: str):
        model = self.openai_model
        print(f"Using OpenAI model: {model}")

        prompts = [
            """Convert the screenshot into Markdown (if there is any text outside a table). 
            Precede it by a YAML data extracted from the table (usually 
            titled "Источники и прецеденты использования"), keep the Russian original.  
            Start and terminate your Markdown with three backquotes (```)""",
            
            """Convert the screenshot of problem number {problemnum} into Markdown; 
            keep the Russian original.
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
            
            (add any values from table under "Источники и прецеденты использования", if present)
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

            ... text under "Решение"
            ```

            If there are images in the screenshot, use names 
            ![]({problemnum}.png), ![]({problemnum}A.png), ![]({problemnum}B.png), etc.
            """
        ]

        input_path = pathlib.Path(input_dir)
        if not input_path.is_dir():
            print(f"Error: The specified input path '{input_dir}' is not a valid directory.")
            return

        png_files = list(input_path.glob('*.png'))
        print(f"Found {len(png_files)} PNG images to process.")


        count = 0
        for image_path in png_files:
            count += 1
            # Terminate, if too many images are processed
            if count > 1: 
                break
            try:
                image_name = image_path.name
                problem_number = int(re.match(r"^(\d+)", image_name).group(1))
                
                prompt_num = 0 if image_name.endswith("A.png") else 1

                system_prompt = prompts[prompt_num]

                system_prompt = system_prompt.format(problemnum=problem_number)

                print(f"\nProcessing image: {image_path.name} with prompt# {prompt_num}...")

                # Read image as base64
                img_b64 = self.encode_image_to_base64(image_path)
                # Compose OpenAI vision message (see API docs)
                messages = [
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{img_b64}"
                                }
                            }
                        ]
                    }
                ]

                response = openai.chat.completions.create(
                    model=model,
                    messages=messages,
                    max_tokens=4096,
                    temperature=0.2,
                )
                summary_text = response.choices[0].message.content

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

            except Exception:
                print(f"An error occurred while processing {image_path.name}")
                traceback.print_exc()
                print("Skipping this file.")

        print("\nProcessing complete.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python openai_ocr.py <input_dir>")
        sys.exit(1)

    directory_path = sys.argv[1]

    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_model = os.getenv('OPENAI_MODEL', 'gpt-5')

    oaiOcr = OpenAIOCR(openai_api_key, openai_model)
    oaiOcr.summarize_images_in_directory(directory_path)