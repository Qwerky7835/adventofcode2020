import string

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
counter = 0

def validate(code, stri):
	if code == 'byr':
		if stri.isdigit():
			intyear = int(stri)
			if intyear <= 2002 or intyear >= 1920:
				return True
	if code == 'iyr':
		if stri.isdigit():
			intyear = int(stri)
			if intyear <= 2020 or intyear >= 2010:
				return True
	if code == 'eyr':
		if stri.isdigit():
			intyear = int(stri)
			if intyear <= 2030 or intyear >= 2020:
				return True
	if code == 'hgt':
		if 'cm' in stri:
			if stri[:3].isdigit():
				intheight = int(stri[:3])
				if intheight <= 193 or intheight >= 150:
					return True
		if 'in' in stri:
			if stri[:2].isdigit():
				intheight = int(stri[:2])
				if intheight <= 76 or intheight >= 59:
					return True
	if code == 'hcl':
		if stri[0] == '#' and (all(c in string.hexdigits for c in stri)):
			return True
	if code == 'ecl':
		if len(stri) == 3 and (stri in 'amb blu brn gry grn hzl oth'):
			return True
	if code == 'pid':
		if len(stri) == 9 and stri.isdigit():
			return True
	return False


with open("input.txt") as file:
	for line in file:
		if line[0] == "\n":
			if (len(fields) == 0) or (len(fields)==1 and fields[0] == 'cid'):
				counter += 1
				print "here"
			fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
		else:
			listfields = line.split()
			for item in listfields:
				code = item[:3]
				inputseq = item[4:]
				if validate(code,inputseq):
					fields.remove(code)
				else:
					break

if (len(fields) == 0) or (len(fields)==1 and fields[0] == 'cid'):
				counter += 1
				
print counter 

