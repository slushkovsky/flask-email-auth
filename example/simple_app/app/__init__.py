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
from flask_email_auth.utils import setting_name, module_member

@login_manager.user_loader
def load_user(user_id):
    User = module_member(app.config[setting_name('USER_MODEL')])
    return db.session.query(User).filter_by(id=user_id).first()

init_email_auth(app, db.session)
app.register_blueprint(bp_email_auth)

db.create_all()
EAuthBase.metadata.create_all(db.engine)


from . import routes
