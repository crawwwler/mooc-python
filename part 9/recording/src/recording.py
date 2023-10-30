class Recording:
    def __init__(self, length: int):
        if length >= 0 :
            self.__length = length
        else :
            raise ValueError("The length cannot be negative")
        
    @property
    def length(self):
            return self.__length
        
    @length.setter
    def length(self, le: int):
        if le >= 0 :
            self.__length = le
        else :
            raise ValueError("The length cannot be negative")