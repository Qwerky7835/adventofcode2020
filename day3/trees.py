i = 0
counter = 0
with open("input.txt") as file:
	for line in file:
		index = i%31
		if line[index]=="#":
			counter+=1
		i = i+3

print(counter)
		