from . import providers
from flask import request, make_response
from application.models import Providers, get_database
import json
from flask_jwt import jwt_required, current_identity


def __handle_error(exception):
    return make_response(f'Error trying to handle data. Message {str(exception)}' , 400)



@providers.route('/api/whois', methods=["GET"])
@jwt_required()
def protected():
    return '%s' % current_identity

@providers.route('/api/providers/insert/', methods=["POST"])
@jwt_required()
def insert():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    
    try:
        provider = Providers()
        provider.id = data.get("id", "")
        provider.name = data.get("name", "not informed")
        provider.company = data.get("company", "not informed")
        provider.amount_products = data.get("amount_products", 1)
        
        db = get_database()
        db.session.add(provider)
        db.session.commit()
        return make_response("Success", 201)
        
    except Exception as e:
        return __handle_error(e)
        
        

@providers.route('/api/providers/update/<id>', methods=["PUT"])
@jwt_required()
def update(id):
    data = request.data.decode("utf-8")
    data = json.loads(data)
    
    try:
        provider = Providers.query.filter_by(id=id).first()
        if provider == None:
            return make_response(f'Provider ID not found: {id}', 404)
        
        provider.name = data.get("name", provider.name )
        provider.company = data.get("company", provider.company)
        provider.amount_products = data.get("amount_products", provider.amount_products)
        
        db = get_database()
        db.session.commit()
        output =  Providers.serialize(provider)
        return make_response(output, 200)
        
    except Exception as e:
        return __handle_error(e)
    


@providers.route('/api/providers/list/<id>', methods=["GET"])
@providers.route('/api/providers/list/', methods=["GET"])
@jwt_required()
def list(id=None):
    try:
        db = get_database()
        if id != None:
            providers = db.session.execute(db.select(Providers).filter_by(id=id).order_by(Providers.name)).scalars()
        else:
            providers = db.session.execute(db.select(Providers).order_by(Providers.name)).scalars()
        
        output = [Providers.serialize(provider) for provider in providers]
        if len(output) == 0:
            return make_response(f'Provider ID not found: {id}', 404) 
        else:
            return make_response(output, 200)
        
    except Exception as e:
        return __handle_error(e)



@providers.route('/api/providers/delete/<id>', methods=["DELETE"])
@jwt_required()
def delete(id):
    try:
        provider = Providers.query.filter_by(id=id).first()
        if provider == None:
            return make_response(f'Provider ID not found: {id}', 404)        
       
        db = get_database()
        db.session.delete(provider)
        db.session.commit()
        return make_response("", 200)
        
    except Exception as e:
        return __handle_error(e)