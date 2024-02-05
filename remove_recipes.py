import json
import subprocess

# Asks for recipe to delete
Name = input('Enter Name of Recipe to Delete\n')

# Current recipeslist
recipes = []

# Updated recipes list
new_recipes = []

# ingredients to remove
ingredient_removed = []

# Ingredients from other recepies
ingredients = []
# Opens recipies list and assigns it to current recipies
with open("static/recipes.json", "r") as file:
    recipes = json.load(file)

# Appends recipies to updated recipies unless it is the recipe to remove 
for r in recipes:
        if r["Name"] == Name:
               ingredient_removed.append(r["Ingredients"])
               print("Recipe Deleted")
        else:
               ingredients.append(r["Ingredients"])
               new_recipes.append(r)
             
# Updates the new recipe list to recipes              
with open("static/recipes.json", "w") as file:
        # Update recipes.json
        json.dump(new_recipes, file, indent=4)

# Iterates through lists and leaves behind unique ingredients to be removed 
for item in ingredients:
       for items in item:
              for rm in ingredient_removed:
                     for rms in rm:
                            if items == rms:
                                          ingredient_removed[0].remove(items)

# Calls to the ingredient remover and removes 
# all unique ingredients from removed recipe
for r in ingredient_removed:
       for t in r:            
              child = subprocess.Popen(["python", "remove_ingredients.py"], stdin=subprocess.PIPE)
              child.communicate(input=t.encode())


       
