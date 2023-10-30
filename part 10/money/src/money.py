# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._amount():.2f} eur"
    
    def _amount(self):
        x = float(self._euros)
        y = self._cents / 100
        return x + y
    
    def __eq__(self, another):
        return self._amount() == another._amount()

    def __gt__(self, another):
        return self._amount() > another._amount()
    
    def __lt__(self, another):
        return self._amount() < another._amount()
    def __ne__(self, another):
        return self._amount() != another._amount()
    
    def __add__(self, another):
        v = self._amount() + another._amount()
        a = int(v)
        b = (v - a) * 100
        return Money(a, b)

    def __sub__(self, another):
        if self._amount() - another._amount() >= 0 :
            v = self._amount() - another._amount()
            a = int(v)
            b = (v - a) * 100
            return Money(a, b)
        else:
            raise ValueError(f"a negative result is not allowed")


