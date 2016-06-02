BASE_URL = 'localhost:5000'

SQLALCHEMY_DATABASE_URI = "sqlite:///./app.db"
EAUTH_USER_MODEL = 'app.models.User'
EAUTH_ENABLE_EMAIL_CONFIRM = False
EAUTH_ON_FINISH = {
	'register': '/'
}

ENABLE_CSRF = True
SECRET_KEY = 'some_secret'
SQLALCHEMY_TRACK_MODIFICATIONS = True
