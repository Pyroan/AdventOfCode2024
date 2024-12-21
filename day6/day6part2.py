# It's a loop if you're ever in the same cell with the same heading.
# hopefully tyhis won't become a mess, spacially.
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Guard:

    def __init__(self, x, y, heading=UP):
        self.x = x
        self.y = y
        self.heading = heading
        self.history = []

    def next_cell(self):
        if self.heading == UP:
            return self.x-1, self.y
        elif self.heading == RIGHT:
            return self.x, self.y+1
        elif self.heading == DOWN:
            return self.x+1, self.y
        elif self.heading == LEFT:
            return self.x, self.y-1

    def is_in_bounds(self, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def step(self):
        newX, newY = self.next_cell()
        if self.is_in_bounds(newX, newY) and grid[newX][newY] == '#':
            self.heading = (self.heading + 1) % 4
        else:
            self.x, self.y = newX, newY
        # brutey brute brute
        # nvm brute ain't gonna cut it ugh.
        entry = [self.x, self.y, self.heading]
        if entry in self.history:
            # loop detected.
            return True
        self.history.append([self.x, self.y, self.heading])
        return False


with open('day6.txt') as f:
    main_grid = [*map(list, map(str.strip, f.readlines()))]
guardX = 0
guardY = 0
# find the guard
for i in range(len(main_grid)):
    for j in range(len(main_grid[i])):
        if main_grid[i][j] == '^':
            guardX = i
            guardY = j

total = 0
grid = []
for i in range(len(main_grid)):
    for j in range(len(main_grid[0])):
        guard = Guard(guardX, guardY)
        grid = [l[:] for l in main_grid]
        if grid[i][j] != '.':
            continue
        grid[i][j] = '#'
        while (guard.is_in_bounds(guard.x, guard.y)):
            if guard.step():
                total += 1
                break
print(total)
