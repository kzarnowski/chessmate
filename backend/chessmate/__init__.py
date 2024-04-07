import os
from flask import Flask
from .config import config

def create_app(config_mode):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_mode])

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .models.base import db
    db.init_app(app)

    from .views.auth import auth_bp
    app.register_blueprint(auth_bp)

    from .views.tournament import tournament_bp
    app.register_blueprint(tournament_bp)
    
    return app