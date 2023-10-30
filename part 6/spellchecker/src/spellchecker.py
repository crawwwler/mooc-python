def spell_checker(word: str)-> bool :
    with open("wordlist.txt") as file_name :
        for line in file_name :
            line = line.strip()
            if line == word.lower() :
                return True
        return False
        


sen = input("Write text:")
words = sen.split(" ")
for w in words :
    x = spell_checker(w)
    if x :
        w = w
    else :
        w = f"*{w}*"
    print(f"{w}", end=" ")



