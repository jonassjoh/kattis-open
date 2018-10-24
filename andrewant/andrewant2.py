import operator

class Ant:
	def __init__(self, p, r):
		self.p = p 		  # The position of the ant
		self.r = r 		  # True if the ant is headed right
		self.t = -1		  # The calculated time of the ant
		self.i_l = -1     # last index of left list
		self.i_r = -1	  # First index of right list
		self.clear = None

	def __str__(self):
		return 'Ant(' + str(self.p) + ", " + ('R' if self.r else 'L') + ", ("+str(self.i_l)+", "+str(self.i_r)+")" + ')'

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

def path_clear(ants):
	"""
	Determines if the path to the edge is clear or if you have to bump
	another ant first.
	"""
	# if ants[i].r:
	# 	return all(ants[k].r for k in range(i, len(ants)))
	# return all(not ants[k].r for k in range(i))
	left = True
	right = True
	for i in range(len(ants)):
		ii = len(ants) - i - 1
		if not ants[i].r:
			ants[i].clear = left
		else:
			left = False
		if ants[ii].r:
			ants[ii].clear = right
		else:
			right = False
		if not left and not right:
			return

def distance_to_edge(L, ants, i):
	"""
	Returns the distance the i:th ant has left to the edge.
	"""
	if ants[i].r:
		return L - ants[i].p
	return ants[i].p

def get_left_and_right(ants):
	# left = [k for k in range(i) if ants[k].r]
	# right = [k for k in range(i + 1, len(ants)) if not ants[k].r]
	left = []
	right = []
	for i in range(len(ants)):
		ants[i].i_l = len(left) - 1
		ants[i].i_r = len(right) + 1
		if ants[i].r:
			left.append( i )
			ants[i].i_l = len(left) - 2
		else:
			right.append( i )
			ants[i].i_r = len(right) + 1
	return left, right

def get_last_bumper(L, ants, i, left, right):
	# left = left[:ants[i].i_l]
	# right = right[ants[i].i_r:]
	_r = min(len(right), ants[i].i_r)
	ll = max(0, ants[i].i_l)
	lr = len(right) - ants[i].i_r
	if ants[i].r:
		s = lr - ll
		if s <= 0:
			# Same dir
			return left[(ll - 1 - (lr + 1))]
		return right[_r + (ll)]
	else:
		s = ll - lr
		if s <= 0:
			return right[_r + (ll - 1)]
		return left[(ll - 1 - lr)]

def walk(L, ants, i, left, right):
	if ants[i].clear: # path_clear(ants, i):
		ants[i].t = distance_to_edge(L, ants, i)
		return
	# We need to bump atleast one ant
	k = get_last_bumper(L, ants, i, left, right)
	# The last ant that will cause us to bump should already be walking
	# towards us.
	ants[i].t = distance_to_edge(L, ants, k)

def get_last_ant(L, ants):
	"""
	Returns the oldest ants
	"""
	oldest = []
	left, right = get_left_and_right(ants)
	path_clear(ants)
	for i in range(len(ants)):
		walk(L, ants, i, left, right)
		a = ants[i]
		if oldest == [] or oldest[0].t <= a.t:
			if len(oldest) > 0 and oldest[0].t < a.t:
				oldest = []
			oldest.append(a)
	return oldest

def test():
	while True:
		L, ants = get_ants()
		if L is None or ants is None:
			break

		oldest = get_last_ant(L, ants)

		t = oldest[0].t
		if (t * 1.0).is_integer():
			t = int(t)
		p = ' and '.join([ str(a.p) for a in oldest ])

		print("The last ant will fall down in " + str(t) + " seconds - started at " + p + ".")

import cProfile
cProfile.run('test()')
