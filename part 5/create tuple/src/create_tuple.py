def create_tuple(x: int, y: int, z: int):
    li = [x,y,z]
    li.sort()
    sum_of_values = sum(li)
    li.pop(1)
    tuple_to_return = (li[0],li[1],sum_of_values)
    return tuple_to_return




if __name__ == "__main__" :
    print(create_tuple(1,4,2))