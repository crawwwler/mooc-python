def writer(finn:str, eng:str):
    with open("dictionary.txt", "a") as dic :
        dic.write(f"{finn}:{eng}\n")

    print("Dictionary entry added")


def reader(term:str):
    rList = []
    with open("dictionary.txt") as dic :
        for line in dic:
            parts = line.split(":")
            if term in parts[0] or term in parts[1]:
                rList.append(f"{parts[0]} - {parts[1]}")
    for z in rList :
        print(z)
    


while True :
    print("1 - Add word, 2 - Search, 3 - Quit")
    vorodi = int(input("Function:"))
    if vorodi == 3 :
        print("Bye!")
        break

    if vorodi == 1 :
        finn = input("The word in Finnish:")
        eng = input("The word in English:")
        writer(finn,eng)

    if vorodi == 2 :
        term = input("Search term:")
        reader(term)


