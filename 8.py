x=int(input("ENTER A TWO DIGIT NUMBER: ")) #786
y = int(x//10) #78
z = x%10 #6
p = int(y//10) #7
q = y%10 #8
a = z*100
c = q*10
b = a+c+p
print(f"YOUR NUMBER RWRITTEN IN REVERSE IS: {b}")