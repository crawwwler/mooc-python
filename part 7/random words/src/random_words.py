import random

def words(n: int, beginning: str):
    x = reader_file(beginning)
    try:
        tor = random.sample(x, n)
    except:
        raise ValueError("not enough words")
    return tor




def reader_file(beginning: str):
    lisst = []
    with open("words.txt") as myfile:
        for line in myfile :
            line = line.strip()
            if line.startswith(beginning):
                lisst.append(line)

    return lisst




if __name__ == "__main__" :
    word_list = words(3, "ca")
    for word in word_list:
        print(word)