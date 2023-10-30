def add_student(students: dict, name: str):
    students[name] = []


def print_student(students: dict, key: str):
    print(f"{key}:", end="")
    if not(key in students):
        print(" no such person in the database")
    elif len(students[key]) == 0 :
        print()
        print(f" no completed courses")
    else :
        print()
        print(f" {len(students[key])} completed courses:")
        for ex in students[key]:
            print(f"  {ex[0]} {ex[1]}") 
        ave = 0
        for ex in students[key]:
            ave = ave + ex[1]
        print(f" average grade {ave / len(students[key])}")


def add_course(students: dict, key: str, course: tuple):
    if course[1] == 0 :
        return

    for i in range(len(students[key])):
        if students[key][i][0] == course[0]:
            if students[key][i][1] < course[1]:
                students[key].pop(i)
                students[key].append(course)
                return
            else :
                return
    students[key].append(course)

        
def summary(students: dict):
    length = len(students)
    most, average = check_exercises(students)
    print(f"students {length}")
    print(f"most courses completed {most[0]} {most[1]}")
    print(f"best average grade {average[0]} {average[1]}")


def check_exercises(students: dict):
    most = 0 
    name = ""
    averages = []


    for key in students:
        if len(students[key]) > most :
            name = key
            most = len(students[key])
        
    
    for key in students :
        ave = 0
        for i in students[key]:
            ave = ave + i[1]
        ave = ave / len(students[key])
        averages.append((ave,key))
    averages.sort()

    m = (most,name)
    a = (averages[-1])

    return m, a
