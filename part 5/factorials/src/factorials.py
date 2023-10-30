def factorials(n: int):
    fact = {}
    for i in range(1, n+1):
        f = i
        if f == 1:
            fact[1] = 1
            continue
        for x in range(i-1, 0, -1):
            f = f * x
        fact[i] = f
    return fact




if __name__ == "__main__":
    xx = factorials(5)
    print(xx)