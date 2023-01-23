from flask import current_app, flash, render_template, request, redirect, url_for
from app import db
from . import main_blueprint
from .models import Items
from .forms import ItemsForm, EditItemsForm


#@main_blueprint.route('/', methods=['GET', 'POST'])
#def home():
#    return render_template('main/index.html')
  
  
@home_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
