from flask.ext.login import LoginManager
lm = LoginManager()

from flask.ext.restless import APIManager
api = APIManager()

from travis import Travis
travis = Travis()