import re
with open('day3.txt') as f:
    matches = []
    enabled = True
    for m in re.finditer(r'(?:do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', f.read()):
        if m.group(0) == "do()":
            enabled = True
        elif m.group(0) == "don't()":
            enabled = False
        elif enabled:
            matches.append(int(m.group(1))*int(m.group(2)))
    print(sum(matches))
