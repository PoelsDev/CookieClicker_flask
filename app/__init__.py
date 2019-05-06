from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

score = 0

@app.route("/click")
def click():
    score+=1

@app.route("/cookieclicker")
def cookieclicker():
    return render_template("index.html")

@app.route("/")
def home():
    return redirect(url_for("cookieclicker"))
    
app.run(debug=1)