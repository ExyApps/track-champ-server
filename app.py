import os
from flask import jsonify
from http import HTTPStatus
from dotenv import load_dotenv

from config import Config, TestConfig

from src.initializer import create_app

load_dotenv()

if os.environ.get('FLASK_ENV') == 'development':
    app = create_app(config_class=TestConfig)
else:
    app = create_app()

# app.run()
