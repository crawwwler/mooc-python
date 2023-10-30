def spruce(i):
    print("a spruce!")
    x = 1
    f = i - 2
    s = i - 2
    while i > 0 :
        if f >= 0 :
            print(" " * f, "*" * x)
        else :
            print("*" * x)
        i -= 1
        f -= 1
        x += 2
    print(" " * s , "*")



if __name__ == "__main__":
    spruce(5)