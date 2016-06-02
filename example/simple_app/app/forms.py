from wtforms import Form, StringField 
from wtforms.validators import Required

from flask_email_auth.default.forms import RegisterFormMixin 
from flask_email_auth.forms import ModelField

class RegisterForm(RegisterFormMixin):
	first_name = ModelField('first_name', StringField('Имя',     [Required()]))
	last_name  = ModelField('last_name',  StringField('Фамилия', [Required()]))