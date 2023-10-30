import json

def print_persons(filename: str):
    with open(filename) as ff:
        content = ff.read()
    
    x = json.loads(content)
    for i in x :
        print(f"{i['name']} {i['age']} years (", end="")
        if len(i['hobbies']) != 0 :
            for j in range(len(i['hobbies'])-1) :
                print(f"{i['hobbies'][j]},", end=" ")
            print(f"{i['hobbies'][-1]})")
        else :
            print(")")



if __name__ == "__main__" :
    print_persons('file4.json')