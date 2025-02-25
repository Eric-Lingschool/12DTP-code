from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title = "Home")


@app.route("/pizza/<float:id>")
def pizza(id):
    return render_template("pizza.html", id=id)



if __name__ == "__main__":
    app.run(debug = True)
