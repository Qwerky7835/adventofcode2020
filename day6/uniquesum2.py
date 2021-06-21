responses = {}
sums = []
counter = 0

with open("input.txt") as file:
	for line in file:
		if line[0] == '\n':
			groupcounter = 0
			for key in responses:
				if responses[key]==counter:
					groupcounter+=1
			sums.append(groupcounter)
			
			responses.clear()
			counter = 0
		else:
			line = line[:-1]
			counter+=1

			for letter in line:
				if letter in responses:
					responses[letter] += 1
				else:
					responses[letter] = 1

print(sum(sums))
