def remove_smallest(numbers: list):
    smallest = numbers[0]
    for n in numbers :
        if n < smallest :
            smallest = n
    
    numbers.remove(smallest)









if __name__ == "__main__":
    li = [9,7,5,3]
    remove_smallest(li)

        