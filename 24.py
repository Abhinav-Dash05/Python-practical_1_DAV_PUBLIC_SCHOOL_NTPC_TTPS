p = int(input("Enter principal amount: "))
r = int(input("Enter rate of intrest: "))
t = int(input("Enter time: "))

a = p*(1+(r/100))**t
print(f"The total amout to be paid is {a}")