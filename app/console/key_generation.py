from ..config.keys import create_application_token
from .colors import *
from .default_ask import input_asked
import secrets

def key_generation_program():
    print(f'\033[96m\n You are about to create the keys for the application, this program will generate three keys, two of them must be placed in the app .env and another must be used to make requests to the api \n{ENDC}')
    print(f""" {OKGREEN}1) Generate Keys{ENDC} \n 0) Exit \n""")
    choice = input_asked(' What\'s is your choice: ', 'Do you want to generate the keys?')

    if not choice:
        print('')
        quit()

    if choice:
        __generate_keys()

def __generate_keys():
    key = secrets.token_urlsafe(32)
    secret_key = secrets.token_urlsafe(40)
    app_token = create_application_token(key, secret_key)

    print('')
    print(f' APP_KEY: {OKGREEN}{key}{ENDC}')
    print(f' APP_SECRET: {OKGREEN}{secret_key}{ENDC}')
    print(f' APP_TOKEN: {OKGREEN}{app_token}{ENDC}')
    print('\n\033[94m APP_KEY and APP_SECRET must go in the .env')
    print(f' APP_TOKEN must be in request header as x-api-key{ENDC}')
    print('')
