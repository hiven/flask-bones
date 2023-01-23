from flask import Flask, render_template


@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')
