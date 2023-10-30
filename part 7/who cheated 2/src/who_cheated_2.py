from datetime import datetime, timedelta

def final_points():
    students_and_points = {}
    start_time = start_of_exam('start_times.csv')
    stats = exam_statistic('submissions.csv')

    for key in start_time :
        x = key
        total_point = 0
        start = start_time[x]
        for i in range(1,9):
            best_point = 0
            try:
                for j in stats[x][i]:
                    if j[0] > best_point and diff_check(start,j[1]) :
                        best_point = j[0]
            except:
                best_point = 0
            total_point += best_point
        students_and_points[key] = total_point
    return students_and_points




def start_of_exam(filename: str):
    dic = {}
    with open(filename) as ff:
        for line in ff :
            name, time = line.strip().split(';')
            dic[name] = time
    
    return dic


def exam_statistic(filename: str):
    dic = {}
    with open(filename) as ff:
        for line in ff :
            name, task, point, time = line.strip().split(';')
            task = int(task)
            point = int(point)
            if name in dic :
                if task in dic[name] :
                    dic[name][task].append((point,time))
                else:
                    dic[name][task] = [(point,time)]
            else :
                dic[name]= {task:[(point,time)]}

    return dic


def diff_check(start_time: str, end_time: str)-> bool :
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    max_diff = timedelta(hours=3)
    diff = end - start
    return diff < max_diff
                



if __name__ == "__main__" :
    print(final_points())

            
            