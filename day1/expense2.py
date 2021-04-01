
str_stack = [];

with open("input.txt", "r") as f:
    for line in f:
        str_stack.append(int(line.strip()))

for a in str_stack:
	for b in str_stack:
		diff = 2020 - a - b
		if diff in str_stack:
			print(diff*a*b)
			break
		else:
			continue 
