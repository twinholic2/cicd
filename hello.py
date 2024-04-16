"""
test hello.py
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    hello_world API
    """
    return "<p>Hello, World!! 123456</p>"
