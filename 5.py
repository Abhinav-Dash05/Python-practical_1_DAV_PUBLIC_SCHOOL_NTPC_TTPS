y = int(input("ENTER YEAR: "))
m = y%4

if(m == 0):
    print(f"{y} is a leap year")
else:
    print(f"{y} is a not leap year")