from add_recipes import add_recipe
import requests
from bs4 import BeautifulSoup
import unicodedata


def parse_recipe_name(page):
    # On this website the recipe name is an h1 element with an 'article-heading' class
    recipe_name = page.find('h1', class_='article-heading')
    return recipe_name.text


def parse_ingredients(page):
    # On this website each ingredient is a span element with an attribute 'data-ingredient-name'
    ingredients_list = page.find_all(
        'span', attrs={'data-ingredient-name': True})

    ingredients = [normalize_text(item.text).lower()
                   for item in ingredients_list]
    return ingredients


def main():
    for url in get_urls():
        try:
            name, ingredients, link = parse_page(url)
        except:
            print("\nRequest failed for", url, "\n")
            continue

        print(f"\nValidating {url}\n")

        name = validate_name(name)
        validate_ingredients(ingredients)

        print(name)
        print(ingredients)
        print(link)

        add_recipe(name=name, ingredients=ingredients, link=link)


def get_urls():
    url_list = set()
    print("Enter URL for recipe or \"done\" to complete: ")
    while (True):
        url = input()

        if url == "done":
            print()
            return list(url_list)

        url_list.add(url)


def parse_page(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    ingredients = parse_ingredients(page)
    recipe_name = parse_recipe_name(page)
    return [recipe_name, ingredients, url]


def validate_name(name):
    print("Is this name correct?\nType a new name to rename, or press enter to confirm.")
    user_input = input(f"{name}\n")
    if user_input == "" or user_input == "yes" or user_input == "y" or user_input == " ":
        return name
    else:
        return user_input


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

        ingredients[i] = user_input
        i += 1


def normalize_text(input_text):
    normalized = unicodedata.normalize('NFKC', input_text)
    return normalized.replace('\xa0', ' ')


if __name__ == "__main__":
    main()
