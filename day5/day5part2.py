from functools import cmp_to_key

lut = {}
with open('day5.txt') as f:
    rules, updates = f.read().split('\n\n')
# preprocessing
for r in rules.split():
    a, b = map(int, r.split('|'))
    if a not in lut.keys():
        lut[a] = []
    lut[a].append(b)

# actual validation.


def isValid(update, lut):
    for i in range(len(update)):
        for j in range(i):
            if update[i] in lut and update[j] in lut[update[i]]:
                return False
    return True


def compare(a, b):
    if a == b:
        return 0
    if a in lut.keys() and b in lut[a]:
        return 1
    return -1


total = 0
for u in updates.split():
    pages = [*map(int, u.split(','))]
    if not isValid(pages, lut):
        pages = sorted(pages, key=cmp_to_key(compare))
        total += pages[len(pages)//2]
print(total)