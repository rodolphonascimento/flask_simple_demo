from . import providers
from flask import request, make_response, session
from application.models import Providers, get_database
import json




@providers.route('/api/providers/insert/', methods=["POST"])
def insert():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    
    try:
        provider = Providers()
        provider.id = data.get("id", "")
        provider.name = data.get("name", "")
        provider.company = data.get("company", "")
        provider.amount_products = data.get("amount_products", "")
        
        db = get_database()
        db.session.add(provider)
        db.session.commit()
        response = make_response("", 200)
        
    except Exception as e:
        response = make_response(e, 401)
        
    return response


@providers.route('/api/providers/update/', methods=["PUT"])
def update():
    request.data
    pass


@providers.route('/api/providers/list/', methods=["GET"])
def list():
    request.data
    pass


@providers.route('/api/providers/delete/', methods=["DELETE"])
def delete():
    request.data
    pass