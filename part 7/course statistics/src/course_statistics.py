import urllib.request
import json

def retrieve_all():

    first = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    sec = first.read()

    content = json.loads(sec)

    clist = []

    for i in content :
        sum_of_ex = 0

        xtup = ()

        if i['enabled'] == True :
            cfname = i['fullName']
            cname = i['name']
            cyear = i['year']
            for j in i['exercises'] :
                sum_of_ex += j
            xtup = cfname, cname, cyear, sum_of_ex
            clist.append(xtup)
    
    return clist


def retrieve_course(course_name: str):
    link = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats".replace('****', course_name)
    x = urllib.request.urlopen(link)
    xx = x.read()
    content = json.loads(xx)
    dic = {}
    dic['weeks'] = len(content)
    try:
        dic['students'] = content['0']['students']
        rang = range(len(content))
    except:
        dic['students'] = content['1']['students']
        rang = range(1,len(content)+1)
    dic['hours'] = 0
    dic['exercises'] = 0

    for i in rang :
        xi = str(i)
        if content[xi]['students'] > dic['students'] :
            dic['students'] = content[xi]['students']
        dic['hours'] += content[xi]['hour_total']
        dic['exercises'] += content[xi]['exercise_total']
    
    dic['hours_average'] = dic['hours'] // dic['students']
    dic['exercises_average'] = dic['exercises'] // dic['students']

    return dic


    




if __name__ == "__main__" :
    print(retrieve_course("CCFUN"))