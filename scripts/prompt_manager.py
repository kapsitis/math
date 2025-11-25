import json
# pip install pyyaml
from pathlib import Path
import yaml

class PromptManager:
    prompt_file = "NA"
    prompt_name = "NA"
    system_instruction = "NA"
    user_query = "NA"
    metadata = dict()

    def __init__(self, prompt_file):
        self.prompt_file = prompt_file
        try:
            with Path(self.prompt_file).open("r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Prompt configuration file not found: {self.prompt_file}") from e
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in prompt configuration file: {self.prompt_file}") from e
        # Validate structure and required keys
        if not isinstance(config, dict):
            raise TypeError(
                f"Prompt configuration must be a mapping/dict, got {type(config).__name__}"
            )
        required = ("system_instruction", "user_query")
        missing = [k for k in required if k not in config]
        if missing:
            raise KeyError(f"Missing required key(s) in prompt configuration: {', '.join(missing)}")
        self.system_instruction = config["system_instruction"]
        self.user_query = config["user_query"]
        if not isinstance(self.system_instruction, str) or not self.system_instruction.strip():
            raise ValueError("system_instruction must be a non-empty string")
        if not isinstance(self.user_query, str) or not self.user_query.strip():
            raise ValueError("user_query must be a non-empty string")
        self.metadata = config

    def print(self):
        print(self.metadata)

    @staticmethod
    def prepare_regular_prompt(self, fname_in, fname_out):
        with open(fname_in, 'r') as infile:
            data = json.load(infile)
        with open(fname_out, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        
if __name__ == '__main__': 
    pManager = PromptManager('prompts/prompt-make-section-longer.yaml')
    pManager.print()