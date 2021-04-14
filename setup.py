from app.database import MigrateDatabase
from app.console import *

if __name__ == '__main__':
    try:
        print(f""" {OKGREEN}1) Key Generation{ENDC} \n {OKGREEN}2) Migrate Database{ENDC} \n 0) Exit \n""")
        option_text = 'Select a option:'
        choice = input_asked(f' {option_text} ', option_text, 2)

        if not choice:
            print('')
            quit()

        if choice == 1:
            key_generation_program()

        if choice == 2:
            print('')
            MigrateDatabase()
            print('')

    except Exception as e:
        print(f'\n {FAIL}Error occurred.{ENDC}')
        print(f' {FAIL}{e}{ENDC}')
        print('')
    except KeyboardInterrupt:
        print('\n')
        pass
