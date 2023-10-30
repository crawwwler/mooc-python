number = int(input("please type in a positive integer:"))
for i in range(-number,number+1,1) :
    if i == 0 :
        continue
    print(i)