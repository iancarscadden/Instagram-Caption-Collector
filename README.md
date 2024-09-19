# Instagram Caption Collector

This repository contains Python scripts that can be used to collect a specified number of captions from posts on an Instagram account. The script starts at the most recent post and iteratively goes post by post, collecting captions. This repository also contains files to clean the captions, then categorize them using user-specified categories with the help of the ChatGPT API. Additionally, a file is included to translate the categorized captions into an Excel file.

## Features
- Collect captions from any Instagram account.
- Clean and process captions for easier categorization.
- Use the ChatGPT API to categorize captions into user-specified categories.
- Export categorized captions into an Excel file.

## Step 1: Collect Captions
Use the `get_captions.py` script to collect captions from an Instagram account.

1. Input your personal Instagram username and password to authenticate the session.
2. Input the Instagram account from which you want to pull captions.
3. Specify the number of posts you want to parse. This will be clearly visible as a variable in the script.
4. The collected captions will be saved in a file named `raw_captions.json`.

> **Note:** These scripts require the use of JSON files as intermediaries to store the caption data.

## Step 2: Clean Captions
Once you have the captions in `raw_captions.json`, the next step is to clean them.

1. Use the `clean_captions.py` script to clean the raw captions.
2. In the script, you will find comments specifying what you need to do. Initialize variables with the name of your raw captions file (`raw_captions.json` by default).
   
> **Note:** The cleaning process involves steps such as removing unnecessary characters and ensuring proper formatting.

## Step 3 (Optional): Categorize Captions Using ChatGPT
If you want to categorize your captions and export them to Excel, proceed with this step.

1. Use the `categorize_captions.py` script.
2. You will need to:
   - Input your API key (obtain from [OpenAI API](https://openai.com/index/openai-api/)).
   - Define the categories you would like to use for the captions.
   - Specify the file name of your cleaned captions (e.g., `cleaned_captions.json`).
   - Set the file name for the categorized captions output.
   
> **Note:** This step requires the use of the OpenAI API, which may incur real costs depending on your usage.

## Step 4 (Optional): Export to Excel
To translate your categorized captions into an Excel file:

1. Use the `captions_to_excel.py` script.
2. Provide the `.json` file with your categorized captions.
3. The script will create an Excel file with column headers representing your categories, and each caption will be placed under its specified category.

> **Tip:** Ensure the caption list you are working with matches the one used in the `categorize_captions.py` script.

## Issues
If you encounter any issues or have questions about the code, feel free to open an issue in this repository. Contributions are also welcome. Thank you for using this tool!

