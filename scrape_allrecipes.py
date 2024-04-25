from add_recipes import add_recipe
import requests
from bs4 import BeautifulSoup
import unicodedata
import re
import json


with open("static/ingredients.json", "r") as all_ingredients:
    all_ingredients = json.load(all_ingredients)


def get_recipe_name(page):
    response = requests.get(page)
    page = BeautifulSoup(response.text, 'html.parser')
    # retrieves recipes names
    recipe_name = page.find('h1', class_='article-heading type--lion')
    return recipe_name.text


def get_ingredients(page):
    response = requests.get(page)
    page = BeautifulSoup(response.text, 'html.parser')
 # gets list of ingredients
    ingredients_list = page.find_all(
        'span', attrs={'data-ingredient-name': True})
    ingredients = [normalize_text(item.text).lower()
                   for item in ingredients_list]
    return ingredients


def get_page(url):
    url_list = []
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    for link in page.find_all("a"):
        test = link.get('href')
        if 'https://www.allrecipes.com/recipe/' in test:
            url_list.append(link.get('href'))
    for url in url_list:
        ingredients = get_ingredients(url)
        recipe_name = get_recipe_name(url)
        validate_ingredients(ingredients)
        add_recipe(name=recipe_name, ingredients=ingredients, link=url)


def validate_ingredients(ingredients):
    print("\n\nValidating ingredients...\nPress enter to confirm, \"r\" to remove, or a new name to rename.\n")
    i = 0
    while (i < len(ingredients)):
        user_input = input(f"{ingredients[i]} :  ")
        if user_input == "" or user_input == "y" or user_input == "yes":
            i += 1
            continue

        if user_input == "r":
            ingredients.pop(i)
            continue

        if ingredients[i] in all_ingredients:
            print("This Ingredient is already on the list")
            all_ingredients.pop(all_ingredients.index(user_input))
            ingredients[i] = user_input
            i += 1
            continue
        else:
            ingredients[i] = user_input
            i += 1


def normalize_text(input_text):
    normalized = unicodedata.normalize('NFKC', input_text)
    return normalized.replace('\xa0', ' ')


def main():
    get_page('https://www.allrecipes.com/gallery/best-roast-chicken-recipes/')


if __name__ == "__main__":
    main()
