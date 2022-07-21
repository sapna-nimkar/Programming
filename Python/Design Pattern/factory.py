from email.mime import base
import requests
import urllib3

from abc import ABC, abstractmethod

#http_interface.py
class HttpReq(ABC):
    @abstractmethod
    def get(self, url):
        pass

# urlib3_warpper.py
# from http_interface import HttpReq
class Urllib3Wrapper(HttpReq):
    def __init__(self, base_url) -> None:
        self.http = urllib3.PoolManager()
        self.base = base_url
    
    def get(self, url):
        response = self.http.request('GET', f'{self.base}/{url}')
        return response.status, response.data

u = Urllib3Wrapper('https://www.starandread.com')
s, d = u.get('supratim/cartitems')

class RequestsWrapper(HttpReq):
    def __init__(self, base_url) -> None:
        self.base = base_url

    def get(self, url):
        response = requests.get(f'{self.base}/{url}')
        return response.status_code, response.text

r = RequestsWrapper('https://www.starandread.com')
s, d = r.get('supratim/cartitems')


class HttpFactory:
    @staticmethod
    def get_instance(http_type, base):
        if http_type == 'urllib3':
            return Urllib3Wrapper(base)
        elif http_type == 'requests':
            return RequestsWrapper(base)
        else:
            raise ValueError("Invalid Option")


http_connection = HttpFactory.get_instance('urliib3', 'https://starandread.com')
status, text = http_connection.get('supratim/cartitems')

http_connection = HttpFactory.get_instance('requests', 'https://starandread.com')
status, text = http_connection.get('supratim/cartitems')

http_connection.post()


