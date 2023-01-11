from . import providers
from flask import Flask, flash, request, redirect, session





@providers.route('/api/providers/insert/', methods=["POST"])
def insert():
    request.data
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