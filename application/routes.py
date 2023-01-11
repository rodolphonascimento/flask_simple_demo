from application.providers import providers as providers_blueprint


def init_routes(app):
    app.register_blueprint(providers_blueprint)
