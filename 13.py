import random as r
import statistics as s

A = r.randrange(1, 100, 16)
B = r.randrange(1, 100, 16)
C = r.randrange(1, 100, 16)
D = r.randrange(1, 100, 16)
E = r.randrange(1, 100, 16)
F = r.randrange(1, 100, 16)

a = (A,B,C,D,E,F)
b = s.mean(a)
c = s.median(a)
d = s.mode(a)
print(a)
print(f"""
Mean: {b}
Median: {c}
Mode: {d}

""")