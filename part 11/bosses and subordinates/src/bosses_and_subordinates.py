# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)
    
    def number_of_subs(self):
        return len(self.subordinates)

def count_subordinates(employee: Employee):
    count = employee.number_of_subs()
    if count > 0 :
        for e in employee.subordinates:
            count += count_subordinates(e)
    return count

