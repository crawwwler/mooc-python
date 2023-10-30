def line(i,s):
    print(s * i)

def square_of_hashes(size):
    x = 0
    while x < size:
        line(size, "#")
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
