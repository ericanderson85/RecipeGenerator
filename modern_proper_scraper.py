from add_recipes import add_recipe
import requests
from bs4 import BeautifulSoup
import unicodedata

# Reference url for testing purposes
# url = 'https://themodernproper.com/baked-salmon-with-grapefruit-salad'


def parse_recipe_name(page):
    # On this website the recipe name is an h1 element with an 'post-hero__title' class
    recipe_name = page.find('h1', class_='post-hero__title')
    return recipe_name.text


def parse_ingredients(page):
    # Create an empty ingredients list
    ingredients_list = []

    # Navigating through the HTML to retreive the ingredients
    # Using If statements to ensure that the value exist and doesnt error
    items = page.find('ul', class_='recipe-ingredients__list')
    if items:
        for item in items.find_all('li', class_='recipe-ingredients__item'):
            ingredient = item.find(
                'span', class_='recipe-ingredients__item--ingredient')
            if ingredient:
                ingredient_text = ingredient
                ingredients_list.append(ingredient_text)
    ingredients = [normalize_text(item.text).lower()
                   for item in ingredients_list]
    return ingredients


def main():
    urls = get_urls()
    for url in urls:
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

        if url.lower() == "done":
            print()
            return list(url_list)

        url_list.add(url)


def parse_page(url):
    response = requests.get(url)
    html_content = response.content
    page = BeautifulSoup(html_content, 'html.parser')
    ingredients = parse_ingredients(page)
    recipe_name = parse_recipe_name(page)
    print(recipe_name, ingredients, url)
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
