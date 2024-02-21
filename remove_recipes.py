import json


def main():
    # Asks for recipe to delete
    DELETED_RECIPE = input(
        "Enter the name of the recipe to be deleted:\n").title()

    # Current recipeslist
    recipes = []

    # Updated recipes list
    new_recipes = []

    # Opens recipes list and assigns it to current recipes
    with open("static/recipes.json", "r") as file:
        recipes = json.load(file)

    # Appends recipes to updated recipes unless it is the recipe to remove
    for r in recipes:
        if r["Name"] != DELETED_RECIPE:
            new_recipes.append(r)
        else:
            print("Removed", r["Name"])

    # Ingredients from other recepies
    ingredients = set()

    for r in new_recipes:
        ingredients.update(r["Ingredients"])

    # Updates the new recipe list to recipes
    with open("static/recipes.json", "w") as file:
        # Update recipes.json
        json.dump(new_recipes, file, indent=4)

    # Updates the new recipe list to recipes
    with open("static/ingredients.json", "w") as file:
        # Update recipes.json
        json.dump(list(ingredients), file, indent=4)

    print("Updated recipes")


if __name__ == "__main__":
    main()
