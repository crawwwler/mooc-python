def same_chars(word,i,j):
    if j >= len(word) or i >= len(word):
        return False
    else:
        if word[i] == word[j] :
            return True
        else:
            return False
    


if __name__ == "__main__":
    same_chars("abc", 0, 3) 