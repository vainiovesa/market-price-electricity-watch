from flask import Flask
from flask import render_template
from control import which

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", lights=which())

if __name__ == "__main__":
    app.run()
