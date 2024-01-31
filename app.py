from flask import Flask, render_template, request

app = Flask(__name__)


# This method recieves the user input from the front end
@app.route('/receive_ingredients', methods=['POST'])
def receive_ingredients():
    # Call processing function
    recipe_list = process(request.json)

    recipe_list = [
        ["Mac and Cheese", "pasta, cheese, milk", "https://google.com/"],
        ["Scrambled Eggs", "eggs, milk, salt, pepper, butter", "https://amazon.com/"]
    ]

    return render_template('recipes.html', recipe_list=recipe_list)


# TODO
def process(data):
    recipe_list = []
    print("Ingredients selected:")
    for ingredient in data:
        print(ingredient)

    # . . .

    return recipe_list


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
