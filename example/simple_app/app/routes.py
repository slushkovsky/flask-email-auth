from flask.ext.login import login_required, current_user

from app import app

@app.route('/')
def public_page(): 
	return 'Public page'

@app.route('/private')
@login_required
def private_page():
	print(current_user.is_authenticated)

	return 'Private page'