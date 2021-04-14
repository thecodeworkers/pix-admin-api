from .colors import *

def input_asked(prompt, message, limit=1):
    while True:
        try:
            n = int(input(prompt))
            if n < 0 or n > limit: raise ValueError
            break

        except ValueError:
            __generate_text_inputs(limit)
            print(f'\n {FAIL}Invalid choice! Enter 0{__generate_text_inputs(limit)}.{ENDC}')
            prompt = f'\n {message} '

    return n

def __generate_text_inputs(limit):
    text_numbers = ''

    for _ in range(limit):
        current_limit = _ + 1
        if current_limit == limit:
            text_numbers += f' or {current_limit}'
        else:
            text_numbers += f', {current_limit}'

    return text_numbers
