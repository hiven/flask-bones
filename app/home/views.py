from flask import Flask, g, render_template, request


@home_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
