from flask import jsonify
from http import HTTPStatus

from extension import app, db

from app.api.auth import auth_bp
from app.api.profile import profile_bp
from app.logging.setup import setup_login

setup_login(app)

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


@app.errorhandler
def handle_error(e):
	"""
	Catch any error that was not desired
	"""
	app.logger.exception('An unhandled exception occured')

	return jsonify({
		'message': 'Algo inesperado aconteceu, pedimos desculpa pelo incómodo'
	}), HTTPStatus.INTERNAL_SERVER_ERROR


# INITIALIZE
with app.app_context():
	db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')

if __name__ == "__main__":
	app.run()