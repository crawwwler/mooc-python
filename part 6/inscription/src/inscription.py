name = input("Whom should i sign this to:")
fin = input("Where shall i save it:")

with open(fin, "w") as inscript :
    inscript.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
