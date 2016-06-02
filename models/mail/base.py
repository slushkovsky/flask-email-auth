import random
from flask_mail import Message
from flask import render_template, current_app
from sqlalchemy import Column, Integer, String, ForeignKey

from .. import _AppSession
from ..orm import SQLAlchemyMixin
from ..user import UserEmailAuth

MESSAGE_TOKEN_LENGTH = 32

class PostMessage(_AppSession, SQLAlchemyMixin):
    __tablename__ = 'post_messages'

    id       = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey(UserEmailAuth.id))
    type     = Column(String(32))
    next     = Column(String(64))

    __mapper_args__ = {'polymorphic_on': type}

    def __init__(autosend=False, *args, **kwars):
        super().__init__(*args, **kwargs)
        self.token = self.gen_unique_token()

        if autosend: 
            email = UserEmailAuth.query.filter_by(id=self.user_id).one().email
            self.send([email])

    def send(self, recepients): 
        self.send_message(recepients)

    @classmethod
    def get_subject(cls): 
        raise NotImplementedError()

    def get_template(self): 
        raise NotImplementedError()

    @classmethod
    def get_html(cls, **kw): 
        return render_template(cls.get_template(), **kw)


    @classmethod 
    def send_message(cls, recepients, **msg_kw): 
        Message(cls.get_subject(), recepients=recepients,  
            html=cls.get_html(**msg_kw)).send()

    @classmethod
    def setting(name, general=False): 
        return current_app.config[name if general else setting_name(name)]

    @classmethod
    def get_hostname(cls): 
        return cls.setting('BASE_URL', general=True)

      
class TokenedPostMessage(PostMessage):
    token = Column(String(MESSAGE_TOKEN_LENGTH), unique=True, index=True)

    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = gen_unique_token()

    def send(self, recepients):
        self.send_message(recepients, link=self.get_link())

    def get_link(self): 
        raise NotImplementedError()

    @classmethod
    def gen_unique_token(cls): 
        while True:
            token = cls.gen_token() 
            
            if cls.query.filter_by(token=token) is None: 
                return token

    @classmethod
    def gen_token(cls):
        choices = string.ascii_uppercase + string.digits
        return ''.join(random.choice(choices) for _ in range(cls.MESSAGE_TOKEN_LENGTH))