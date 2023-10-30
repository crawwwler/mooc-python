def input_from_user()-> list:

    results = []

    while True :
        result = input("Exam points and exercises completed: ")
        if result == "" :
            break
        results.append(result)
    return results



def points(results : list )-> list :
    
    points = []

    for r in results :
        exam ="T "
        exam_point = float(r.split(" ")[0])
        if exam_point < 10 :
            exam = "F " 
        exercise_point = exercise_to_point(float(r.split(" ")[1]))
        point = exam_point + exercise_point
        finalpoint = exam + str(point)
        points.append(finalpoint)
    
    return points



def exercise_to_point(score : float) -> float :
    
    score = score / 100.0

    if score < 0.10 : 
        return 0
    elif score < 0.20 :
        return 1
    elif score < 0.30 :
        return 2
    elif score < 0.40 :
        return 3
    elif score < 0.50 :
        return 4
    elif score < 0.60 :
        return 5
    elif score < 0.70 :
        return 6
    elif score < 0.80 :
        return 7
    elif score < 0.90 :
        return 8
    elif score < 1.0 :
        return 9
    elif score == 1.0 :
        return 10



def grades(points : list )-> list :
    
    grades_list = []
    
    for p in points:
        s = p.split(" ")[0]
        x = float(p.split(" ")[1])
        if s == "F" or x <= 14 :
            grades_list.append(0)
        elif x <= 17 :
            grades_list.append(1)
        elif x <= 20 :
            grades_list.append(2)
        elif x <= 23 :
            grades_list.append(3)
        elif x <= 27 :
            grades_list.append(4)
        elif x <= 30 :
            grades_list.append(5)
    
    return grades_list



def average(points : list)-> float :

    sum = 0 
    for p in points :
        sum = sum + float(p.split(" ")[1])
    
    return sum / len(points)



def percentage(grades : list)-> float :
    
    count = 0 
    for g in grades :
        if g > 0 :
            count += 1
    
    return (count / len(grades)) * 100.0



def print_results(av : float, per : float, grades : list):

    print('Statistics:')
    print(f"Points average: {av}")
    print(f"Pass percentage: {per:.1f}")
    print('Grade distribution:')
    for i in range(5,-1,-1):
        print(f"{i}: ", end="")
        for g in grades :
            if g == i :
                print("*", end="")
        print()
    print()



def main():

    results = input_from_user()
    points_result = points(results)
    grades_result = grades(points_result)
    average_result = average(points_result)
    percentage_result = percentage(grades_result)
    print_results(average_result, percentage_result, grades_result)



main()