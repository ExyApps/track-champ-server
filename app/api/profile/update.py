from . import profile_bp
import base64, os
from flask import request, jsonify, g
from http import HTTPStatus

from app.database.wrapper import authentication

from app.database.enums.GenderEnum import match_gender

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

    image_path = f'files/profile_images/user{g.user_id}.png'
    if profile_image is not None:
        img_type, content = profile_image.split(',')
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(payload['profile_image']))
        payload['profile_image'] = f'files/profile_images/user{g.user_id}.png'
    else:
        if os.path.exists(image_path):
            os.remove(image_path)

    authentication.update_user(g.user_id, payload)
    user = authentication.get_user(g.user_id)

    info = user.to_json()

    return jsonify({ 'success': True, 'info': info }), HTTPStatus.OK
