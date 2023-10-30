def anagrams(word1 : str , word2: str) :
    word1 = sorted(word1)
    word2 = sorted(word2)
    if word1 == word2 :
        return True
    else :
        return False
