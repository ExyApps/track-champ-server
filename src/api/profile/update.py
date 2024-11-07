from . import profile_bp
import base64, os
from flask import request, jsonify, g
from http import HTTPStatus

from src.database.wrapper import authentication

from src.database.enums.GenderEnum import match_gender

@profile_bp.route('/update', methods=['POST'])
def update():
    """
    Update the profile
    """
    if not g.user_id:
        return {'success': False, 'detail': 'Não tem uma sessão iniciada'}, HTTPStatus.TEMPORARY_REDIRECT

    payload = request.json

    if 'gender' in payload:
        payload['gender'] = match_gender(payload['gender'])

    profile_image = payload['profile_image']

    image_path = f'static/images/user_{g.user_id}.png'
    if profile_image is not None:
        img_type, _ = profile_image.split(',')
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(payload['profile_image']))
        payload['profile_image'] = image_path
    else:
        if os.path.exists(image_path):
            os.remove(image_path)

    authentication.update_user(g.user_id, payload, image_path if profile_image else None)
    user = authentication.get_user(g.user_id)

    info = user.to_json()

    return jsonify({ 'success': True, 'info': info }), HTTPStatus.OK
