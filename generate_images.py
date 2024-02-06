import openai
import time
import json
import requests
import os

openai.api_key = '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'

# Read recipes from json
with open("./static/recipes.json", "r") as json_file:
    recipes_list = json.load(json_file)

# Create an image for each recipe
for recipe in recipes_list[10:]:
    recipe_name = recipe["Name"]
    file_name = recipe_name.replace(" ", "-")
    if f"{file_name}.jpg" in os.listdir("./static/images"):
        continue
    try:
        response = openai.images.generate(
            model="dall-e-2",
            prompt=recipe_name,
            size="512x512",
            n=1,
        )
        url = response.data[0].url
        image_response = requests.get(url)
        if image_response.status_code == 200:
            with open(f"./static/images/{file_name}.jpg", "wb") as file:
                file.write(image_response.content)
            print(f"Saved {file_name}.jpg")
        else:
            print(f"Failed to download {file_name}.jpg")
            print(url)
    except openai.OpenAIError as e:
        print(f"Error creating {file_name}.jpg")
    # Wait 15 seconds for the next API call
    time.sleep(15)
