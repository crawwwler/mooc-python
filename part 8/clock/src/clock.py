class Clock:

    def __init__(self, hour: int, minute: int, second: int):
        self.hour = 0
        self.minute = 0
        self.second = 0

        if hour < 24 :
            self.hour = hour
        if minute < 60 :
            self.minute = minute
        if second < 60 :
            self.second = second

    def set(self, hour: int, min: int):
        if hour < 24 :
            self.hour = hour
        if min < 60 :
            self.minute = min
        self.second = 0

    def tick(self):
        if self.second < 59 :
            self.second += 1
        else :
            self.second = 0
            if self.minute < 59 :
                self.minute += 1
            else :
                self.minute = 0
                if self.hour < 23:
                    self.hour += 1
                else :
                    self.hour = 0
    
    def __str__(self):
        sec = f"{self.second}"
        min = f"{self.minute}"
        hou = f"{self.hour}"

        if self.second < 10 :
            sec = f"0{self.second}"
        if self.minute < 10 :
            min = f"0{self.minute}"
        if self.hour < 10 :
            hou = f"0{self.hour}"
        
        return f"{hou}:{min}:{sec}"
    


