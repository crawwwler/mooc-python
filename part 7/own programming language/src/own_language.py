def run(program: list)-> list:
    xctn = []
    dicx = {chr(65 + i): 0 for i in range(26)} # a to z 
    locations = coordinates(program)
    i = 0
    while i < len(program) :
        
        #handling locations // quitting the loop
        if len(program[i]) == 1:
            if program[i] == 'END':
                break
               
        #jump to locations
        if 'JUMP' in program[i]:
            check = False
            commands = program[i].split(" ")
            if len(commands) == 2 :
                i = locations[commands[1].strip(':')]
                continue
            x = 0
            y = 0
            if commands[1] in dicx :
                x = dicx[commands[1]]
            else :
                x = int(commands[1])
            if commands[3] in dicx :
                y = dicx[commands[3]]
            else :
                y = int(commands[3])
            if '<' in commands :
                check = x < y
            elif '<=' in commands :
                check = x <= y
            elif '>' in commands :
                check = x > y
            elif '>=' in commands :
                check = x >= y
            elif '==' in commands :
                check = x == y
            elif '!=' in commands :
                check = x != y
            if check :
                i = locations[commands[-1].strip(':')]
                continue
                
        #moving
        if "MOV" in program[i]:
            partso = program[i].split(" ")
            if partso[2] in dicx :
                dicx[partso[1]] = dicx[partso[2]]
            else :
                dicx[partso[1]] = int(partso[2])
       
        # adding
        if "ADD" in program[i]:
            partsa = program[i].split(" ")
            if partsa[2] in dicx :
                dicx[partsa[1]] += dicx[partsa[2]]
            else :
                dicx[partsa[1]] += int(partsa[2])

        #subtaction
        if 'SUB' in program[i]:
            partss = program[i].split(" ")
            if partss[2] in dicx :
                dicx[partss[1]] -= dicx[partss[2]]
            else:
                dicx[partss[1]] -= int(partss[2])
            
        #multiplying
        if 'MUL' in program[i]:
            partsm = program[i].split(" ")
            if partsm[2] in dicx :
                dicx[partsm[1]] *= dicx[partsm[2]]
            else :
                dicx[partsm[1]] *= int(partsm[2])

        #print: adding the value to the final list
        if 'PRINT' in program[i]:
            partsp = program[i].split(" ")
            if partsp[1] in dicx :
                xctn.append(dicx[partsp[1]])
            else :
                xctn.append(int(partsp[1]))
        i += 1
    return xctn

def coordinates(program: list)-> dict:
    dic_to_return = {}
    for i in range(len(program)):
        parts = program[i].strip().split(" ")
        if len(parts) == 1 :
            dic_to_return[parts[0].strip(":")] = i
    return dic_to_return



