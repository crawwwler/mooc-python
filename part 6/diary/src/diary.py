def diary_writer(diary: str):
    with open("diary.txt", "a") as notebook:
        notebook.write(f"{diary}\n")
        notebook.close()

def diary_reader():
    with open("diary.txt") as notebook:
        xd =notebook.read()
        print(xd)


while True :
    print("1 - add an entry, 2 - read entries, 0 - quit")
    entry = int(input("Function:"))

    if entry == 0 :
        print("Bye now!")
        break

    if entry == 1 :
        diary = input("Diary entry")
        diary_writer(diary)

    if entry == 2 :
        diary_reader()
    

