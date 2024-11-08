import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import ProdConfig
from src.database.models import *
from http import HTTPStatus

from src.endpoint_wrappers.context import setup_body_verification
from src.endpoint_wrappers.context import setup_context
from src.endpoint_wrappers.logging import setup_logs

from src.api.auth import auth_bp
from src.api.profile import profile_bp
from src.api.team import team_bp
from src.api.test import test_bp

NEEDED_PATHS = [
    'static',
    'static/images'
]

def create_app(config_class=ProdConfig): # Function to create the app with a configurable config class
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ProdConfig.PROJECT_PATH_JOINER))

    app = Flask(
        __name__,
        static_folder=os.path.join(project_root, 'static'),       # Absolute path to the static folder
        static_url_path='/static',                                 # URL prefix for static files
    )

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
        return 'v0.6.4'
    
    @app.route('/favicon.ico')
    def favicon():
        return '', 204
    
    # ERROR HANDLING
    @app.errorhandler(KeyError)
    def handle_key_error(e):
        """
        Catch the error if there is a required field missing in the request
        """
        app.logger.exception('An unhandled KeyError exception occured')

        return jsonify({
            'message': 'Pedido inválido, confirme que envia toda a informação necessária'
        }), HTTPStatus.BAD_REQUEST


    @app.errorhandler(Exception)
    def handle_error(e):
        """
        Catch any error that was not desired
        """
        app.logger.exception('An unhandled exception occured')

        return jsonify({
            'message': 'Algo inesperado aconteceu, pedimos desculpa pelo incómodo'
        }), HTTPStatus.INTERNAL_SERVER_ERROR

    return app