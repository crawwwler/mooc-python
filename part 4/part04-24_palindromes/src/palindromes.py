def palindromes(word : str) -> bool :
    if len(word) == 2 :
        if word[0] == word[1] :
            return True
        else:
            return False
    length = len(word) // 2
    h = ""
    if len(word) % 2 == 0 :
        w1 = word[0:length]
        w2 = word[length:len(word)]
    else :
        w1 = word[0:length]
        w2 = word[length+1:len(word)]
    for i in range(len(w2)-1, -1, -1) :
        h = h + w2[i]
    
    return w1 == h
    


while True:
    winput = input("Please type in a palindrome:")

    if palindromes(winput) :
        print(f"{winput} is a palindrome!")
        break
    else :
        print("that wasn't a palindrome")