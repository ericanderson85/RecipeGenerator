import json


def main():
    # Create recipes list
    recipes = []

    # Open recipes.json and read it to recipes list
    with open("recipes.json", "r") as file:
        recipes = json.load(file)

    # Create new recipe to add (( EDIT THESE ))
    name = "Sugar Cookies"
    ingredients = ["butter", "sugar", "flour"]
    link = "https://bellyfull.net/easy-sugar-cookie-recipe/"

    # Create dictionary for new recipe
    new_recipe = {"Name": name.title(),
                  "Ingredients": [ingredient.lower() for ingredient in ingredients],
                  "Link": link}

    # Make sure the name isn't already in recipes
    for r in recipes:
        if r["Name"] == name:
            print(f"{name} already in recipes")
            return

    # Append new recipe to recipes list
    recipes.append(new_recipe)

    with open("recipes.json", "w") as file:
        # Update recipes.json
        json.dump(recipes, file)

    print(f"Added {name} to recipes")


if __name__ == "__main__":
    main()
