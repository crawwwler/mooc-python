class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(routes: list):
    def new_order(cr: ClimbingRoute):
        return cr.length
    return sorted(routes, key= new_order, reverse=True)



def sort_by_difficulty(routes: list):
    def new_order(cr: ClimbingRoute):
        return cr.grade, cr.length
    # *** VERY IMPORTANT POINT RIGHT HERE ***
    # TO HANDLE EQUALITY BY FIRST FACTOR, YOU COULD HAVE A TUPPLE OR LIST AS CRITERIA 
    #SO IF OBJECTS ARE EQUAL BASED ON FIRST FACTOR PYTHON WILL CHECK THE SECOND FACTOR
    return sorted(routes, key=new_order, reverse=True)


    