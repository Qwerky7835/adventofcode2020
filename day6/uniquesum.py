group = []
yes = set()

with open("input.txt") as file:
	for line in file:
		if line[0] == '\n':
			print(len(yes))
			group.append(len(yes))
			yes = set()
		else:
			line = line[:-1]
			for letter in line:
				yes.add(letter)
			print(yes)

print(sum(group))