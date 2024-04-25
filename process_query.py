import json

# Reads recipes from json
with open("static/recipes.json", "r") as file:
    all_recipes = json.load(file)


def recipes(ingredients):
    recipes_list = []
    for recipe in all_recipes:
        count = len(set(recipe["Ingredients"]) & set(ingredients))
        if count > 0:
            recipes_list.append(recipe)

    recipes_list.sort(key=lambda x: len(
        set(x["Ingredients"]) & set(ingredients)), reverse=True)

    return recipes_list[:12]
