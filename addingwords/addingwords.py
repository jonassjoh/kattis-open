from sys import stdin

values = {}

for line in stdin:
	line = line.strip()
	oldline = line
	if len(line) > 0:
		line = line.split(' ')
		if line[0] == 'def':
			values[line[1]] = int(line[2])
		elif line[0] == 'clear':
			values = {}
		else:
			ans = 'unknown'
			if line[1] in values:
				s = values[line[1]]

				line = line[2:-1]
				for i in range(int(len(line) / 2)):
					if line[i*2+1] not in values:
						s = 10000000
						break
					if line[i*2] == '-':
						s -= values[line[i*2+1]]
					else:
						s += values[line[i*2+1]]

				for key, v in values.items():
					if v == s:
						ans = key
						break

			print(oldline[5:] + ' ' + ans)