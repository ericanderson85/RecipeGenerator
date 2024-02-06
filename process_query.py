import json

# Reads recipes from json
with open("static/recipes.json", "r") as all_recipes:
    all_recipes = json.load(all_recipes)


# Returns all recipes that can be made and all recipes that can almost be made
def recipes(ingredients):
    possible_recipes_list = []
    recipe_search_list = {}
    for index, recipe in enumerate(all_recipes):
        current = recipe["Ingredients"]
        if all(ingredient in ingredients for ingredient in current):
            possible_recipes_list.append(recipe)
        # If all ingredients aren't fulfilled, store index and number of missing ingredients
        elif any(ingredient in ingredients for ingredient in current):
            recipe_search_list[index] = sum(
                ingredient in ingredients for ingredient in current) - len(current)

    # Sort and turn back into recipes
    almost_recipes = sorted(recipe_search_list.items(),
                            reverse=True, key=lambda x: x[1])[:4]
    almost_recipes = [all_recipes[index[0]] for index in almost_recipes]

    [print(rec) for rec in almost_recipes]
    return possible_recipes_list, almost_recipes
