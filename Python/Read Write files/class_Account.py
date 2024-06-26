class Account:
    def __init__(self, bal) -> None:
        self.__balance = bal
    
    @property
    def balance(self):
        return self.__balance
    
    @setter.balance
    def balance(self, value):
        if value < 0:
            value = 0

        self.__balance = value

sapna_acc = Account()


priint(sapna_acc.balance)

sapna_acc.balance = 100

