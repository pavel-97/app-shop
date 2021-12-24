from django.core.exceptions import PermissionDenied
import time


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise PermissionDenied

        response = self.get_response(request)
        return response


class CountRequest:
    def __init__(self, get_response):
        self.get_response = get_response
        self.dict_inf = {}

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        self.dict_inf[ip] = self.dict_inf.get(ip, 0) + 1

        if not self.dict_inf.get('t1'):
            self.dict_inf['t1'] = time.time()

        count_request = self.dict_inf.get(ip)
        t2 = time.time()

        if count_request > 5 and t2 - self.dict_inf['t1'] < 10:
            raise PermissionDenied

        elif t2 - self.dict_inf['t1'] >= 10 and count_request > 5:
            self.dict_inf = {}

        return self.get_response(request)


class User:
    def __init__(self, ip):
        self.ip = ip
        self.k_request = 0
