with open('day4.txt') as f:
    grid = [list(s.strip()) for s in f]


def search(grid, x, y):
    '''
    This time a valid answer is any "A" diagonally adjacent to
    two M's and two S's, which (when read clockwise) must not be alternating.
    (i.e. they must be on the same side of the A, not diagonal to each other.)
    '''
    # we don't care about the outer edge of the grid anymore
    if x < 1 or x >= len(grid)-1 or y < 1 or y >= len(grid[0])-1:
        return False
    # get the corners
    rots = ''.join([grid[x-1][y-1], grid[x+1][y-1],
                   grid[x+1][y+1], grid[x-1][y+1]])
    # test all rotations.
    for i in range(4):
        if rots[i:]+rots[:i] == 'MMSS':
            return True
    return False


count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'A':
            count += search(grid, i, j)
print(count)
