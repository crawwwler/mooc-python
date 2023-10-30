fileOne = input("Student information:")
fileTwo = input("Exercises completed:")
fileThree = input("Exam points:")


students = {}
exercises = {}
examPoints = {}

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


#reading the third file coitaining the exam points
with open(fileThree) as three :
    for line in three :
        parts = line.split(";")
        if parts[0] == "id" :
            continue
        identifier = parts[0]
        examPoints[identifier] = []
        for i in parts[1:] :
            examPoints[identifier].append(int(i.strip()))
    

        
#calculate the exercise point
def exercise_point(point: int):
    if point < 4 :
        return 0
    elif point < 8 :
        return 1
    elif point < 12 :
        return 2
    elif point < 16 :
        return 3
    elif point < 20 :
        return 4
    elif point < 24 :
        return 5
    elif point < 28 :
        return 6
    elif point < 32 :
        return 7
    elif point < 36 :
        return 8 
    elif point < 40 :
        return 9
    elif point == 40 :
        return 10


# returning the grade :
def grade(exam: int, point: int):
    g = exam + point

    if g <=14 :
        return 0
    elif g <= 17 :
        return 1
    elif g <= 20 :
        return 2
    elif g <= 23 :
        return 3
    elif g <= 27 :
        return 4
    elif g >= 28 :
        return 5


#printing the results 
for key, value in students.items():
    if key in exercises and key in examPoints :
        ex = exercise_point(sum(exercises[key]))
        g = grade(sum(examPoints[key]), ex)
        print(f"{students[key]} {g}")
