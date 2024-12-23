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
    image_path = f'static/images/user_{g.user_id}'

    # Delete previous images
    if profile_image is None:
        for type in ['jpg', 'png', 'jpeg']:
            if os.path.exists(f'{image_path}.{type}'):
                os.remove(f'{image_path}.{type}')

    elif '/static/images/' not in profile_image:
        img_type, content = profile_image.split(',')
        image_path += '.' + img_type.split(';')[0].split('/')[1]
        with open(image_path, "wb") as fh:
            fh.write(base64.b64decode(content))
        payload['profile_image'] = f'/{image_path}'

    authentication.update_user(g.user_id, payload)
    user = authentication.get_user(g.user_id)

    info = user.to_json()

    return jsonify({ 'success': True, 'info': info }), HTTPStatus.OK
