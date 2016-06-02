BASE_URL = 'localhost'

EAUTH_USER_MODEL = 'models.User'
EAUTH_ENABLE_EMAIL_CONFIRM = False
EAUTH_ON_FINISH = {
	'register': '/'
}

ENABLE_CSRF = True
SECRET_KEY = 'some_secret'
SQLALCHEMY_TRACK_MODIFICATIONS = True
