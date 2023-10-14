
from functools import wraps

from flask_jwt_extended import get_jwt

def roles_required(user_role):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                claims = get_jwt()  # You need to define the get_jwt() function to get JWT claims  # noqa: E501
                role = claims["role"]
                if role == user_role:
                    return fn(*args, **kwargs)
                else:
                    return {'message': 'Access denied. Unauthorized User.'}, 403
            return wrapper
        return decorator
    