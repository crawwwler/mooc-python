import re
def filter_incorrect():
    try:
        alpha = []
        with open("lottery_numbers.csv") as lottery :
            for line in lottery :
                beta = []
                test = True
                line = line.strip()
                parts = re.split(' |;|,', line)
                helper = []
                for i in range(2,len(parts)):
                    #you can use try - except statement in such error prone situations,
                    #just one line in try block
                    try:
                        x = int(parts[i])
                    except:
                        x = -1
                    if x in helper:
                        test = False
                        break
                    elif x < 0 or x > 39 :
                        test = False
                        break
                    helper.append(x)
                if test :
                    try:
                        if int(parts[1]) < 0 :
                            continue
                    except:
                        continue
                    beta.append(parts[0] + " " + parts[1])
                    for i in parts[2:] :
                        beta.append(i)
                alpha.append(beta)
            writer(alpha)

    except :
        print("theres somthing wrong reading the file")                


def writer(alpha: list) :
    with open("correct_numbers.csv", "w") as co:
        for l in alpha:
            if len(l) < 8 :
                continue
            co.write(f"{l[0]};{l[1]},{l[2]},{l[3]},{l[4]},{l[5]},{l[6]},{l[7]}\n")



if __name__ == "__main__" :
    filter_incorrect()

    


    
    




