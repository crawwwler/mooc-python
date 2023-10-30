def list_sum(list1 : list, list2 : list) -> list :
    list_to_return = []
    sum = 0
    for i in range(len(list1)) :
        sum = list1[i] + list2[i]
        list_to_return.append(sum)
    return list_to_return




if __name__ == "__main__" :
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]