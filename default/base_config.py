SQLALCHEMY_TRACK_MODIFICATIONS = True

EAUTH_FORM_REGISTER      = 'flask_email_auth.default.forms.RegisterFormMixin'
EAUTH_FORM_LOGIN         = 'flask_email_auth.default.forms.LoginForm'
EAUTH_FORM_RESET_PASS    = 'flask_email_auth.default.forms.ResetPasswordForm'
EAUTH_FORM_REQUEST_RESET = 'flask_email_auth.default.forms.ForgotPasswordForm'

EAUTH_TEMPLATE_REGISTER      = ('register.html',        {})
EAUTH_TEMPLATE_LOGIN         = ('login.html',           {})
EAUTH_TEMPLATE_RESET_PASS    = ('reset_pass.html',      {})
EAUTH_TEMPLATE_REQUEST_RESET = ('forgot_password.html', {}) 

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