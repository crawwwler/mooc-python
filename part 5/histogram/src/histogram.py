def histogram(h: str):
    dic = {}
    for i in range(len(h)):
        if not(h[i] in dic):
            dic[h[i]] = 0
        dic[h[i]] += 1

    for key, value in dic.items():
        print(key,"*"*value)
    



if __name__ == "__main__" :
    histogram("statistically")