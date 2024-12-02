with open('day2.txt') as f:
    l = [[*map(int, line.split())] for line in f]
unsafe = 0
for r in l:
    k = [r[i]-r[i-1]for i in range(1,len(r))]
    if (0 < sum(x<0 for x in k) < len(k)) or any(not x or abs(x)>3 for x in k):
        unsafe += 1
print(len(l)-unsafe)