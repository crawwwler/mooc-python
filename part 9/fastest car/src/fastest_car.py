# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"



def fastest_car(cars: list):
    speed = cars[0].top_speed
    name = cars[0].make
    for car in cars :
        if car.top_speed > speed :
            speed = car.top_speed
            name = car.make
    return name 