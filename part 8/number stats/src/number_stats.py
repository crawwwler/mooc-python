# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.numlist = []

    def add_number(self, number:int):
        self.numlist.append(number)
        self.numbers += 1

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return sum(self.numlist)

    def average(self):
        try:
            return sum(self.numlist) / len(self.numlist)
        except ZeroDivisionError:
            print('No numbers added')
    




print('Please type in integer numbers:')
wwn = NumberStats()
even = NumberStats()
odd = NumberStats()
while True :
    inp = int(input())

    if inp == -1 :
        break
    elif inp % 2 == 0 :
        even.add_number(inp)
    elif inp % 2 != 0 :
        odd.add_number(inp)
    
    wwn.add_number(inp)

print(f"Sum of numbers: {wwn.get_sum()}")
print(f"Mean of numbers: {wwn.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")
