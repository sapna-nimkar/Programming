'''
overloading and overriding
'''
from typing import Any, Union, List

class Polly():



    @staticmethod
    def add_them(a: Any , b: Any) ->Any:
        if type(a) == type(2) and type(b) == type(2):
            return a + b
        elif type(a) == type('abc') and type(b) == type('cd'):
            return a + " " + b
        else:
            return f'inputs cannot be added'


class Tom(Polly):
    pass
    # @staticmethod
    # def add_them(a:Any, b:Any) ->Any:
    #     if type(a) == type(2) and type(b) == type(2):
    #         return a * b
    #     elif type(a) == type('abc') and type(b) == type('cd'):
    #         return f'result is {a + " " + b}'
    #     else:
    #         return f'inputs cannot be added'

polly_obj = Polly()
print(Tom.add_them(10, 40))
print(Polly.add_them(10, 40))
print(polly_obj.add_them('sdf','fgd'))
print(polly_obj.add_them(2, 'dfs'))
