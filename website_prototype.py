from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# how to run the website.
# first use following command on cmd(windows)
# then copy the https link given by the cmd and copy paste in your browser
# python -m flask -app website_prototype run

