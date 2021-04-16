from .verify_token import verify_app_token

middlewares = {
    'auth': [verify_app_token],
    'user': [verify_app_token],
    'role': [verify_app_token]
}
