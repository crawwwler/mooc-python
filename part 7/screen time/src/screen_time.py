from datetime import datetime, timedelta

fn = input("Filename:") 

sd = input("Starting date:") # date from

hmd = int(input("How many days:"))

timelist = [] # list to store screentimes

x = 0 # for loop

alltimes = 0 # sum of all screen times

start = datetime.strptime(sd, "%d.%m.%Y") # date in format

dayplus = timedelta(days=1) # day plus one

wholeplus = timedelta(days=(hmd-1)) # start day + number of days 

finish = start + wholeplus # date of last day

matn = "Screen time " + start.strftime("%d.%m.%Y") # string for asking the screentimes

print("Please type in screen time in minutes on each day (TV computer mobile):") 

# in loop we take the screentimes , append the string to list then calculate the sum of screentimes
while x < hmd :
    times = input(matn)
    timelist.append(times)
    parts = times.split(" ")
    for p in parts :
        alltimes += int(p)
    start += dayplus
    x +=1

start = datetime.strptime(sd, "%d.%m.%Y")
# conveting the format to the one we should print in
for i in range(len(timelist)) :
    x = timelist[i].replace(" ", "/")
    timelist[i] = x

# making the file 
with open(fn, "w") as ff :
    ff.write("Time period: " + start.strftime("%d.%m.%Y") + "-" + finish.strftime("%d.%m.%Y") + "\n")
    ff.write(f"Total minutes: {alltimes}\n")
    ff.write(f"Average minutes: {alltimes/hmd}\n")
    for i in timelist:
        ff.write(start.strftime("%d.%m.%Y") + ": " + i + "\n")
        start +=dayplus
print(f"Data stored in file {fn}")