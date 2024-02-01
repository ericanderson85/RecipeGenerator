import json

# Asks for the Ingredient to remove
Name = input("Which Ingredient do You Want to Remove\n")

# list for ingredients from ingredients
ingredients = []

# updated list of ingredients
new_ingredients = []

# Assigns ingredients to ingredient list
with open("static/ingredients.json", "r") as file:
    ingredients = json.load(file)

# Appends ingredients to new ingredients unless it is the one to remove
for i in ingredients:
    if i == Name:
        print("Ingredient Removed")
    else:
        new_ingredients.append(i)

# Updates ingredients with the new list of ingredients
with open("static/ingredients.json", "w") as file:
        # Update recipes.json
        json.dump(new_ingredients, file, indent=1)
