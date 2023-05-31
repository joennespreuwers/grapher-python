from flask import Flask, render_template, request, Response, redirect, url_for
from grapher import plot


from matplotlib import pyplot as plt

app = Flask(__name__)
debug = True
port = 8080


@app.route("/", methods=["GET", "POST"])
def index():
    image_data = None
    if request.method == "POST":
        data = request.form.to_dict()
        f = data["form_1"]
        if f:
            print(f)
            image_data = plot(f)
        else:
            image_data = plot("x")

    return render_template("index.html", image_data=image_data)


if __name__ == "__main__":
    app.run(debug=debug, port=port)
