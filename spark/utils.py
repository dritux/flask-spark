from functools import wraps

from werkzeug.exceptions import Unauthorized, UnsupportedMediaType
from itsdangerous import BadSignature

from . import app

from flask import g, request

def requires_json(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.mimetype not in ('application/json',):
            raise UnsupportedMediaType(
                "You must send a raw body in JSON format with the Content-Type"
                " header properly set to application/json.")

        return f(*args, **kwargs)

    return decorated
def requires_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth:
            raise Unauthorized("API key required.")
        auth = auth.split()

        try:
            auth_params = dict([a.strip(',').split('=', 1) for a in auth[0:]])
        except ValueError:
            raise Unauthorized('Invalid authorization scheme.')

        apikey = auth_params.get('apikey', '').strip('"')
        if not apikey:
            raise Unauthorized("API key required.")

        try:
            profile = app.signer.unsign(apikey)
        except BadSignature:
            raise Unauthorized("Invalid API key.")

        g.profile = profile
        g.apikey = apikey

        return f(*args, **kwargs)

    return decorated