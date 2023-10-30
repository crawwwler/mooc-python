def no_vowels(word : str)-> str :
    
    vowe = ['a', 'e', 'i', 'o', 'u']
    for v in vowe :
       word = word.replace(v, "")
    return word 