from .verify_token import *

middlewares = {
    'auth': [verify_app_token]
}
