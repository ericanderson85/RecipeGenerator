from flask import Flask, render_template, request
import process_query as process_query
import json

app = Flask(__name__)


# This method recieves the user input from the front end
@app.route('/receive_ingredients', methods=['POST'])
def receive_ingredients():
    recipe_list = process(request.json)
    return render_template('recipes.html', recipe_list=recipe_list)


def process(ingredients):
    # result list index 0 contains recipes that only have the given ingredients
    # result list index 1 contains recipes that have the ingredient and are missing other ingredients
    result_list = []
    print("Ingredients selected:")
    for ingredient in ingredients:
        process_query.INPUT.append(ingredient)
    process_query.possible_recipes(process_query.INPUT)
    process_query.recipe_search(process_query.INPUT)
    result_list.append(process_query.possible_recipes_list)
    result_list.append(process_query.recipe_search_list)
    for x in (result_list[1]):
        if x in result_list[0]:
            result_list[1].remove(x)
    return result_list


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
