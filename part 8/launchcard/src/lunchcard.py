class LunchCard:

    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        if self.balance - 2.60 >= 0 :
            self.balance -= 2.60
            return True
        return False
    
    def eat_special(self):
        if self.balance - 4.60 >= 0 :
            self.balance -= 4.60
            return True
        return False
    
    def deposit_money(self, amount: int):
        if amount < 0 :
            raise ValueError('You cannot deposit an amount of money less than zero')
        self.balance += amount




peter = LunchCard(20)
grace = LunchCard(30)

peter.eat_special()
grace.eat_lunch()

print(f"Peter: {peter}")
print(f"Grace: {grace}")

peter.deposit_money(20)
grace.eat_special()

print(f"Peter: {peter}")
print(f"Grace: {grace}")

peter.eat_lunch()
peter.eat_lunch()
grace.deposit_money(50)

print(f"Peter: {peter}")
print(f"Grace: {grace}")