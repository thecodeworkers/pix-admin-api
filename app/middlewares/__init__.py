from .verify_token import verify_app_token, verify_user_token

middlewares = {
    'auth': [
        verify_app_token
    ],
    'user': [
        verify_app_token,
        verify_user_token
    ],
    'role': [
        verify_app_token,
        verify_user_token
    ],
    'permission': [
        verify_app_token,
        verify_user_token
    ],
    'currency': [
        verify_app_token,
        verify_user_token
    ],
    'language': [
        verify_app_token,
        verify_user_token
    ]
}
