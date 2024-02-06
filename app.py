from flask import Flask, render_template, request
from process_query import recipes

app = Flask(__name__)


# This method recieves the user input from the front end
@app.route('/receive_ingredients', methods=['POST'])
def receive_ingredients():
    recipe_list, almost_recipes = recipes(request.json)
    return render_template('recipes.html', recipe_list=recipe_list, almost_recipes=almost_recipes)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
