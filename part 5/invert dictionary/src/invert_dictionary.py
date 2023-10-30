def invert(dictionary: dict):
    
    dic = {}
    for key, value in dictionary.items():
        dic[value] = key
    dictionary.clear()
    for key, value in dic.items() :
        dictionary[key] = value
    
    







if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
    
    