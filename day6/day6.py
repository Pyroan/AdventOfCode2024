# TURTLE TIME BAYBEE
# this implementation is cursed but i'm literally recovering from surgery don't @ me
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Guard:
    '''i know writing a class for this isn't my style but meh'''

    def __init__(self, x, y, heading=UP):
        self.x = x
        self.y = y
        self.heading = heading
        self.coverage = 0

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
            if grid[self.x][self.y] != 'X':
                grid[self.x][self.y] = 'X'
                self.coverage += 1
            self.x, self.y = newX, newY


with open('day6.txt') as f:
    grid = [*map(list, map(str.strip, f.readlines()))]
guard = Guard(0, 0)
# find the guard (i'm really feeling lazy)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '^':
            guard.x = i
            guard.y = j

while (guard.is_in_bounds(guard.x, guard.y)):
    guard.step()
print(guard.coverage)
