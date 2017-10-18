grid = [
	[int(a) for a in input().split(' ')],
	[int(a) for a in input().split(' ')],
	[int(a) for a in input().split(' ')],
	[int(a) for a in input().split(' ')]
]

direction = int(input())

newGrid = [
	[False] * 4,
	[False] * 4,
	[False] * 4,
	[False] * 4
]

DIR_LEFT = 0
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3

if direction == DIR_RIGHT or direction == DIR_LEFT:
	for y in range(4):
		for x in (reversed(range(4)) if direction == DIR_RIGHT else range(4)):
			c = x
			while (c < 3 if direction == DIR_RIGHT else c > 0) and grid[y][c+(1 if direction == DIR_RIGHT else -1)] == 0 and not newGrid[y][c+(1 if direction == DIR_RIGHT else -1)]:
				c = c + (1 if direction == DIR_RIGHT else -1)
			if (c < 3 if direction == DIR_RIGHT else c > 0) and grid[y][c+(1 if direction == DIR_RIGHT else -1)] == grid[y][x] and not newGrid[y][c+(1 if direction == DIR_RIGHT else -1)]:
				c = c + (1 if direction == DIR_RIGHT else -1)
			if not c == x and (grid[y][c] == grid[y][x] or grid[y][c] == 0):
				newGrid[y][c] = not grid[y][c] == 0
				grid[y][c] = grid[y][c] + grid[y][x]
				grid[y][x] = 0

elif direction == DIR_UP or direction == DIR_DOWN:
	if direction == DIR_DOWN:
		direction = DIR_RIGHT
	else:
		direction = DIR_LEFT
	for y in range(4):
		for x in (reversed(range(4)) if direction == DIR_RIGHT else range(4)):
			c = x
			while (c < 3 if direction == DIR_RIGHT else c > 0) and grid[c+(1 if direction == DIR_RIGHT else -1)][y] == 0 and not newGrid[c+(1 if direction == DIR_RIGHT else -1)][y]:
				c = c + (1 if direction == DIR_RIGHT else -1)
			if (c < 3 if direction == DIR_RIGHT else c > 0) and grid[c+(1 if direction == DIR_RIGHT else -1)][y] == grid[x][y] and not newGrid[c+(1 if direction == DIR_RIGHT else -1)][y]:
				c = c + (1 if direction == DIR_RIGHT else -1)
			if not c == x and (grid[c][y] == grid[x][y] or grid[c][y] == 0):
				newGrid[c][y] = not grid[c][y] == 0
				grid[c][y] = grid[c][y] + grid[x][y]
				grid[x][y] = 0

for a in grid:
	a = ' '.join(map(str, a))
	print(a)