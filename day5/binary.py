import sys

def binaryboundary(difference, boundary, position):
	change = difference//2
	if position == 'F' or position == 'L':
		#print(str(position) + ": "+str(boundary))
		return boundary - change -1
	else:
		#print(str(position) + ": "+str(boundary))
		return boundary + change + 1



def decode(seatstr):
	row = seatstr[:7]
	col = seatstr[7:10]

	row_upper = 127
	row_lower = 0
	col_left = 0
	col_right= 7

	for letter in row:
		difference = row_upper-row_lower
		if letter == 'F':
			row_upper = binaryboundary(difference, row_upper, 'F')
		else:
			row_lower = binaryboundary(difference, row_lower, "B")

	if row_upper == row_lower:
		print('correct row')
	else:
		raise Exception("row convergence failed")


	for letter in col:
		difference = col_right-col_left
		if letter == 'L':
			col_right = binaryboundary(difference, col_right, 'L')
		else:
			col_left = binaryboundary(difference, col_left, "R")

	if col_left == col_right:
		print("correct seat")
	else:
		raise Exception("seat convergence failed")

	return row_upper*8+col_right

maxID = 0
with open("input.txt") as file:
	for line in file:
		seatID = decode(line)
		if seatID > maxID:
			maxID=seatID


print(maxID)
