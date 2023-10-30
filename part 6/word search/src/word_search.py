def find_words(searched_term: str)-> list:
    words = read_words()
    li = []
    for w in words :
        # no1 condition
        if w == searched_term :
            li.append(w)
            #no2 condition
        elif "." in searched_term :
            if len(w) == len(searched_term):
                parts = searched_term.split(".")
                helper = True
                for i in parts:
                    if i == "":
                        continue
                    x = searched_term.find(i)
                    #importan thing is to correspond the part of the term with the word
                    if w[x:x+len(i)] != i : # yeeeesssssssss GET THE FUCK INNN!!!
                        helper = False
                if helper :
                    li.append(w)
        #no3 condition
        elif searched_term.startswith("*") :
            term = searched_term[1:]
            if w.endswith(term) :
                li.append(w)
        #no4 condition
        elif searched_term.endswith("*") :
            term = searched_term[:-1]
            if w.startswith(term) :
                li.append(w)
    return li

#reading the words file
def read_words():
    words = []
    with open("words.txt") as thisFile:
        for line in thisFile :
            line = line.strip()
            words.append(line)
    return words


#print(find_words('ca.'))
#if __name__ == "__main__" :
 #   print(find_words("*vokes"))