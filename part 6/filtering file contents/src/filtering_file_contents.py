import re
def filter_solutions():
    problems = []
    results = []
    names = []

    #reading the file
    with open("solutions.csv") as theFile :
        for line in theFile :
            parts = line.split(";")
            names.append(parts[0])
            problems.append(parts[1])
            results.append(parts[-1].strip())
    
    #doing operations using the lists
    correct_list = []
    incorrect_list = []
    for i in range(len(problems)) :
        parts = re.split(r'\s*([-+])\s*', problems[i])
        r = 0
        x = int(parts[0])
        y = int(parts[-1])
        if parts[1] == "-" :
            r = x - y
        elif parts[1] == "+" :
            r = x + y 
        if r == int(results[i]) :
            correct_list.append(f"{names[i]};{problems[i]};{results[i]}")
        else :
            incorrect_list.append(f"{names[i]};{problems[i]};{results[i]}")
    
    with open("correct.csv", "w") as correct:
        for s in correct_list :
            correct.write(s+"\n")
    
    with open("incorrect.csv", "w") as incorrect :
        for s in incorrect_list :
            incorrect.write(s+"\n")


