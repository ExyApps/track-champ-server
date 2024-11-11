import os
from flask import jsonify
from dotenv import load_dotenv

from config import DevConfig

from src.initializer import create_app

load_dotenv()

if os.environ.get('FLASK_ENV') == 'development':
    app = create_app(config_class=DevConfig)
else:
    app = create_app()

# app.run()
