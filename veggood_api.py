from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/post", methods=['POST'])


@app.route("/")
def homepage():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)