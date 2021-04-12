from ..controllers import auth

def init_blueprints(app):
    app.register_blueprint(auth.bp)
