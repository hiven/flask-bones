from flask import Flask, render_template
from ..home import home

@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@home.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@home.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')

@home.route('/security', methods=['GET'])
def security():
    return render_template('security.html')
