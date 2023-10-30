def line(i,s):
    print(s * i)

def shape(height,first,width,second):
    x = 1
    while x <= height :
        line(x,first)
        x += 1
    while width > 0 :
        line(height,second)
        width -= 1



if __name__ == "__main__":
    shape(5, "x", 2, "o")