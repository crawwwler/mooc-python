from difflib import get_close_matches
import keyword

def spellchecker(word: str):
    with open('wordlist.txt') as ff:
        for line in ff :
            line = line.strip()
            if word == line :
                return True
        return False


def suggestions(word: str):
    wlist = []
    with open('wordlist.txt') as ff:
        for line in ff :
            line = line.strip()
            wlist.append(line)
    x = get_close_matches(word,wlist)
    s = ''
    for i in x :
        s = s + i + ", "
    return word + ": " + s[:-2]

sen = input("write text:")
words = sen.split(" ")
corrections = []
for w in words:
    if spellchecker(w.lower()):
        w = w
    else :
        sen = sen.replace(w, "*"+w+"*")
        corrections.append(suggestions(w))

print(sen)
print('suggestions:')
for c in corrections :
    print(c)
