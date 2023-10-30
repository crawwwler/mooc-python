dic = {}
while True :
    cmd = input("command (1 search, 2 add, 3 quit):")

    if cmd == "3":
        print("quitting...")
        break
    elif cmd == "2":
        name = input("name:")
        number = input("number:")
        dic[name] = number
        print("ok!")
    elif cmd == "1":
        name = input("name:")
        if name in dic :
            print(dic[name])
        else :
            print("no number")
        
