# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        if len(self.people) == 0 :
            return True
        return False
    
    def print_contents(self):
        print(f"There are {len(self.people)} persons in the room, and their combined height is {self.com_heights()} cm")
        for p in self.people:
            print(f"{p} ({p.height} cm)")

    def com_heights(self):
        combined = 0
        for p in self.people :
            combined += p.height
        return combined
    
    def shortest(self):
        if self.is_empty():
            return None
        check_p = self.people[0]
        check_height = self.people[0].height
        for p in self.people:
            if p.height < check_height :
                check_p = p
                check_height = p.height
        return check_p
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        person_to_remove = self.shortest()
        self.people.remove(person_to_remove)
        return person_to_remove
    
