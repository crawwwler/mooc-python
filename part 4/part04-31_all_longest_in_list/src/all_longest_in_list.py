def all_the_longest(list : list ) -> list :

    x = sorted(list, key = len)
    newlist = []
    for i in list :
        if len(i) >= len(x[-1]) :
            newlist.append(i)
    
    return newlist
                



if __name__ == "__main__" :

    list = ["Alan", "Steve", "Seymour", "Kim", "Susan"]
    print(all_the_longest(list))