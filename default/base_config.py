SQLALCHEMY_TRACK_MODIFICATIONS = True

EAUTH_FORMS = {
	'register':      'email_auth.default.forms.RegisterForm', 
	'login':         'email_auth.default.forms.LoginForm',
	'reset_pass':    'email_auth.default.forms.ResetPasswordForm',
	'request_reset': 'email_auth.default.forms.ForgotPasswordForm'
} 

EAUTH_TEMPLATES = {
	'register':   ('register.html',    {}), 
	'login':      ('login.html',           {}), 
	'reset_pass': ('reset_password.html',  {}),
	'req_reset':  ('forgot_password.html', {})
}

EAUTH_MAIL_CONFIRM_SUBJECT = 'Подтверждение регистрации'
EAUTH_MAIL_RESET_SUBJECT   = 'Восстановление пароля'

EAUTH_MAIL_CONFIRM_TEMPLATE = 'post/confirm_email.html'
EAUTH_MAIL_RESET_TEMPLATE   = 'post/reset_pass.html'

EAUTH_ON_FINISH = {
	'register': None,
	'request_reset': None
}

EAUTH_DEFUALT_NEXT_URL = None
EAUTH_ON_RESET_UNKNOWN_EMAIL = None
EAUTH_LOGOUT_REDIRECT_URL = None