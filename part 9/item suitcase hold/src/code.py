class Item:
    
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max: int):
        self.__items = []
        self.__max = max

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max:
            self.__items.append(item)
        
    def weight(self):
        sum = 0
        for i in self.__items:
            sum += i.weight()
        return sum
    
    def print_items(self):
        for i in self.__items:
            print(i)
        
    def heaviest_item(self):
        heaviest = None
        heaviest_w = 0
        if len(self.__items) == 0:
            return heaviest
        for i in self.__items:
            if i.weight() > heaviest_w :
                heaviest_w = i.weight()
                heaviest = i
        return heaviest
    
    def __str__(self):
        length = len(self.__items)
        x = ''
        if length == 1 :
            x = '1 item'
        else:
            x = f"{length} items"

        return f"{x} ({self.weight()} kg)"


class CargoHold:
    def __init__(self, max: int):
        self.__max = max
        self.__suitcases = []
  
    def add_suitcase(self, suitcase: Suitcase):
        if self.total_weight() + suitcase.weight() <= self.__max:
            self.__suitcases.append(suitcase)

    def total_weight(self):
        sum = 0
        for i in self.__suitcases:
            sum += i.weight()
        return sum
    
    def print_items(self):
        for s in self.__suitcases:
            s.print_items()
           
    def __str__(self):
        space = self.__max - self.total_weight()
        length = len(self.__suitcases)
        x = ''
        if length == 1 :
            x = '1 suitcase'
        else :
            x = f"{length} suitcases"
        
        return f"{x}, space for {space} kg"