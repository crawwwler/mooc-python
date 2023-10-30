from datetime import datetime, timedelta


def cheaters()-> list :
    cheaters_list = []
    exam_times = time_reader('start_times.csv')
    sub_times = sub_reader('submissions.csv')
    for key in exam_times :
        x = exam_times[key]
        for i in sub_times[key]:
            if diff_time(i, x) :
                continue
            else :
                if not(key in cheaters_list):
                    cheaters_list.append(key)
    return cheaters_list



def time_reader(filename: str)-> dict:
    exam_times = {} # to store time of starting the exam of each student
    with open(filename) as ff :
        for line in ff :
            name, time = line.strip().split(';') #strip and split at the same time,storing in a tuple way
            exam_times[name] = time
    return exam_times



# function to handle exam statistics for each student
def sub_reader(filename: str)-> dict:
    sub_times = {}
    with open(filename) as ff:
        for line in ff :
            name, task, points, time = line.strip().split(';')
            if name in sub_times :
                sub_times[name].append(time)
            else :
                sub_times[name] = [time]
    return sub_times



# to calculate the difference between start time and end time
def diff_time(endtime: str, starttime: str):
    start = datetime.strptime(starttime, "%H:%M")
    end = datetime.strptime(endtime,"%H:%M")
    diff = end - start
    max_diff = timedelta(hours=3) #defining timedelta is a key here
    return diff <= max_diff




if __name__ == "__main__" :
    z = cheaters()
    print(z)