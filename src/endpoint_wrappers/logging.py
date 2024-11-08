import logging
import uuid
from flask import Flask, request, g

def setup_logs(app: Flask) -> None:
    """
    Setup the logging of the app

    Parameters:
        app (Flask): The app object
    """
    handler = logging.FileHandler('app.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Create a Formatter
    handler.setFormatter(formatter)  # Set the formatter for the handler
    app.logger.addHandler(handler)  # Add the handler to the app logger
    app.logger.setLevel(logging.DEBUG) # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)


    @app.before_request
    def log_request():
        """
        Record in the log file the important information regarding the request
        """
        request.id = uuid.uuid4()
        app.logger.info(f"""Request: {request.method} {request.path}
            ID: {request.id}
            Args: {request.args}
            Form: {request.form}
            JSON: {request.json if request.is_json else 'Not applicable'}
            User ID: {g.user_id}
            User ST: {g.session_token}
            Headers: {request.headers}"""
        )


    @app.after_request
    def log_response(response):
        """
        Record in the log file the important information regarding the response
        """

        app.logger.info(f"""Response: {response.status_code} {request.path}
            ID: {request.id}
            Data: {response.get_data().decode() if 'json' in response.headers['Content-Type'] else ''}"""
        )

        return response #Important to return the response