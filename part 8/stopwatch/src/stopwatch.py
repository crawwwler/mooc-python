# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59 :
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < 59 :
                self.minutes +=1 
            else:
                self.minutes = 0
        

    def __str__(self):
        sec = f"{self.seconds}"
        min = f"{self.minutes}"
        if self.seconds < 10 :
            sec = f"0{self.seconds}"
        if self.minutes < 10 :
            min = f"0{self.minutes}"

        return f"{min}:{sec}"


