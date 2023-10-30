import fractions

def fractionate(amount: int):
    alist = []
    for i in range(amount):
        x = fractions.Fraction(1,amount)
        alist.append(x)
    return alist


if __name__ == "__main__" :
    print(fractionate(3))
