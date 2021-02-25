import numpy as np
import operator
import sys

files = ["a_", "b_", "c_", "d_", "e_", "f_"]

def solve(file):
	# Read each file
	score = 0
	print("Read " + file)
	with open(file) as f:
		content = f.read().splitlines()
	
	# Get first line
	N, M, lines = list(map(int, content[0].split(' ')))
	
	# Get array from the second line
	print("Parsing..")
	array = list(map(int, content[1].split(' ')))
	pos = 2
	for i in range(lines):
		# Read the next lines
		n = list(map(int, content[pos].split(' ')))
		pos += 1
	
	score = 0
	
	# solution = set()
	print("Writing..")
	with open("output/" + file.split('/')[1].replace(".in", "") + ".out", 'w+') as f:
		f.write(str(lines) + "\n")
		for i in range(lines):
			f.write("test" + "\n")
	return score
		
def main():
	# Solve all?
	if len(sys.argv) == 1:
		total = 0
		for file in files:
			total += solve("input/" + file + ".in")
		print("Total score: " + str(solve()))
	else:
		# Only one!
		print("Score for " + sys.argv[1] + ": " + str(solve(sys.argv[1])))

if __name__ == '__main__':
  main()

