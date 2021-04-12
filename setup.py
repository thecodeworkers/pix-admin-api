from dotenv import dotenv_values
from app.config.keys import create_application_token
import secrets

if __name__ == '__main__':
    ENDC = '\033[0m'
    OKGREEN = '\033[92m'

    def _generate_keys():
        key = secrets.token_urlsafe(32)
        secret_key = secrets.token_urlsafe(40)
        app_token = create_application_token(key, secret_key)

        print('')
        print(f' APP_KEY: {OKGREEN}{key}{ENDC}')
        print(f' APP_SECRET: {OKGREEN}{secret_key}{ENDC}')
        print(f' APP_TOKEN: {OKGREEN}{app_token}{ENDC}')
        print('\n\033[94m APP_KEY and APP_SECRET must go in the .env')
        print(f' APP_TOKEN must be in request header as X-API-Key{ENDC}')
        print('')

    def _input_asked(prompt=''):
        while True:
            try:
                n = int(input(prompt))
                if n < 0 or n > 1: raise ValueError
                break

            except ValueError:
                print(f'\n \033[91mInvalid choice! Enter 0 or 1.{ENDC}')
                prompt = '\n Do you want to generate the keys? '

        return n

    print(f'\033[96m\n You are about to create the keys for the application, this program will generate three keys, two of them must be placed in the app .env and another must be used to make requests to the api \n{ENDC}')
    print(f""" {OKGREEN}1) Generate Keys{ENDC} \n 0) Exit \n""")
    choice = _input_asked(' What\'s is your choice: ')

    if not choice:
        print('')
        quit()

    if choice:
        _generate_keys()
