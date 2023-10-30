def dict_of_numbers()-> dict :
    
    numbers = {}
    txxt = ""
    for num in range(100):
        if num == 0 :
            txxt = "zero"
        elif num < 10 :
            txxt = yekan(num)
        elif num < 20 :
            txxt = dahtabis(num)
        elif num < 100 :
            
            tos = str(num)
            y = int(tos[0])
            d = int(tos[1])
            if d == 0 :
                txxt = f"{dahgan(y)}"
            else :    
                txxt = f"{dahgan(y)}-{yekan(d)}"
        
        numbers[num] = txxt
    return numbers








def yekan(num: int)-> str :

    match num :
        case 1 :
            return "one"
        case 2 :
            return "two"
        case 3 :
            return "three"
        case 4 :
            return "four"
        case 5 :
            return "five"
        case 6 :
            return "six"
        case 7 :
            return "seven"
        case 8 :
            return "eight"
        case 9 :
            return "nine"
        


def dahgan(num: int)-> str :
    match num :
        case 2 :
            return "twenty"
        case 3 :
            return "thirty"
        case 4 :
            return "forty"
        case 5 :
            return "fifty"
        case 6 :
            return "sixty"
        case 7 :
            return "seventy"
        case 8 :
            return "eighty"
        case 9 :
            return "ninety"
        


def dahtabis(num: int)-> str :
    match num :
        case 10 :
            return "ten"
        case 11 :
            return "eleven"
        case 12 :
            return "twelve"
        case 13 :
            return "thirteen"
        case 14 :
            return "fourteen"
        case 15 :
            return "fifteen"
        case 16 :
            return "sixteen"
        case 17 :
            return "seventeen"
        case 18 :
            return "eighteen"
        case 19 :
            return "nineteen"
        



if __name__ == "__main__" :
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])