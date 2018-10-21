import operator

class Ant:
	def __init__(self, p, r):
		self.t = 0		  # The local time for the ant
		self.p = p 		  # The position of the ant
		self.op = p 	  # The original position
		self.r = r 		  # True if the ant is headed right
		self.alive = True # If the ant has fallen off or not

	def age(self, t):
		"""
		Walk and age the ant t time units. Assumes no obstacles.
		"""
		self.t += t
		if self.r:
			self.p += t
		else:
			self.p -= t

	def die(self):
		"""
		Marks the ant as fallen off the edge (or dead)
		"""
		self.alive = False

	def turn(self):
		self.r = not self.r

	def __str__(self):
		return 'Ant(' + str(self.op) + " - " + str(self.p) + " @ " + str(self.t) + ", " + ('R' if self.r else 'L') + ')'

def get_ants():
	"""
	Reads the ants from stdin
	"""
	try:
		line = input().split(' ')
		L, A = int(line[0]), int(line[1])
		ants = []
		for _ in range(A):
			line = input().split(' ')
			p, r = int(line[0]), line[1] == 'R'
			ants.append( Ant(p, r) )
		# Make sure the ants are in order
		ants.sort(key=operator.attrgetter('p'))
		return L, ants
	except EOFError:
		pass
	return None, None

def printt(ants):
	"""
	Prints the ants array
	"""
	ants = [str(a) for a in ants]
	print(ants)

def is_path_clear(ants, i):
	"""
	Determines if the path to the edge is clear or if you have to bump
	another ant first.
	"""
	if ants[i].r:
		return all(ants[k].r for k in range(i, len(ants)))
	return all(not ants[k].r for k in range(i))

def distance_to_edge(L, ants, i):
	"""
	Returns the distance the i:th ant has left to the edge.
	"""
	if ants[i].r:
		return L - ants[i].p
	return ants[i].p

def get_neighbour(ants, i):
	"""
	Returns the neighbour the ant is looking at.
	"""
	if ants[i].r:
		return i + 1
	return i - 1

def bump(ants, i, k):
	"""
	Bumps the two ants. Assumes they are at the same place in time.
	"""
	# Ants will meet at the very middle between them.
	d = abs(ants[i].p - ants[k].p) / 2
	# Walk, or age, the ants
	ants[i].age(d)
	ants[k].age(d)
	# Since they bumped into eachother, turn them around
	ants[i].turn()
	ants[k].turn()

def sync(ants, i, k):
	"""
	Assumes the ants are moving towards eachother.
	"""
	diff = ants[i].t - ants[k].t
	if diff >= 0:
		# The i:th ant has been alive longer, move other ant
		ants[k].age(diff)
	else:
		ants[i].age(-diff)

def walk(L, ants, i):
	"""
	Walks the i:th ant to the edge.
	"""
	while ants[i].alive:
		clear_path = is_path_clear(ants, i)
		if clear_path:
			d = distance_to_edge(L, ants, i)
			ants[i].age(d)
			ants[i].die()
			return
		# We have to bump another ant first
		neighbour = get_neighbour(ants, i)
		if ants[neighbour].r == ants[i].r:
			# We are moving in the same direction and we have to turn the neighbour
			# around first.
			walk(L, ants, neighbour)
		else:
			# The ants are moving towards eachother, make sure they are
			# in the same timespan
			sync(ants, i, neighbour)
			# Bump the ants
			bump(ants, i, neighbour)

def get_last_ant(L, ants):
	for i in range(len(ants)):
		walk(L, ants, i)
	for i in reversed(range(len(ants))):
		walk(L, ants, i)

def get_oldest(ants):
	"""
	Returns the oldest ants
	"""
	oldest = []
	for a in ants:
		if oldest == [] or oldest[0].t <= a.t:
			if len(oldest) > 0 and oldest[0].t < a.t:
				oldest = []
			oldest.append(a)
	oldest.sort(key=operator.attrgetter('op'))
	return oldest

while True:
	L, ants = get_ants()
	if L is None or ants is None:
		break

	get_last_ant(L, ants)
	oldest = get_oldest(ants)

	t = oldest[0].t
	if (t * 1.0).is_integer():
		t = int(t)
	op = ' and '.join([ str(a.op) for a in oldest ])

	print("The last ant will fall down in " + str(t) + " seconds - started at " + op + ".")
