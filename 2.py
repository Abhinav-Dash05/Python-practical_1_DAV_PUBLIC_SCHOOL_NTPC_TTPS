import statistics as s

M = int(input("ENTER TEMPERATURE ON MONDAY: "))
T = int(input("ENTER TEMPERATURE ON TUESDAY: "))
W = int(input("ENTER TEMPERATURE ON WEDNESDAY: "))
TH = int(input("ENTER TEMPERATURE ON THURSDAY: "))
F = int(input("ENTER TEMPERATURE ON FRIDAY: "))
SA = int(input("ENTER TEMPERATURE ON SATURDAY: "))
S = int(input("ENTER TEMPERATURE ON SUNDAY: "))

a = (M,T,W,TH,F,SA,S)
A = s.mean(a)
print(f"THE AVERAGE TEMPERATURE OF THE WEEK IS- {A}")