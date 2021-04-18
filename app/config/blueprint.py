from ..controllers.users import auth, user, role, permission
from ..controllers.resources import currency, language, country

def init_blueprints(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)
    app.register_blueprint(permission.bp)
    app.register_blueprint(currency.bp)
    app.register_blueprint(language.bp)
    app.register_blueprint(country.bp)
