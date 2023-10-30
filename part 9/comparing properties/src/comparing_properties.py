# Write your solution here:
#import math

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared: 'RealProperty'):
        if self.square_metres > compared.square_metres:
            return True
        return False
    
    def price_difference(self, compared: 'RealProperty'):
        this_price = self.square_metres * self.price_per_sqm
        compared_price = compared.square_metres * compared.price_per_sqm
        return abs(this_price - compared_price)
    
    def more_expensive(self, compared: 'RealProperty'):
        this_price = self.square_metres * self.price_per_sqm
        compared_price = compared.square_metres * compared.price_per_sqm
        return this_price > compared_price
    





