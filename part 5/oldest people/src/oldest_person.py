def oldest_person(people: list):
    hlpr = people[0][1]
    name = people[0][0]

    for p in people :
        if p[1] < hlpr :
            hlpr = p[1]
            name = p[0]
        
    return name








#if __name__ == "__main__" :
  #  person1 = ("mary", 1984)
   # person2 = ("eli", 1978)
    #person3 = ("al", 1940)
    #person4 = ("mino", 1973)

    #persons = [person1, person2, person3, person4]
    #p = oldest_people(persons)
    #print(p)