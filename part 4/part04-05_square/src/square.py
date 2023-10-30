def line(i,s):
    print(s * i)

def square(size, character):
    x = 0
    while x < size :
        line(size,character)
        x += 1
    


if __name__ == "__main__":
    square(5, "x")