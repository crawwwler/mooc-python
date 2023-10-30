def store_personal_data(person: tuple):
    name = person[0]
    age = person[1]
    height = person[-1]

    with open("people.csv", "a") as pipel:
        pipel.write(f"{name};{age};{height}\n")






if __name__ == "__main__" :
    t = 'shahin dehghan', 28, 1.88
    store_personal_data(t)