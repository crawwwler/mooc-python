class Car:
    def __init__(self):
        self.__petrol = 60
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, distance: int):
        if distance > 0 :
            if distance <= self.__petrol :
                self.__petrol -= distance
                self.__odometer += distance
            else :
                self.__odometer += self.__petrol
                self.__petrol = 0
            
    def __str__(self):
        return f"Car: otometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"