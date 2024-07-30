p = int(input("Enter principal amount: "))
r = int(input("Enter rate of intrest: "))
t = int(input("Enter time: "))

s = p*r*t/100
a = p+s
print(f"The total amout to be paid is {a}")