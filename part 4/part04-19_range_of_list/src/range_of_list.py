def range_of_list(list : list) -> int :
    maximum = max(list)
    minimum = min(list)
    return maximum - minimum



if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)