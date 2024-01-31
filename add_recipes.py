import json

# Create a new recipe to add (( EDIT THESE ))
NAME = "Pizza"
INGREDIENTS = ["flour", "salt", "sugar", "yeast", "oil", "tomato sauce",
               "italian seasoning", "garlic powder", "pepper", "pepperoni slices", "cheese"]
LINK = "https://www.food.com/recipe/easy-and-quick-homemade-pizza-22754/"


def main():

    # Create recipes list
    recipes = []

    # Open recipes.json and read it to recipes list
    with open("static/recipes.json", "r") as file:
        recipes = json.load(file)

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

    with open("static/recipes.json", "w") as file:
        # Update recipes.json
        json.dump(recipes, file)
    print(f"Added {NAME} to recipes")

    recipe_ingredients = []
    # Add ingredients from recipes list to json
    for r in recipes:
        for i in r["Ingredients"]:
            if i not in recipe_ingredients:
                recipe_ingredients.append(i)

    with open('static/ingredients.json', "w") as file:
        json.dump(recipe_ingredients, file)

    print(f"Updated ingredients")


if __name__ == "__main__":
    main()
