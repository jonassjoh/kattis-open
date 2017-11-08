import functools

class Ant:
	def __init__(self, position, d):
		self.position = position
		self.d = d
		self.index = position
		self.dead = False

	def right(self):
		return self.d

	def turnRight(self):
		self.d = True

	def turnLeft(self):
		self.d = False

	def move(self, time, L):
		if self.right():
			self.position += time
			if self.position >= L:
				self.dead = True
				return True
		else:
			self.position -= time
			if self.position <= 0:
				self.dead = True
				return True
		return False

	def __str__(self):
		return "position: " + str(self.position) + ((", going " + ("right" if self.d else "left")) if not self.dead else ", dead")

def customsort(a1, a2):
	return a1.position - a2.position

def get_ants():
	tmp = ''
	try:
		tmp = input().strip().split(' ')
	except EOFError:
		return -1, []
	L = int(tmp[0])
	A = int(tmp[1])
	ants = []
	for _ in range(A):
		tmp = input().strip().split(' ')
		position = int(tmp[0])
		d = tmp[1] == 'R' 
		ants.append(Ant(position, d))
	ants = sorted(ants, key=functools.cmp_to_key(customsort))
	return L, ants

L = 0
while not L == -1: # For EOF

	L, ants = get_ants()
	if L != -1:

		alive_left = 0
		alive_right = len(ants) - 1

		def will_meet(ants, ant1, ant2):
			return abs(ants[ant1].position - ants[ant2].position) / 2

		def move_ants(ants, time, L):
			global alive_left, alive_right
			dead = []
			for i in range(alive_left, alive_right+1):
				died = ants[i].move(time, L)
				if died:
					dead.append(i)
					if i == alive_left:
						alive_left += 1
					else:
						alive_right -= 1
			return dead


		def turn_ants(ants):
			global alive_left, alive_right
			i = alive_left
			while i < alive_right+1:
				if i < alive_right:
					if ants[i].position == ants[i+1].position:
						ants[i].turnLeft()
						ants[i+1].turnRight()
						i += 1 # Skip next one

				i += 1

		def will_walk_off(L, ants):
			global alive_left, alive_right

			min_time = 200000 # INF
			min_i = -1
			
			i = alive_left
			while i < alive_right+1:

				# First ant will die
				if i == alive_left and not ants[i].right():
					time = ants[i].position
					if time < min_time:
						min_time = time
						min_i = i

				# Last ant will die
				if i == alive_right and ants[i].right():
					time = L - ants[i].position
					if time < min_time:
						min_time = time
						min_i = i

				# Two ants will meet eachother
				if i < alive_right:
					if ants[i].right() and not ants[i+1].right():
						time = will_meet(ants, i, i+1)
						if time < min_time:
							min_time = time
							min_i = i
				if i > alive_left:
					if not ants[i].right() and ants[i-1].right():
						time = will_meet(ants, i, i-1)
						if time < min_time:
							min_time = time
							min_i = i
				i += 1

			# min_time is the first instance where some ants will meet
			died = move_ants(ants, min_time, L)
			turn_ants(ants)
			return died, min_time

		t = []
		tot_time = 0
		while alive_left <= alive_right:
			t, time = will_walk_off(L, ants)
			tot_time += time

		tot_time = int(tot_time)
		
		for i in range(len(t)):
			t[i] = ants[t[i]].index

		print("The last ant will fall down in " + str(tot_time) + " seconds - started at " + str(t[0]) + ((' and ' + str(t[1]) + '.') if len(t) > 1 else '.'))