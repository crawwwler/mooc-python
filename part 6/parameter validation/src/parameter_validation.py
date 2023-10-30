def new_person(name:str, age:int):
    x = name.split(" ")

    if name == '' or len(x) < 2 or len(name) > 40 :
        raise ValueError("something went wrong")
    if age < 0 or age > 150 :
        raise ValueError("somethign went wrong")
    
    return (name, age)
