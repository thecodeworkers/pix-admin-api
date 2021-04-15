from flask import request
from functools import wraps
import time

def log_record(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()

        __save_log(
            r['user_id'],
            r['log_type'],
            r['service'],
            r['method'],
            r['details'],
            end - start
        )

        return r['response']
    return wrapper

def __save_log(user_id, log_type, service, method, details, time_execute):
    info = {
        'user_id': user_id,
        'ip_address': request.remote_addr,
        'log_type': log_type,
        'service': service,
        'method': method,
        'details': details,
        'time_execute': time_execute
    }

    ## insert log in database
