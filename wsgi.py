import os
from flask import jsonify
from http import HTTPStatus

from config import Config, TestConfig

from app.initializer import create_app

if __name__ == "__main__":
    if os.environ.get('FLASK_ENV') == 'development':
        app = create_app(config_class=TestConfig)
    else:
        app = create_app()

    # ERROR HANDLING
    # @app.errorhandler(KeyError)
    # def handle_key_error(e):
    #     """
    #     Catch the error if there is a required field missing in the request
    #     """
    #     app.logger.exception('An unhandled KeyError exception occured')

    #     return jsonify({
    #         'message': 'Pedido inválido, confirme que envia toda a informação necessária'
    #     }), HTTPStatus.BAD_REQUEST


    # @app.errorhandler(Exception)
    # def handle_error(e):
    #     """
    #     Catch any error that was not desired
    #     """
    #     app.logger.exception('An unhandled exception occured')

    #     return jsonify({
    #         'message': 'Algo inesperado aconteceu, pedimos desculpa pelo incómodo'
    #     }), HTTPStatus.INTERNAL_SERVER_ERROR

    app.run()
