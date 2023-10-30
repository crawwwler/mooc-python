fileOne = input("Student information:")
fileTwo = input("Exercises completed:")

students = {}
exercises = {}

#reading from first file containing students names
with open(fileOne) as first :
    for line in first :
        parts = line.split(";")
        if parts[0] == "id":
            continue
        identifier = parts[0]
        name = f"{parts[1].strip()} {parts[2].strip()}"
        students[identifier] = name 

#reading the grades and storing every student's grades in a separate list
with open(fileTwo) as two :
    for line in two :
        parts = line.split(";")
        if parts[0] == "id" :
            continue
        identifier = parts[0]
        exercises[identifier] = []
        for i in parts[1:] :
            exercises[identifier].append(int(i.strip()))
        

#printing the info

for key, value in students.items():
    if key in exercises :
        grades = exercises[key]
        print(f"{value} {sum(grades)}")
    else :
        print(f"{value } has done nothing!")
