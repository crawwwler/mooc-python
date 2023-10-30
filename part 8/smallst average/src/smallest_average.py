def smallest_average(person1: dict, person2: dict, person3: dict):
    x = person1, person2, person3
    helper = [] 
    for i in x :
        d = average(i)
        helper.append((i, d))
    smallest = helper[0][1]
    dic_to_return = helper[0][0]
    for i in range(len(helper)):
        if helper[i][1] < smallest :
            smallest = helper[i][1]
            dic_to_return = helper[i][0]
    return dic_to_return

# for returning the average of a person's stats
def average(person: dict)-> float:
    sum = 0
    for value in person.values():
        if isinstance(value, int):
            sum += value
    return sum / 3

if __name__ == "__main__" :
    
    print(smallest_average({"result1": 1,"result2": 1,"result3": 1},
                            {"result1": 2,"result2": 2,"result3": 2},
                              {"result1": 3,"result2": 3,"result3": 3}))

