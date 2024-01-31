import json

# Asks for recipe to delete
Name = input('Enter Name of Recipe to Delete\n')

# Current recipeslist
recipies = []

# Updated recipes list
new_recipies = []

# Opens recipies list and assigns it to current recipies
with open("static/recipes.json", "r") as file:
    recipies = json.load(file)

# Appends recipies to updated recipies unless it is the recipe to remove 
for r in recipies:
        if r["Name"] == Name:
               print("Recipe Deleted")
        else:
               new_recipies.append(r)
             
# Updates the new recipe list to recipes              
with open("static/recipes.json", "w") as file:
        # Update recipes.json
        json.dump(new_recipies, file, indent=4)
