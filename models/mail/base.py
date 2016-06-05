import random
import string
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

    def __init__(self, autosend=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if autosend: 
            email = UserEmailAuth.query().filter_by(id=self.user_id).one().email
            self.send([email])

    def send(self, recipients): 
        self.send_message(recipients)

    @classmethod
    def get_subject(cls): 
        raise NotImplementedError()

    def get_template(self): 
        raise NotImplementedError()

    @classmethod
    def get_html(cls, **kw): 
        return render_template(cls.get_template(), **kw)


    @classmethod 
    def send_message(cls, recipients, **msg_kw): 
        current_app.mailer.send(Message(cls.get_subject(), 
                                        recipients=recipients,  
                                        html=cls.get_html(**msg_kw)))


    @classmethod
    def get_hostname(cls): 
        return cls.setting('BASE_URL', general=True)

      
class TokenedPostMessage(PostMessage):
    token = Column(String(MESSAGE_TOKEN_LENGTH), unique=True, index=True)

    def __init__(self, *args, **kwargs):
        self.token = self.gen_unique_token()
        super().__init__(*args, **kwargs)

    def send(self, recipients):
        self.send_message(recipients, link=self.get_link())

    def get_link(self): 
        raise NotImplementedError()

    @classmethod
    def gen_unique_token(cls): 
        while True:
            token = cls.gen_token() 
            
            if cls.query().filter_by(token=token).count() == 0: 
                return token

    @classmethod
    def gen_token(cls):
        choices = string.ascii_uppercase + string.digits
        return ''.join(random.choice(choices) for _ in range(MESSAGE_TOKEN_LENGTH))