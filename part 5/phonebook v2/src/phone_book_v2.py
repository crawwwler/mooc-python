dic = {}

while True :
    cmd = input("command (1 search, 2 add, 3 quit):")

    if cmd == "3":
        print("quitting...")
        break
    elif cmd == "2":
        name = input("name:")
        number = input("number:")
        if not(name in dic):
            dic[name] = []
        dic[name].append(number)
        print("ok!")
    elif cmd == "1":
        name = input("name:")
        if name in dic :
            for n in dic[name]:
                print(n)
        else :
            print("no number")
    
    