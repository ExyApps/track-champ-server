import os
from flask import Flask
from config import Config
from app.database.models import *

from app.endpoint_wrappers.context import setup_body_verification
from app.endpoint_wrappers.context import setup_context
from app.endpoint_wrappers.logging import setup_logs

from app.api.auth import auth_bp

NEEDED_PATHS = [
    'files',
    'files/profile_images'
]

def create_app(config_class=Config): # Function to create the app with a configurable config class
    app = Flask(__name__)
    app.config.from_object(config_class)

    if not config_class.TESTING:
        for path in NEEDED_PATHS:
            if not os.path.exists(path):
                os.mkdir(path)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix='/auth')

    setup_context(app)
    setup_logs(app)
    # setup_body_verification(app)

    return app