from collections import Counter
with open("day1.txt") as f:
    l = [*map(int,f.read().split())]
    a,b = Counter(l[::2]),Counter(l[1::2])
print(sum(k*a[k]*b[k] for k in a.keys()))
