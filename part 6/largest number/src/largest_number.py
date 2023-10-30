def largest():
    biggest = 0
    with open("numbers.txt") as num_file :
        for line in num_file :
            line = line.replace("\n", "")
            num = int(line)
            if num > biggest :
                biggest = num
    return biggest

