with open("day1.txt") as f:
    l = [*map(int,f.read().split())]
    a,b = sorted(l[::2]),sorted(l[1::2])
print(sum(abs(a[i]-b[i]) for i in range(len(a))))
