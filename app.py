from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():

    return "Welcome to the main page"



@app.route("/sub/")
def who():

    return "Welcome to my subpage"



@app.route("/sub/<username>")
def greet(username):

    return f"Welcome {username}"


# app.run(host= '0.0.0.0', port=5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
