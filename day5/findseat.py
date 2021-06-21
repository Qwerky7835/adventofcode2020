from binary import decode


seats = []
with open("input.txt") as file:
	for line in file:
		seats.append(decode(line))

seats.sort()
for i in range(1,len(seats)):
	if seats[i]-2 == seats[i-1]:
		print(seats[i]-1)
		break
