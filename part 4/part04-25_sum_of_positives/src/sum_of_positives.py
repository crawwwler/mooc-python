def sum_of_positives(list : list) -> int :
    sum = 0
    for i in list :
        if i > 0 :
            sum = sum + i
    return sum


if __name__ == "__main__" :
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)