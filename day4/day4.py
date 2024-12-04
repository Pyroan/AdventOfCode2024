with open('day4.txt') as f:
    grid = [list(s.strip()) for s in f]


def search(grid, x, y, xdelta, ydelta):
    '''
    xdelta and ydelta define what direction we're searching in.
    '''
    s = ''
    for i in range(4):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        s += grid[x][y]
        x += xdelta
        y += ydelta

    return s == 'XMAS'


count = 0
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            for d in directions:
                count += search(grid, i, j, d[0], d[1])
print(count)
