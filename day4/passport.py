fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
counter = 0

with open("input.txt") as file:
	for line in file:
		if line[0] == "\n":
			print fields
			if (len(fields) == 0) or (len(fields)==1 and fields[0] == 'cid'):
				counter += 1
				print "here"
			fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
		else:
			listfields = line.split()
			for item in listfields:
				code = item[:3]
				if code in fields:
					fields.remove(code)

if (len(fields) == 0) or (len(fields)==1 and fields[0] == 'cid'):
				counter += 1

print counter 

