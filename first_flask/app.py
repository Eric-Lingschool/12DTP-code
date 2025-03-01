from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title = "Home")


@app.route("/pizza/<float:id>")
def pizza(id):
    return render_template("pizza.html", id=id)


@app.route("/all_pizza")
def all_pizza():
    conn = sqlite3.connect("pizza.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pizza")
    pizzas = cur.fetchall()
    conn.close()
    return render_template("all_pizza.html", pizzas = pizzas)


if __name__ == "__main__":
    app.run(debug = True)
