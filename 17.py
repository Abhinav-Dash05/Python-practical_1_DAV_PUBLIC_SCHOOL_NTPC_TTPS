import math

s1 = int(input("Enter perpendicular side length"))
s2 = int(input("Enter base side length"))

#sinx=p/h
#h=p/sinx
x = int(input("Enter angle between perpendicular and base"))

sinx = math.sin(x)
h = s1/sinx
print(h)