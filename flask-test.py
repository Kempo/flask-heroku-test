from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def homepage():
    author1 = "Aaron Chen"
    author2 = "Tim Cheng"
    return render_template("index.html", author1=author1, author2=author2)


@app.route("/ping")
def test():
    return "pong"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)