from sqlalchemy import Column, ForeignKey
from flask import url_for

from .base import TokenedPostMessage

class ConfirmEmailMessage(TokenedPostMessage): 
    __tablename__ = 'post_email_confirms'
    __mapper_args__ = {'polymorphic_identity': 'confirm_email'}

    id = Column(None, ForeignKey(TokenedPostMessage.id), primary_key=True)

    def get_link(self):
        return self.get_hostname() + url_for('confirm_email', token=self.token)

    @classmethod
    def get_subject(cls): 
        return cls.setting('MAIL_CONFIRM_SUBJECT')

    @classmethod
    def get_template(cls): 
        return cls.setting('MAIL_CONFIRM_TEMPLATE')


    
class ResetPasswordMessage(TokenedPostMessage): 
    __tablename__ = 'post_reset_passwords'
    __mapper_args__ = {'polymorphic_identity': 'reset_password'}

    id = Column(None, ForeignKey(TokenedPostMessage.id), primary_key=True)

    def get_link(self): 
        return self.get_hostname() + url_for('reset_password', token=self.token)

    @classmethod
    def get_subject(cls): 
        return cls.setting('MAIL_RESET_SUBJECT')

    @classmethod
    def get_template(cls): 
        return cls.setting('MAIL_RESET_TEMPLATE')