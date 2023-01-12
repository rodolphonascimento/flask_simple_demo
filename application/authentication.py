
from flask_jwt import JWT
from application.models import User

__jwt: JWT

def create_jwt(app)-> JWT:
    __jwt = JWT(app, autehticate, identity)
    
def identity(payload):
    data = payload['identity']
    return data
    
def autehticate(username, password):
    if username=="scott" and password=="cat":
        user = User(123, username, password)
        return user
    
    
    
def get_jwt()-> JWT:
    return __jwt