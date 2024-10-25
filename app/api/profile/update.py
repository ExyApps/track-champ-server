from . import profile_bp
import base64, os, re
from flask import request, jsonify
from http import HTTPStatus

from app.database.wrapper import authentication
from app.validator.validator import Validator

from app.database.models.GenderEnum import match_gender

@profile_bp.route('/update', methods=['POST'])
def update():
    """
    Update the profile
    """
    payload = request.json

    for k, v in payload.items():
        if k in ['id', 'profileImage']: continue
        snake_case_key = re.sub(r'(?<!^)(?=[A-Z])', '_', k).lower()
        verifier = getattr(Validator, snake_case_key)
        valid, message = verifier(v)

        if not valid:
            return { 'error': message, 'field': k }, HTTPStatus.BAD_REQUEST
        
    if 'gender' in payload:
        payload['gender'] = match_gender(payload['gender'])
		
    profile_image = payload['profileImage']

    image_path = f'files/profile_images/user{payload["id"]}.png'
    if profile_image is not None:
        img_type, content = profile_image.split(',')
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(payload['profileImage']))
        payload['profileImage'] = f'files/profile_images/user{payload["id"]}.png'
    else:
        if os.path.exists(image_path):
            os.remove(image_path)

    authentication.update_user(payload)
    user = authentication.get_user(payload['id'])
	
    info = user.to_json()

    return jsonify({ 'success': True, 'info': info }), HTTPStatus.OK