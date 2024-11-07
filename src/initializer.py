import os
from flask import Flask
from flask_cors import CORS
from config import Config
from src.database.models import *

from src.endpoint_wrappers.context import setup_body_verification
from src.endpoint_wrappers.context import setup_context
from src.endpoint_wrappers.logging import setup_logs

from src.api.auth import auth_bp
from src.api.profile import profile_bp
from src.api.team import team_bp
from src.api.test import test_bp

NEEDED_PATHS = [
    'files',
    'files/profile_images'
]

def create_app(config_class=Config): # Function to create the app with a configurable config class
    app = Flask(__name__)
    CORS(
        app,
        supports_credentials=True
    )
    app.config.from_object(config_class)

    if not config_class.TESTING:
        for path in NEEDED_PATHS:
            if not os.path.exists(path):
                os.mkdir(path)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(team_bp, url_prefix='/team')
    app.register_blueprint(test_bp, url_prefix='/test')

    setup_context(app)
    setup_logs(app)
    setup_body_verification(app)

    @app.route('/', methods=['GET'])
    def home():
        return 'v0.2.2'

    return app