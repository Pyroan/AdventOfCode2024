signum=lambda a:-(a<0)or a>0

def is_safe(r):
    diffs = [r[i]-r[i-1]for i in range(1,len(r))]
    dampened = False
    for i,diff in enumerate(diffs):
        if signum(diff) != signum(diffs[0]) or diff == 0 or abs(diff) > 3:
            if dampened:
                return False
            if i<len(diffs)-1:
                diffs[i+1]+=diff
            dampened = True
    return True

with open('day2.txt') as f:
    l = [[*map(int, line.split())] for line in f]
print(sum(is_safe(report)or is_safe([*reversed(report)]) for report in l))