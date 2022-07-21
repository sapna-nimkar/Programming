from typing import Any, Union, List
class SomeWonder:
    # def sum(a: int, b: int, c: int) -> int:
    #     return a + b + c
    # def sum(a: int, b: int) -> int:
    #     return a + b
    # def sum(a: str, b: str) -> str:
    #     return a + " " + b

    def sum(a: int, b: int, c: int = 0) -> int:
        return a + b + c
    @staticmethod
    def add(a: Union[int, str], b: Union[int, str]) -> Any:
        if type(a) == type(10) and type(b) == type(10):
            return a + b
        if type(a) == type("") and type(b) == type(""):
            return a + " " +b


obj = SomeWonder()
print(obj.add(10, 20))                   # 30
print(obj.add("Supratim", "Samantray"))    # "Supratim Samantray"
