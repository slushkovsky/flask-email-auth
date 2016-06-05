SQLALCHEMY_TRACK_MODIFICATIONS = True

EAUTH_FORM_REGISTER      = 'flask_email_auth.default.forms.RegisterFormMixin'
EAUTH_FORM_LOGIN         = 'flask_email_auth.default.forms.LoginForm'
EAUTH_FORM_RESET_PASS    = 'flask_email_auth.default.forms.ResetPasswordForm'
EAUTH_FORM_REQUEST_RESET = 'flask_email_auth.default.forms.ForgotPasswordForm'

EAUTH_TEMPLATE_REGISTER      = ('eauth_mixins/register.html',        {})
EAUTH_TEMPLATE_LOGIN         = ('eauth_mixins/login.html',           {})
EAUTH_TEMPLATE_RESET_PASS    = ('eauth_mixins/reset_pass.html',      {})
EAUTH_TEMPLATE_REQUEST_RESET = ('eauth_mixins/forgot_password.html', {}) 

EAUTH_MAIL_CONFIRM_SUBJECT = 'Подтверждение регистрации'
EAUTH_MAIL_RESET_SUBJECT   = 'Восстановление пароля'

EAUTH_MAIL_CONFIRM_TEMPLATE = 'eauth_mixins/post/confirm_email.html'
EAUTH_MAIL_RESET_TEMPLATE   = 'eauth_mixins/post/reset_pass.html'

EAUTH_ON_FINISH_LOGOUT = '/login'
EAUTH_ON_FINISH_REGISTER = '/login'
EAUTH_ON_FINISH_REQUEST_RESET = '/login'

EAUTH_DEFUALT_NEXT_URL = None
EAUTH_ON_RESET_UNKNOWN_EMAIL = None
EAUTH_LOGOUT_REDIRECT_URL = None