
def cost(a, b):
    return abs(a[0] - b[0]) + abs(a[1] + b[1])

def astar(m, start, goal, wall):
    """
    Credit to whoever wrote the pseudocode found on wikipedia
    """
    if m[start[0]][start[1]] == wall: return False
    if m[goal[0]][goal[1]] == wall: return False

    closedSet = set()
    openSet = {start}
    cameFrom = dict()
    gScore = dict()
    gScore[start] = 0
    fScore = dict()

    fScore[start] = cost(start, goal)

    while len(openSet):
        tmp = { k: fScore[k] for k in openSet  }
        current = min(tmp, key=tmp.get) # the node in openSet having the lowest fScore[] value

        if current == goal:
            return True

        openSet.remove(current)
        closedSet.add(current)

        for neigh in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            neighbor = (current[0] + neigh[0], current[1] + neigh[1])

            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > len(m) - 1 or neighbor[1] > len(m[0]) - 1:
                continue

            if m[neighbor[0]][neighbor[1]] == wall:
                continue

            if neighbor in closedSet:
                continue

            tentative_gScore = gScore[current] + cost(current, neighbor)

            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue

            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + cost(neighbor, goal)
    return False

def can_move(m, p1, p2):
    bin = astar(m, p1, p2, 1)
    dec = astar(m, p1, p2, 0)

    if bin: print("binary")
    elif dec: print("decimal")
    else: print("neither")

r, c = map(int, input().split(" "))

m = []

for i in range(r):
    m.append(list(map(int, list(input()))))

n = int(input())

for i in range(n):
    r1, c1, r2, c2 = map(int, input().split(" "))

    can_move(m, (r1-1, c1-1), (r2-1, c2-1))
