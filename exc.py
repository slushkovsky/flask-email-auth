from functools import wraps

class HttpException(Exception):
    def http(self):
        return (self.msg, self.code)

class WrongTokenError   (HttpException): code = 500; msg = 'Invalid token'
class InvalidUserIdError(HttpException): code = 500; msg = 'Invalid user id'
class LoginFailError    (HttpException): code = 401; msg = 'Invalid email/password'
class UnknownEmailError (HttpException): code = 404; msg = 'No user with such email'


def except_errors(f): 
    @wraps(f)
    def wrapper(*args, **kwargs): 
        try: 
            return f(*args, **kwargs)
        except HttpException as e:
            return e.http() 
    return wrapper

