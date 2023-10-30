fileOne = input("Student information:")
fileTwo = input("Exercises completed:")
fileThree = input("Exam points:")
#fileOne = "students1.csv"
#fileTwo = "exercises1.csv"
#fileThree = "exam_points1.csv"

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
    return point // 4


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
name = "name"
exec_nbr = "exec_nbr"
exm_pts = "exm_pts."
exec_pts = "exec_pts."
tot_pts = "tot_pts."
gr = "grade"
print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{gr:10}")
for key, value in students.items():
    if key in exercises and key in examPoints :
        p = exercise_point(sum(exercises[key]))
        g = grade(sum(examPoints[key]), p)
        e = sum(examPoints[key])
        print(f"{value:30}{sum(exercises[key]):<10}{p:<10}{e:<10}{p+e:<10}{g:<10}")
        