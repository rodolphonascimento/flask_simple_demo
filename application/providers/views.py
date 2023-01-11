from . import providers
from flask import request, session
from application.models import Providers, get_database
import json




@providers.route('/api/providers/insert/', methods=["POST"])
def insert():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    
    provider = Providers()
    provider.name = "xx"
    db = get_database()
    db.session.add(provider)
    db.session.commit()
    
    pass


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