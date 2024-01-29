import json
# gets recipes data from json file
with open("recipes.json", "r") as file:
    file = json.load(file)
#TODO user input is set for now, will work on getting from website
userInput  = ["flour", "butter", "sugar"]

# recipe list that contains the ingredients given
recipesList = []

# list with only recipes that can be made

possibleRecipes = []

def recipeSearcher(userInput):
    for i in file:
        test = i["Ingredients"]
        if any(element in test for element in userInput):
            recipesList.append(i["Name"])
# only includes recipes that can be made with current ingredients
def possibleRecipeGen(userInput):
    for i in file:
        test = i["Ingredients"]
        if all(element in test for element in userInput):
            possibleRecipes.append(i["Name"])

possibleRecipeGen(userInput)
print(possibleRecipes)