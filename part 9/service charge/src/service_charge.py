class BankAccount:
    def __init__(self, name: str, account_number: str, balance: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    
    def deposit(self, amount: float):
        if amount >= 0 :
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("Negative values cannot be used")
    
    def withdraw(self, amount: float):
        if amount >= 0 :
            if self.__balance - amount >= 0 :
                self.__balance -= amount
                self.__service_charge()
        else :
            raise ValueError("Negative values cannot be used")
    
    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        one_percent = self.__balance * 0.01
        self.__balance -= one_percent
