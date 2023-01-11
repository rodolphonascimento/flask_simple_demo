from flask import Blueprint

providers = Blueprint("providers", __name__)

from . import views