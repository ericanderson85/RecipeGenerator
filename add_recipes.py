import json

# Create a new recipe to add (( EDIT THESE ))
NAME = "cranberry oatmeal muffins"
INGREDIENTS = ["rolled oats", "yogurt", "oil", "white sugar", "brown sugar", "egg", "flour", "salt", "baking powder", "baking soda", "orange rind", "cranberries"]
LINK = "https://www.food.com/recipe/cranberry-oatmeal-muffins-37861"


def add_recipe(name, ingredients, link):

    # Create recipes list
    recipes = []

    # Open recipes.json and read it to recipes list
    with open("static/recipes.json", "r") as file:
        recipes = json.load(file)

    # Create dictionary for the new recipe
    new_recipe = {"Name": name.title(),
                  "Ingredients": [ingredient.lower() for ingredient in ingredients],
                  "Link": link}

    # Make sure the name isn't already used in recipes
    for r in recipes:
        if r["Name"] == name:
            print(f"{name} already in recipes")
            return

    # Append new recipe to recipes list
    recipes.append(new_recipe)

    with open("static/recipes.json", "w") as file:
        # Update recipes.json
        json.dump(recipes, file, indent=4)
    print(f"Added {name} to recipes")

    recipe_ingredients = []
    # Add ingredients from recipes list to json
    for r in recipes:
        for i in r["Ingredients"]:
            if i not in recipe_ingredients:
                recipe_ingredients.append(i)

    with open('static/ingredients.json', "w") as file:
        json.dump(recipe_ingredients, file, indent=4)

    print(f"Updated ingredients")


def main():
    add_recipe(NAME, INGREDIENTS, LINK)


if __name__ == "__main__":
    main()
