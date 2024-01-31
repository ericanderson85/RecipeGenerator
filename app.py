from flask import Flask, render_template, request
import process_query as process_query
import json

app = Flask(__name__)


# This method recieves the user input from the front end
@app.route('/receive_ingredients', methods=['POST'])
def receive_ingredients():
    recipe_list = process(request.json)

    # Use all recipes for now, until process() is finished
    with open('static/recipes.json', 'r') as file:
        recipe_list = json.load(file)
    return render_template('recipes.html', recipe_list=recipe_list)


def process(ingredients):
    recipe_list = []
    print("Ingredients selected:")
    for ingredient in ingredients:
        process_query.INPUT.append(ingredient)
    return recipe_list


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
