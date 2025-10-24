from flask import Flask
from flask import render_template
from control import get_info, RED_BOUNDARY, YELLOW_BOUNDARY

app = Flask(__name__)

@app.route("/")
def index():
    current_time, price, light_control = get_info()
    info = {"rb": RED_BOUNDARY,
            "yb": YELLOW_BOUNDARY,
            "price": price,
            "ct": current_time}

    return render_template("index.html", lights=light_control, info=info)

if __name__ == "__main__":
    app.run()
