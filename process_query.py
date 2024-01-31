import json

# Reads recipes from json
with open("static/recipes.json", "r") as all_recipes:
    all_recipes = json.load(all_recipes)
# TODO User input is set for now, will work on getting from website
INPUT = []


# List of recipes that can be made
possible_recipes = []
# List of recipes that contain an inputted ingrendient
recipe_search_list = []

# function that adds ingredients to INPUT


def add_ingredient(ingredient):
    INPUT.append(ingredient)

# Generates recipes that can be made with inputted ingredients


def possible_recipes(user_input):
    for recipe in all_recipes:
        if all(element in recipe["Ingredients"] for element in user_input):
            possible_recipes.append(recipe["Name"])


# Searches for recipes that include an inputted ingredient
def recipe_search(user_input):
    for recipe in all_recipes:
        if any(element in recipe["Ingredients"] for element in user_input):
            recipe_search_list.append(recipe["Name"])
