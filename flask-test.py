from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def homepage():
    time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    author1 = "Aaron Chen"
    author2 = "Tim Cheng"
    return render_template("index.html", author1=author1, author2=author2, time=time)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)