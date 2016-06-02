from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, Field
from wtforms.validators import Required, EqualTo, Email

class ConfirmedPasswordForm(Form): 
    NOT_EQUAL_MSG = 'Пароли должны совпадать'

    password = PasswordField('Пароль', 
                             [
                                Required(), 
                                EqualTo('confirm', message=NOT_EQUAL_MSG)
                             ])

    confirm  = PasswordField('Подтверждение пароля', [Required()])

    def _value(self): 
        return self.password.data



class EmailField(StringField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(Email())



class ModelField(object): 
    def __new__(cls, model_col, field, *args, **kwargs):
        field.kwargs = {'description': 'model_field: {}'.format(model_col)} 
        return field


class ModelForm(Form): 
    def __init__(self, model, form_values):
        super().__init__(form_values)
        self.model = model

    def exec_db(self, f, *args, **kwargs): 
        return f(self.collect_model(), *args, **kwargs)

    def collect_model(self):
        model_kwargs = {}

        for field_name, data in self.data.items():
            field = getattr(self, field_name)
            descr = field.description
            model_field_attr = 'model_field:'

            if descr.startswith(model_field_attr):
                model_kwargs[descr.replace(model_field_attr, '').strip()] = data

        return model_kwargs
