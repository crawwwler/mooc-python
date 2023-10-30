my_list = []
items = int(input("How many items:"))
x = 1 
while x <= items :
    elements = int(input(f"Item {x}:"))
    my_list.append(elements)
    x += 1
print(my_list)