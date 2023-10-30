# Write your solution here
def even_numbers(beginning: int, maximum: int):
    for n in range(beginning, maximum+1):
        if n % 2 == 0:
            yield n
    
