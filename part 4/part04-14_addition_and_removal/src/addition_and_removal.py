list = []
print(f"The list is now {list}")
x = 1
while True :
    cm = input("a(d)d, (r)emove or e(x)it:")
    if cm == "x" :
        break
    if cm == "d" :
        list.append(x)
        x += 1
    if cm == "r" :
        if list != [] :
            list.pop(len(list)-1)
            x-=1
    print(f"The list is now {list}")
print("Bye!")