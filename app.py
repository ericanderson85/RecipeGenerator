from flask import Flask, render_template, request
import process_query as process_query

app = Flask(__name__)


# This method recieves the user input from the front end
@app.route('/receive_ingredients', methods=['POST'])
def receive_ingredients():
    print("a")
    process(request.json)
    return {'status': 'success'}, 200


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
