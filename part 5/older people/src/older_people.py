def older_people(people: list, year: int):

    new_list = []
    for p in people :
        if p[1] < year :
            new_list.append(p[0])
    
    return new_list






if __name__ == "__main__":
    p1 = ("alex", 1986)
    p2 = ("matt", 1994)
    p3 = ("jamie", 1977)
    p4 = ("nick", 1980)
    people = [p1,p2,p3,p4]
    x = older_people(people, 1990)
    print(x)