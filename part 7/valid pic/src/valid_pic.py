import datetime

def is_it_valid(pic: str):
    if len(pic) != 11 :
        return False
    datee = pic[:6]
    century = pic[6]
    ctr = int(pic[:6] + pic[7:-1])
    ctr_char = pic[-1]
    a = date_validator(datee, century)
    b = pic[6] in ['-', '+', "A"]
    c = control_validator(ctr, ctr_char)

    if a and b and c :
        return True
    else :
        return False



def date_validator(datee: str, century: str):
    day = int(datee[:2])
    month = int(datee[2:4])
    year = datee[4:]
    if century == "-":
        year = int("18" + year)
    elif century == "+":
        year = int("19" + year)
    elif century == "A":
        year = int("20"+ year)
    try:
        datetime.date(year,month,day)
        return True
    except:
        return False


def control_validator(ctr: str, ctr_char: str):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K', 19: 'L',
           20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V', 28: 'W', 29: 'X',
             30: 'Y'  }
    remainder = ctr % 31
    if remainder < 10 :
        check = str(remainder)
    else :
        check = dic[remainder]
    
    if check == ctr_char :
        return True
    else :
        return False
    





if __name__ == "__main__" :
    print(is_it_valid("080842-720N"))