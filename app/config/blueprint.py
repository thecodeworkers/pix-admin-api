from ..controllers.users import auth, user, role

def init_blueprints(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)
