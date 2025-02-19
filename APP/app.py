from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/2")
def two():
    return "two"


if __name__ == "__main__":
    app.run(debug = True)
