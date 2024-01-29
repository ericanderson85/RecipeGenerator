import json


def main():
    # Create recipes list
    recipes = []

    # Open recipes.json and read it to recipes list
    with open("recipes.json", "r") as file:
        recipes = json.load(file)

    # Create a new recipe to add (( EDIT THESE ))
    NAME = "Sugar Cookies"
    INGREDIENTS = ["butter", "sugar", "flour"]
    LINK = "https://bellyfull.net/easy-sugar-cookie-recipe/"

    # Create dictionary for the new recipe
    new_recipe = {"Name": NAME.title(),
                  "Ingredients": [ingredient.lower() for ingredient in INGREDIENTS],
                  "Link": LINK}

    # Make sure the name isn't already used in recipes
    for r in recipes:
        if r["Name"] == NAME:
            print(f"{NAME} already in recipes")
            return

    # Append new recipe to recipes list
    recipes.append(new_recipe)

    with open("recipes.json", "w") as file:
        # Update recipes.json
        json.dump(recipes, file)

    print(f"Added {NAME} to recipes")


if __name__ == "__main__":
    main()
