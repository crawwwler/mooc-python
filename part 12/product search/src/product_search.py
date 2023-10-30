# Write your solution here
def search(products: list, criterion: callable):
    x = []
    for p in products:
        if criterion(p):
            x.append(p)
    return x