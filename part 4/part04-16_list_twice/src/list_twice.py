list = []
while True :
    adad = int(input("New item:"))
    if adad == 0 :
        break
    list.append(adad)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")
print("Bye!")