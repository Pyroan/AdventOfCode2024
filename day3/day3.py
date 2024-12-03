import re
with open('day3.txt') as f:
    matches = []
    for m in re.finditer(r'mul\((\d+),(\d+)\)', f.read()):
        matches.append(int(m.group(1))*int(m.group(2)))
    print(sum(matches))
