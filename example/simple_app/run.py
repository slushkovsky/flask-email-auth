from flask import Flask
from flask.ext.login import login_required, current_user, LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

import sys
sys.path.append('../../../')

from email_auth.models import init_email_auth
from email_auth.routes import bp as bp_email_auth

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'email_auth.login'

init_email_auth(app, db.session)
app.register_blueprint(bp_email_auth)

@app.route('/')
def public_page(): 
	return 'Public page'

@app.route('/private')
@login_required
def private_page():
	print(current_user.is_authenticated)

	return 'Private page'

if __name__ == '__main__': 
	app.run(debug=True)


