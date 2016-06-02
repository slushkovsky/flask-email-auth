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


class ModelField(Field): 
    def __init__(self, model_col, field, field_args):
        super().__init__(*field_args)
        self.model_col = model_col

    def __new__(cls, model_col, field, *args, **kwargs):
        return super().__new__(field)


class ModelForm(Form): 
    def __init__(self, model, form_values):
        super().__init__(form_values)
        self.model = model

    # def __new__(cls, *args, **kwargs): 
        # return super().__new__(Form)

    def exec_db(self, query): 
        return query(self.collect_model())

    def collect_model(self):
        model_kwargs = {}

        for field_name, data in self.data:
            field = getattr(field_name, self)

            if ModelFiled in field.__bases__: 
                model_kwargs[field.model_field] = data

        return self.model(**model_kwargs)
