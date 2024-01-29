import json
# gets recipes data from json file
with open("recipes.json", "r") as file:
    file = json.load(file)
#TODO user input is set for now, will work on getting from website
userInput  = ["butter"]

# recipe list that contains the ingredients given
recipesList = []

for i in file:
    test = i["Ingredients"]
    if all(element in test for element in userInput):
        recipesList.append(i["Name"])

print(recipesList)