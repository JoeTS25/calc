from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = request.args.get("a")
    b = request.args.get("b")
    return add(a,b)

@app.route('/sub')
def subtract():
    a = request.args.get("a")
    b = request.args.get("b")
    return sub(a,b)

@app.route('/add')
def multiply():
    a = request.args.get("a")
    b = request.args.get("b")
    return mult(a,b)


@app.route('/add')
def divide():
    a = request.args.get("a")
    b = request.args.get("b")
    return div(a,b)





