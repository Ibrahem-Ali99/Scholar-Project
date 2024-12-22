from functools import wraps
from flask import session, jsonify

def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = session.get('role')
            if not user_role or user_role not in allowed_roles:
                return jsonify({"error": "Unauthorized access"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
