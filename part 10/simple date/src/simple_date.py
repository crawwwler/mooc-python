class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"
    
    def __eq__(self, another):
        if self._year != another._year :
            return False
        elif self._month != another._month :
            return False
        elif self._day != another._day:
            return False
        return True
    
    def __ne__(self, another):
        if (self._year == another._year and
            self._month == another._month and
            self._day == another._day):
            return False
        return True
    
    def __gt__(self, another):
        if self._year > another._year:
            return True
        elif self._year < another._year:
            return False
        else:
            if self._month > another._month:
                return True
            elif self._month < another._month:
                return False
            else:
                if self._day > another._day:
                    return True
                else :
                    return False
                
    def __lt__(self, another):
        if self._year < another._year:
            return True
        elif self._year > another._year:
            return False
        else:
            if self._month < another._month:
                return True
            elif self._month > another._month:
                return False
            else :
                if self._day < another._day :
                    return True
                else:
                    return False

    
    def __add__(self, nod: int):
        day = self._day
        month = self._month
        year = self._year
        x = 0
        while x < nod :
            day += 1
            if day > 30:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            x += 1

        return SimpleDate(day, month, year)
    
    def __sub__(self, another):
        x = (self._year * 360) + (self._month * 30) + self._day
        y = (another._year * 360) + (another._month * 30) + another._day
        dif = abs(x - y)
        return dif


