"""loops.py
Concise examples and small exercises demonstrating Python loops.

Run this file to see example output and to run basic assertions.
"""

def examples():
	# for loop: iterate list
	nums = [1, 2, 3, 4]
	s = 0
	for n in nums:
		s += n

	# for loop with range
	prod = 1
	for i in range(1, 5):
		prod *= i

	# enumerate
	pairs = []
	for idx, val in enumerate(['a', 'b', 'c'], start=1):
		pairs.append((idx, val))

	# while loop
	i = 0
	while i < 3:
		i += 1

	# break and continue
	found = None
	for x in range(10):
		if x % 2 == 0:
			continue
		if x == 7:
			found = x
			break

	# nested loops
	grid = []
	for r in range(3):
		row = []
		for c in range(2):
			row.append(r * 10 + c)
		grid.append(row)

	# list comprehension
	squares = [x * x for x in range(6)]

	return {
		'sum_nums': s,
		'prod_range': prod,
		'pairs': pairs,
		'while_end': i,
		'found': found,
		'grid': grid,
		'squares': squares,
	}


def exercises():
	# Exercise 1: sum of even numbers from 0..10 (inclusive)
	evens = sum(x for x in range(11) if x % 2 == 0)
	assert evens == 30, "Exercise1 failed"

	# Exercise 2: flatten a 2x3 grid using loops
	grid = [[1, 2, 3], [4, 5, 6]]
	flat = []
	for row in grid:
		for val in row:
			flat.append(val)
	assert flat == [1, 2, 3, 4, 5, 6], "Exercise2 failed"

	# Exercise 3: build dict from two lists using for + enumerate
	keys = ['a', 'b', 'c']
	vals = [10, 20, 30]
	mapping = {}
	for i, k in enumerate(keys):
		mapping[k] = vals[i]
	assert mapping == {'a': 10, 'b': 20, 'c': 30}, "Exercise3 failed"

	return True


def main():
	print('=== loop examples ===')
	out = examples()
	print('sum_nums ->', out['sum_nums'])
	print('prod_range ->', out['prod_range'])
	print('pairs ->', out['pairs'])
	print('while_end ->', out['while_end'])
	print('found ->', out['found'])
	print('grid ->', out['grid'])
	print('squares ->', out['squares'])

	print('\nRunning exercises (assertions)...')
	ok = exercises()
	if ok:
		print('All exercises passed.')


if __name__ == '__main__':
	main()

