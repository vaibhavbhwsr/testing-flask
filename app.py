from flask import Flask
from flask import render_template

app = Flask(__name__)


# this route is simple example for first page.
@app.route("/")
def root_page():
    return "<p>Hello, World!</p>"


# this route shows how to get name from endpoint and use it in function.
@app.route("/<name>/")
def hello_world(name):
    return f"<p>Hello, {name}!</p>"


# this route shows how to use the templates in flask.
@app.route("/using_templates/")
def templates():
    return render_template('hello.html')


# this route shows how to use the templates in flask.
@app.route("/using_contect_in_templates/<name>")
def templates_with_context(name):
    return render_template('hello.html', context={"naam": name, "surname": "Bhawsar"})
