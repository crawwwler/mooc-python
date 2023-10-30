def first_word(s):
    index = s.find(" ")
    w = s[0:index]
    return w

def second_word(s):
    list = s.split(" ")
    return list[1]

def last_word(s):
    list = s.split(" ")
    return list[len(list) - 1]



if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))