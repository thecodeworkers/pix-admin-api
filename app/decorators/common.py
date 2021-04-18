from flask.globals import session
from flask import request
from functools import wraps
from ..utils import api_abort
from ..collections.admin_logs import AdminLogs
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
    try:
        info = {
            'user': session['user']['id'] if 'user' in session else '',
            'ip_address': request.remote_addr,
            'log_type': log_type,
            'service': service,
            'method': method,
            'details': details,
            'time_execute': time_execute
        }

        AdminLogs(**info).save()

    except Exception as err:
        AdminLogs(
            ip_address=request.remote_addr,
            log_type='ERROR',
            service=__name__,
            method='save_log',
            details=str(err),
            time_execute=time_execute
        ).save()
