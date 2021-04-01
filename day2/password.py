def process(param):
	results = []
	rangenumbers = param[0].split("-")
	results.append(int(rangenumbers[0]))
	results.append(int(rangenumbers[1]))
	results.append(param[1][0])
	results.append(param[2])
	return results

i = 0
i2 = 0
with open("input.txt") as file:
	for line in file:
		lis = line.split()
		result = process(lis)
		appearance = result[3].count(result[2])
		if ((appearance >= result[0]) and (appearance <= result[1])):
			i=i+1
		if (bool(result[2] == result[3][result[0]-1]) != bool(result[2] == result[3][result[1]-1])):
			i2 = i2+1

print i, i2


