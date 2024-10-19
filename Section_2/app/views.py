from flask import render_template
from app import app

@app.route('/')
def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("inheritance.html",fruits=fruits)