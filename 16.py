import random as r 
import statistics as s

a = r.randrange(0,99999999999999999999999999999999)
b = r.randrange(0,99999999999999999999999999999999)
c = r.randrange(0,99999999999999999999999999999999)
d = r.randrange(0,99999999999999999999999999999999)
e = r.randrange(0,99999999999999999999999999999999)
f = r.randrange(0,99999999999999999999999999999999)

n=(a,b,c,d,e,f)
mean = s.mean(n)
median = s.median(n)
mode = s.mode(n)
print(f"""
Mean: {mean}
Median: {median}
Mode: {mode}

""")