def counter(file, right, down):
	i = 0
	linenumber = 0
	counter = 0

	for line in file:
		index = i%31
		if linenumber%down == 0:
			if line[index]=="#":
				counter += 1
			i = i+right
		# print i
		linenumber+=1
	return counter

linenumber = 0
listfile = []
with open("input.txt") as file:
	for line in file:
		listfile.append(line)

res1 = counter(listfile,1,1)
res2 = counter(listfile,3,1)
res3 = counter(listfile,5,1)
res4 = counter(listfile,7,1)
res5 = counter(listfile,1,2)

print res1*res2*res3*res4*res5
