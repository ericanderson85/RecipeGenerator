import json

# Create recipes list
recipes = []

# Open recipes.json and read it to recipes list
with open("recipes.json", "r") as file:
    recipes = json.load(file)

# Create new recipe to add
name = "..."
ingredients = ["Milk", "Butter"]
link = "https://google.com/"

# Create dictionary for new recipe
new_recipe = {"Name": name,
              "Ingredients": ingredients,
              "Link": link}

# Append new recipe to recipes list
recipes.append(new_recipe)

with open("recipes.json", "w") as file:
    # Update recipes.json
    json.dump(recipes, file)
