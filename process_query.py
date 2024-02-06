import json

# Reads recipes from json
with open("static/recipes.json", "r") as all_recipes:
    all_recipes = json.load(all_recipes)


# Returns all recipes that can be made and all recipes that can almost be made
def recipes(ingredients):
    possible_recipes_list = []
    recipe_search_list = []
    for recipe in all_recipes:
        if all(ingredient in ingredients for ingredient in recipe["Ingredients"]):
            possible_recipes_list.append(recipe)
        elif any(ingredient in ingredients for ingredient in recipe["Ingredients"]):
            recipe_search_list.append(recipe)
    return possible_recipes_list, recipe_search_list
