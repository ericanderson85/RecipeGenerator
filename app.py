from flask import Flask, render_template, request
from process_query import recipes

app = Flask(__name__)


# This method recieves the user input from the front end
@app.route('/receive_ingredients', methods=['POST'])
def receive_ingredients():
    recipe_list = recipes(request.json)[0]
    print(recipe_list)
    return render_template('recipes.html', recipe_list=recipe_list)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
