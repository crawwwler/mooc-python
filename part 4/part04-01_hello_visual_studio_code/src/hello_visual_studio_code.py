while True :
    editor = input("Editor:")
    word = editor.lower()
    if word == "visual studio code" :
        print("an excellent choice!")
        break
    elif word == "word" or word == "notepad" :
        print("awful")
    else :
        print("not good")