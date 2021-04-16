from ..controllers.users import auth, user

def init_blueprints(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
