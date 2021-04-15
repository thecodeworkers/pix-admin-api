from flask.globals import session
from flask import request
from functools import wraps
from ..utils import api_abort
import time

def log_record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()

        total_time = f'{end-start:0.8f}'

        __save_log(
            r['log_type'],
            r['service'],
            r['method'],
            r['details'],
            total_time
        )

        if 'response' in r: return r['response']
        if 'error' in r: api_abort(**r['error'])

    return wrapper

def __save_log(log_type, service, method, details, time_execute):
    info = {
        'user': session['user'] if 'user' in session else '',
        'ip_address': request.remote_addr,
        'log_type': log_type,
        'service': service,
        'method': method,
        'details': details,
        'time_execute': time_execute
    }

    print(info)

    ## insert log in database
