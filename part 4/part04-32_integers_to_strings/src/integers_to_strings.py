def formatted(list: list) -> list:
    newlist = []
    for f in list :
        newlist.append(f"{f:.2f}")
    return newlist




#if __name__ == "__main__" :
    #my_list = [1.234, 0.3333, 0.11111, 3.446]
   # new_list = formatted(my_list)
   # print(new_list)