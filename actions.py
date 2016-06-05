import sqlalchemy.orm.exc

from .models import UserEmailAuth, ConfirmEmailMessage, ResetPasswordMessage, \
    new_user, _new_model
from .exc import LoginFailError, WrongTokenError, InvalidUserIdError, \
    UnknownEmailError


def register_new_user(model_kw, with_confirm=True, next_url=None):
    global_user = new_user(model_kw)
    user = UserEmailAuth(global_user.id, model_kw['email'], 
                                     model_kw['password'])
    UserEmailAuth._add(user)

    if with_confirm:
        ConfirmEmailMessage._new(user_id=user.id, next=next_url, autosend=True)


def check_user(model_kw):
    try:
        user = UserEmailAuth.query().filter_by(email=model_kw['email']).one()

        if not user.check_password(model_kw['password']):
            raise LoginFailError()

        return user

    except sqlalchemy.orm.exc.NoResultFound:
        raise LoginFailError()


def request_pass_reset(email):
    try:
        user = UserEmailAuth.query().filter_by(email=email).one()
    except sqlalchemy.orm.exc.NoResultFound:
        raise UnknownUserEmailError()

    ForgotPasswordMessage._new(user_id=user.id, autosend=True)


def __get_msg_by_token(token, model):
    try:
        return model.query().filter_by(token=token).one()
    except sqlalchemy.orm.exc.NoResultFound:
        raise WrongTokenError()


def get_confirm_msg(token):
    return __get_msg_by_token(token, ConfirmEmailMessage)


def get_reset_msg(token):
    return __get_msg_by_token(token, ResetPasswordMessage)


def __get_user_by_msg(msg):
    try:
        return UserEmailAuth.query().filter_by(id=msg.user_id).one()
    except sqlalchemy.orm.exc.NoResultFound:
        raise InvalidUserId()


def confirm_user(msg_token):
    msg = get_confirm_msg(msg_token)
    user = __get_user_by_msg(msg)

    user.confirmed = True

    msg._delete(msg)

    return msg.next


def reset_password_by_msg(msg, new_password):
    user = get_user_by_msg(msg)
    user.reset_password(new_password)

    db.delete(msg)

    return msg.next
