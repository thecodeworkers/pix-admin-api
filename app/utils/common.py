from flask import abort

response = lambda result='': {'result': result}

def api_abort(code, error):
    abort(code, {'message': str(error)})
