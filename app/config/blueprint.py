from ..controllers import keys

def init_blueprints(app):
    app.register_blueprint(keys.bp)
