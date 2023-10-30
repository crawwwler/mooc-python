from datetime import datetime,timedelta

def millenium(year:int, month: int, day: int):
    m = datetime(1999,12,31)
    x = datetime(year,month,day)
    ans = m - x
    dt = timedelta(days=0)
    #print(ans)
    if ans < dt :
        return "You weren't born yet on the eve of the new millennium."

    return f"You were {ans.days} days old on the eve of the new millennium."


day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))
print(millenium(year,month,day))
