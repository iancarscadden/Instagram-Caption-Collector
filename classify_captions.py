from openai import OpenAI
import json

# Assign your open openAI key to the your_api_key
your_api_key = "Your OpenAI API key here"
client = OpenAI(api_key=your_api_key)

CATEGORIES = [
    #Fill this with your categories to sort the captions into groups, example structure: "Hope", "kindness", ...
]

def get_categories(caption):
    """Gets a list of relevant categories for a given caption using OpenAI API."""
    response = client.chat.completions.create(

        # Below choose your model you would like to make the call too, pre-assigned to gpt-4o
        model="gpt-4o",  # Updated model
        messages=[
            {
                "role": "system",

                # Below is the prompt that gets sent to the ChatGPT endpoint
                "content": f"Please classify the following Instagram caption into the relevant categories from this list.: {', '.join(CATEGORIES)}. Respond with a comma-separated list of JUST the category names that apply. If a caption clearly has no relevant categories assign it to the miscellaneous category."
            },
            {
                "role": "user",
                "content": caption,
            },
        ],
        max_tokens=50,
    )
    category_string = response.choices[0].message.content.strip()

    if category_string.lower() == "none":
        return []

    categories = [cat.strip() for cat in category_string.split(",")]
    valid_categories = [cat for cat in categories if cat in CATEGORIES]
    return valid_categories

# Load captions from JSON file

"""Replace the varaibale below with the name of your file cotaining your cleaned captions"""
clean_captions_filename = ""
with open(clean_captions_filename, "r", encoding="utf-8") as f:
    captions = json.load(f)

categorized_captions = []
i = 1
length = len(captions)
# Process all captions (removed the slicing)
for caption in captions:
    if caption is not None:  # Skip empty captions (if any)
        categories = get_categories(caption)
        # Corrected formatting to include the closing bracket
        categorized_captions.append(f"[{', '.join(categories)}] {caption}")
        print(f'{i}/{length}')  # More informative progress message
        i += 1

# Save the categorized captions to a new json file
# You may adjust the name of the file that the categorized captions will end up in
categorized_captions_file = "categoized_captions.json"
with open(categorized_captions_file, "w", encoding="utf-8") as f:
    json.dump(categorized_captions, f, ensure_ascii=False, indent=4)
