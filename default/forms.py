from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, DateField, SelectField, \
                    SubmitField, FormField
from wtforms.validators import Required, Email, EqualTo, InputRequired

from ..forms import ModelForm, ModelField, EmailField, ConfirmedPasswordForm

# ConfirmPasswordField = FormField(ConfirmedPasswordForm)

class LoginForm(ModelForm): 
    email    = ModelField('email',    EmailField   ,('Почта',  [Required()]))
    password = ModelField('password', PasswordField,('Пароль', [Required()]))
    
    submit = SubmitField('Войти')


class RegisterForm(ModelForm): 
    password = ModelField('password', PasswordField, ('Пароль', [Required(), EqualTo('confirm')]))
    confirm  = PasswordField('Подтверждение', [Required()])
    email    = ModelField('email',    EmailField, ('Электронная почта',  [Required()]))
    
    submit = SubmitField('Далее')


class ResetPasswordForm(Form): 
    password = FormField(ConfirmedPasswordForm, [Required()])

    submit = SubmitField('Далее')

class ForgotPasswordForm(Form): 
    email = EmailField('Почта', [Required()])

