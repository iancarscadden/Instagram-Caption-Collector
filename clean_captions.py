import json
import re

# Load captions

# Assign filename to name of your json file containing the raw collected captions, example: "my_captions.json"
filename = "Your file name"

with open(filename, "r", encoding="utf-8") as f:
    captions = json.load(f)

cleaned_captions = []
for caption in captions:
    if caption is not None:
        # Remove newlines
        cleaned_caption = caption.replace("\n", " ")

        # Remove standalone hashtags and trailing whitespace
        cleaned_caption = re.sub(r"\B#\w+\b\s*", "", cleaned_caption)

        cleaned_captions.append(cleaned_caption)

# Save cleaned captions
# Assign save_filename with the file name that you want to save the cleaned captions to, example: cleaned_captions.json
save_filename = "Your file name"
with open(save_filename, "w", encoding="utf-8") as f:
    json.dump(cleaned_captions, f, ensure_ascii=False, indent=4)
