from flask import Blueprint, redirect, request, render_template, current_app
from flask.ext.login import login_required

from .utils import module_member, filter_config, setting_name
from .exc import except_errors
from .models import UserEmailAuth
from .actions import register_new_user, check_user, request_pass_reset, \
                     confirm_user, reset_password_by_msg, get_reset_msg


bp = Blueprint('email_auth', __name__)



def render_config_template(name, **kwargs):
    template_config = current_app.config[setting_name('TEMPLATES')][name]
    all_kw = template_config[1].copy()
    all_kw.update(kwargs)

    return render_template(template_config[0], **all_kw)


@bp.before_request
def set_config():
    bp.config = filter_config(current_app.config)

    global ResisterForm
    global LoginForm
    global ReqResetForm
    global ReqResetForm

    ResisterForm  = module_member(bp.config['FORMS']['register'])
    LoginForm     = module_member(bp.config['FORMS']['login'])
    ReqResetForm  = module_member(bp.config['FORMS']['request_reset'])
    ResetPassForm = module_member(bp.config['FORMS']['reset_pass'])

@bp.route('/register', methods=['GET', 'POST'])
@except_errors
def register():
    form = ResisterForm(UserEmailAuth, request.form)

    if form.validate_on_submit():
        print('OK')
        user = form.exec_db(lambda user: register_new_user(user, 
            with_confirm=bp.config['ENABLE_EMAIL_CONFIRM'],
            next_url=request.args.get('next', bp.config['DEFAULT_AUTH_NEXT'])))

        return redirect(bp.config['ON_FINISH']['register'])

    print('NOT OK')
    print(form.errors)

    return render_config_template('register', form=form)


@bp.route('/login', methods=['GET', 'POST'])
@except_errors
def login(): 
    form = LoginForm(UserEmailAuth, request.form)

    if form.validate_on_submit(): 
        form.exec_db(check_user)
        login_user(user)
        return redirect(request.args.get('next', bp.config['DEFAULT_AUTH_NEXT']))

    return render_config_template('login', form=form)


@bp.route('/forgot_password', methods=['POST'])
@except_errors
def forgot_password(): 
    form = ReqResetForm(request.form)

    if form.validate_on_submit():
        request_pass_reset(form.email.data)
        return redirect(bp.config['ON_FINISH']['request_reset'])

    return render_template('request_reset', form=form)
  

@bp.route('/logout')
@except_errors
def logout():
    logout_user()

    return redirect(bp.config['ON_FINISH']['logout'])


@bp.route('/confirm_email/<token>')
@except_errors
def confirm_email(token):
    return redirect(confirm_user(token))


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
@except_errors
def reset_password(token):
    form = ResetPassForm(request.form)
    msg = get_reset_msg(token)

    if form.validate_on_submit(): 
        return redirect(reset_password_by_msg(msg, form.passwrod.data))

    return render_config_template('reset_pass', form=form)