from flask import Flask, render_template
from ..home import home

@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')
