import numpy as np
import operator
import sys

files = ["a", "b", "c", "d", "e", "f"]

def solve(file):
	# Read each file
	score = 0
	print("Read " + file)
	with open(file) as f:
		content = f.read().splitlines()
	
	# Get first line
	D, I, S, V, F = list(map(int, content[0].split(' ')))
	
	# Get array from the second line
	print("Parsing..")
	pos = 1
	streets = list()
	mapping = dict()
	for i in range(S):
		# Read the next lines
		splitted = content[pos].split(' ')
		B = int(splitted[0])
		E = int(splitted[1])
		name = splitted[2]
		mapping[name] = i
		L = int(splitted[3])
		streets.append((B, E, name, L))
		pos += 1
	cars = list()
	for i in range(V):
		splitted = content[pos].split(' ')
		p = int(splitted[0])
		
		tmp = []
		for j in range(p):
			tmp.append(mapping[splitted[1 + j]])
		cars.append(tmp)
		pos += 1
	score = 0
	
	print("streets=" + str(streets))
	print("cars=" + str(cars))
	
	# solution = set()
	print("Writing..")
	with open("output/" + file.split('/')[1].replace(".txt", "") + ".out", 'w+') as f:
		f.write(str(0) + "\n")
		for i in range(0):
			f.write("test" + "\n")
	return score
		
def main():
	# Solve all?
	if len(sys.argv) == 1:
		total = 0
		for file in files:
			total += solve("input/" + file + ".txt")
		print("Total score: " + str(total))
	else:
		# Only one!
		print("Score for " + sys.argv[1] + ": " + str(solve(sys.argv[1])))

if __name__ == '__main__':
  main()

