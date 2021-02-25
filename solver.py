import numpy as np
import operator
import sys
import math

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

	schedule = [dict() for i in range(I)]

	for car in cars:
		for street in car:
			value = streets[street][2]
			schedule[streets[street][1]][value] = schedule[streets[street][1]].get(value, 0)+1
	
	print(schedule)
	# solution = set()
	print("Writing..")
	with open("output/" + file.split('/')[1].replace(".txt", "") + ".out", 'w+') as f:
		f.write(str(sum(1 for intersection in schedule if len(intersection)>0)) + "\n")
		for i, intersection in enumerate(schedule):
			if len(intersection) > 0:
				f.write(str(i) + "\n")
				f.write(str(len(intersection)) + "\n")

				sum_cars = 0
				for number in intersection.values():
					sum_cars += number


				for element, number in intersection.items():
					result = math.ceil(D/120*number/sum_cars)
					f.write(element + " " + str(result) + "\n")

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

