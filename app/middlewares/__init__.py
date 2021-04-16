from .verify_token import verify_app_token

middlewares = {
    'auth': [verify_app_token],
    'user': [verify_app_token],
    'role': [verify_app_token],
    'permission': [verify_app_token],
    'currency': [verify_app_token],
    'language': [verify_app_token]
}
