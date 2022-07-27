# Objects
What is Self in method?

self in Instace Methods of a class is used to refer/access the values related to the Object
"""
class Account:
def __init__(self, n, b) -> None:
self.name = n
self.balance = b

def loan_allowed(self):
"""Instance(Object) Method"""
if self.balance > 0:
return self.balance * 10
return 0

def withdraw(self, amount):
if self.balance - amount < 0:
raise ValueError
self.balance -= amount

sapna = Account("Sapna", 10000)
supratim = Account("Supratim", 0)
sapna.loan_allowed()
supratim.loan_allowed()