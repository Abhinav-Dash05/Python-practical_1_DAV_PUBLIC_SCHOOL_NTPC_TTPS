import math


x = int(input("ENTER NUMBER x: "))
y = int(input("ENTER NUMBER y: "))
z = int(input("ENTER NUMBER z: "))

a = 4*x**4+3*y**3+9*z+6*math.pi

print(f"THE VALUE IN EXPRESSION 4x^4+3y^3+9z+6: {a}")
print(math.pow(x, y))