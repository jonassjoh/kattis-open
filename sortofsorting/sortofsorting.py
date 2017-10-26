import functools

def custom_cmp(x, y):
	if ord(x[0]) == ord(y[0]):
		return ord(x[1]) - ord(y[1])
	return ord(x[0]) - ord(y[0])

while True:
	n = int(input())
	if n == 0:
		break

	names = [input() for _ in range(n)]
	names = sorted(names, key=functools.cmp_to_key(custom_cmp))

	print('\n'.join(names), '\n')