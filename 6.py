n1 = int(input("ENTER NUMBER 1: "))
n2 = int(input("ENTER NUMBER 2: "))

o = n1%n2

if(o==0):
    print(f"{n1} is fully divisible by {n2}")
else:
    print(f"{n1} is not divisible by {n2}")