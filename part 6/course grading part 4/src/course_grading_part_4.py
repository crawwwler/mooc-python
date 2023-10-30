def read_students(student: str):
    dic_students = {}
    with open(student) as stFIle :
        for line in stFIle :
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id" :
                continue
            identifier = parts[0]
            dic_students[identifier] = []
            name = parts[1] + " " + parts[2]
            dic_students[identifier].append(name)
    return dic_students



def read_exercises(exercise: str):
    dic_exercises = {}
    with open(exercise) as exFile :
        for line in exFile :
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id" :
                continue
            identifier = parts[0]
            dic_exercises[identifier] = []
            for i in parts[1:] :
                dic_exercises[identifier].append(int(i))
    return dic_exercises



def read_exam_points(exam_points: str):
    dic_exams = {}
    with open(exam_points) as xamFile :
        for line in xamFile :
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "id" :
                continue
            identifier = parts[0]
            dic_exams[identifier] = []
            for i in parts[1:] :
                dic_exams[identifier].append(int(i))
    return dic_exams


def exec_points(ex: int) :
    return ex // 4



def grade(point: int): 
    if point <= 14 :
        return 0
    elif point <= 17 :
        return 1
    elif point <= 20 :
        return 2
    elif point <= 23 :
        return 3
    elif point <= 27 :
        return 4
    elif point >= 28 :
        return 5
    

def read_course(course: str):
    st = ""
    with open(course) as c :
        for line in c :
            line = line.replace("\n", ",")
            parts = line.split(":")
            st += parts[1]
    st += " credits"
    return st.strip()



def resultscsv(students: str, exercises: str, exam: str):
    st = read_students(students)
    ex = read_exercises(exercises)
    ex_am = read_exam_points(exam)
    with open("results.csv", "w") as ff:
        for key, value in st.items():
            id = key
            name = st[key][0]
            p = exec_points(sum(ex[id]))
            pp = sum(ex_am[id])
            x = p + pp
            g = grade(x)
            ff.write(f"{id};{name};{g}\n")



def resulttxt(student: str, exercise: str, exam: str, course: str):
    c = read_course(course)
    students = read_students(student)
    exercise = read_exercises(exercise)
    exams = read_exam_points(exam)

    name = "name"
    exec_nbr = "exec_nbr"
    exm_pts = "exm_pts."
    exec_pts = "exec_pts."
    tot_pts = "tot_pts."
    gr = "grade"
    with open("results.txt", "w") as ff:
        ff.write(c + "\n")
        ff.write("=" * len(c) + "\n")
        ff.write(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{gr:10}\n")
        for key, value in students.items():
            id = key
            n = students[id][0] 
            ex_p = sum(exercise[id])
            ex_pts = exec_points(ex_p)
            exam_p = sum(exams[id])
            total_p = ex_pts + exam_p 
            g = grade(total_p)
            ff.write(f"{n:30}{ex_p:<10}{ex_pts:<10}{exam_p:<10}{total_p:<10}{g:<10}\n")




student = input("Student information:")
exercise = input("Exercise completed:")
exam = input("Exam points:")
course = input("Course information:")
resultscsv(student,exercise,exam)
resulttxt(student,exercise,exam,course)
print("Results written to files results.txt and results.csv")
