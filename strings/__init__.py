import os
import logging
from typing import List
import yaml

logging.basicConfig(level=logging.INFO)

languages = {}
languages_present = {}

def get_string(lang: str):
    return languages[lang]

try:
    for filename in os.listdir(r"./strings/langs/"):
        if "en" not in languages:
            with open(r"./strings/langs/en.yml", encoding="utf8") as en_file:
                languages["en"] = yaml.safe_load(en_file)
                if not languages["en"]:
                    raise ValueError("Base language file 'en.yml' is empty or invalid.")
                languages_present["en"] = languages["en"].get("name", "English")
        if filename.endswith(".yml"):
            language_name = filename[:-4]
            if language_name == "en":
                continue
            with open(r"./strings/langs/" + filename, encoding="utf8") as lang_file:
                languages[language_name] = yaml.safe_load(lang_file)
                if not languages[language_name]:
                    logging.warning(f"Language file '{filename}' is empty or invalid.")
                    continue
                for item in languages["en"]:  # Fallback to English for missing keys
                    if item not in languages[language_name]:
                        languages[language_name][item] = languages["en"][item]
            languages_present[language_name] = languages[language_name].get("name", f"Unknown ({language_name})")
except Exception as e:
    logging.error(f"There was an issue setting up language files: {e}")
    exit()
