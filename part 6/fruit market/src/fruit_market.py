def read_fruits():
    dic = {}
    with open("fruits.csv") as nu_file:
        for line in nu_file :
            line = line.replace("\n", "")
            frus = line.split(";")
            fruit = frus[0]
            price = float(frus[1])
            dic[fruit] = price
    return dic
