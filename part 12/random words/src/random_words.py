from random import randint
def word_generator(characters: str, length: int, amount: int):
    n = 0
    while n < amount:
        x = ''
        for i in range(length):
            x += characters[randint(0,len(characters)-1)]
        yield x
        n += 1

