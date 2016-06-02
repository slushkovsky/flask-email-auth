from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'email_auth.login'

import sys
sys.path.append('../../../')
from flask_email_auth.models import init_email_auth, EAuthBase
from flask_email_auth.routes import bp as bp_email_auth

init_email_auth(app, db.session)
app.register_blueprint(bp_email_auth)

db.create_all()
EAuthBase.metadata.create_all(db.engine)


from . import routes
