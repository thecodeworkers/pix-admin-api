from flask import abort

response = lambda result='': {'result': result}

def api_abort(code, error):
    abort(code, {'message': str(error)})

def success_operation(service, method, data):
    details = data['id'] if 'id' in data else ''
    return {
        **__default_log_entry(service, method, details),
        'log_type': 'INFO',
        'response': response(data)
    }

def error_operation(service, method, code, error):
    return {
        **__default_log_entry(service, method, error),
        'log_type': 'ERROR',
        'error': {
            'code': code,
            'error': error
        }
    }

def __default_log_entry(*args):
    return {
        'service': args[0],
        'method': args[1],
        'details': str(args[2])
    }
