import numpy as np
import operator
import sys
from solver import solve

files = ["a", "b", "c", "d", "e", "f"]

def read(file):
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
	return F, I, D, streets, mapping, cars

def readSolution(file):
	solve(file)
	F, I, D, streets, mapping, cars = read(file)
	
	with open("output/" + file.split('/')[1].replace(".txt", "") + ".out") as f:
		content = f.read().splitlines()
	m = int(content[0].split(' ')[0])
	print(m)
	pos = 1
	
	cycles = dict()
	for index in range(m):
		splitted = content[pos].split(' ')
		pos += 1
		inter = int(splitted[0])
		
		splitted = content[pos].split(' ')
		count = int(splitted[0])
		pos += 1
		
		tmp = []
		for j in range(count):
			splitted = content[pos].split(' ')
			pos += 1
			tmp.append((mapping[splitted[0]], int(splitted[1])))
		cycles[inter] = tmp
	return F, I, D, streets, cars, cycles
	
def simulate(file):
	F, I, D, streets, cars, cycles = readSolution(file)
	if False:
		sim = np.zeros((D + 1, I))
		for i in range(I):
			if not (i in cycles):
				for k in range(D + 1):
					sim[k][i] = -1
				continue
			count = 0
			#print("Fill " + str(i))
			while count <= D:
				#print("len=" + str(len(cycles[i])))
				for j in range(len(cycles[i])):
					#print("Put " + str(cycles[i][j][0]))
					for k in range(cycles[i][j][1]):
						if count == D + 1:
							break
						sim[count][i] = cycles[i][j][0]
						count += 1
					if count == D + 1:
						break
	cost = 0
	
	status = []#np.zeros((I,))
	for i in range(I):
		if not (i in cycles):
			status.append([-1, 0, 0])
		else:
			# (street, ptr, time left of ampel)
			status.append([cycles[i][0][0], 0, cycles[i][0][1] - 1])
	def next():
		for i in range(I):
			if i in cycles:
				# Should another
				if status[i][2] == 0:
					status[i][1] += 1
					if status[i][1] == len(cycles[i]):
						status[i][1] = 0
					# Change street
					status[i][0] = cycles[i][status[i][1]][0]
					
					# Change counter
					status[i][2] = cycles[i][status[i][1]][1] - 1
				else:
					status[i][2] -= 1
	#def cmp(t):
  #	for i in range(I):
	#		if status[i][0] != sim[t][i]:
  #				return False
	#	return True
	
	if False:
		for time in range(D + 1):
			if not cmp(time):
				print("Bad!")
				sys.exit(-1)
			next()
	
	cs = []
	for index in range(len(cars)):
		# (curr street, consume, ptr, won, last time)
		cs.append([cars[index][0], 0, 1, True, D + 1])
	for time in range(D + 1):
		#for i in range(I):
	 #		for 
		for index in range(len(cars)):
			if cs[index][4] != D + 1 or cs[index][3] == False:
				continue
			if time == D:
				if cs[index][1]:
					cs[index][3] = False
					continue
			if cs[index][1]:
				cs[index][1] -= 1
				continue
			if cs[index][2] == len(cars[index]):
				cs[index][4] = time
				continue
			#print("curr=" + status=" 
			if status[streets[cs[index][0]][1]][0] == cs[index][0]:
				cs[index][0] = cars[index][cs[index][2]]
				cs[index][1] = streets[cs[index][0]][3] - 1
				cs[index][2] += 1
		next()
	cost = 0
	for index in range(len(cars)):
		print("won=" + str(cs[index][3]) + " ptr=" + str(cs[index][2]) + " vs " + str(len(cars[index])) + " consume=" + str(cs[index][1]))
		if cs[index][3] and cs[index][2] == len(cars[index]) and (not cs[index][1]):
			cost += F + D - cs[index][4]
	if False:
		for index in range(len(cars)):
			#print("Now: " + str(index))
			
			time = 0
			ptr = 0
			curr = cars[index][ptr]
			ptr += 1
			
			if ptr == len(cars[index]):
				print("Already won!")
				cost += F + D
				continue
			won = True
			consume = 0
			while time <= D:
				if time == D:
					if consume:
						won = False
						break
				#print("time=" + str(time) + " curr=" + str(curr) + " consume=" + str(consume))
				if consume:
					consume -= 1
					time += 1
					continue
				
				if ptr == len(cars[index]):
					break
				
				if sim[time][streets[curr][1]] == curr:
					#print("\tchage to " + str(cars[index][ptr]) + " consume=" + str(streets[cars[index][ptr]][3] - 1))
					curr = cars[index][ptr]
					consume = streets[curr][3] - 1
					ptr += 1
				time += 1
			#print("ptr=" + str(ptr) + " vs " + str(len(cars[index])) + " consume=" + str(consume))
			if won and ptr == len(cars[index]) and (not consume):
				cost += F + D - time
	return cost

def main():
	# Solve all?
	if len(sys.argv) == 1:
		total = 0
		for file in files:
			total += simulate("input/" + file + ".txt")
		print("Total score: " + str(total))
	else:
		# Only one!
		print("Score for " + sys.argv[1] + ": " + str(simulate(sys.argv[1])))

if __name__ == '__main__':
  main()

