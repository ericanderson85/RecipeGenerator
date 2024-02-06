import json

# Reads recipes from json
with open("static/recipes.json", "r") as all_recipes:
    all_recipes = json.load(all_recipes)


# Returns all recipes that can be made and all recipes that can almost be made
def recipes(ingredients):
    print(ingredients)
    possible = possible_recipes(ingredients)
    print(possible)
    almost = [element for element in recipe_search(
        ingredients) if element not in possible]
    return (possible, almost)


# Returns all recipes that can be made with the given ingredients
def possible_recipes(ingredients):
    possible_recipes_list = []
    for recipe in all_recipes:
        if all(ingredient in ingredients for ingredient in recipe["Ingredients"]):
            possible_recipes_list.append(recipe)
    return possible_recipes_list


# Returns all recipes that can almost be made with the given ingredients
def recipe_search(ingredients):
    recipe_search_list = []
    for recipe in all_recipes:
        if any(ingredient in ingredients for ingredient in recipe["Ingredients"]):
            recipe_search_list.append(recipe)
    return recipe_search_list
