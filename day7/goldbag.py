class bag:
	def __init__(self, name, child):
		self.name = name
		self.child = child

	# def setChildren(listofchildren):
	# 	self.child = listofchildren

	def getChildren(self):
		return self.child

	def getName(self):
		return self.name


def bag_parser(description):
	parent, child = description.split(" contain ")
	parent = parent[:-5]

	listofchildren = []
	child_description = child.split(", ")
	for i in child_description:
		description = i.split(" ")
		del description[-1]
		del description[0]
		listofchildren.append(" ".join(description))
	return [parent,listofchildren]

listofbags = []
with open("input.txt") as file:
	for line in file:
		result = bag_parser(line)
		bags = bag(result[0],result[1])
		listofbags.append(bags)

parent = ["shiny gold"]
bags_seen = set()

while len(parent) > 0:
	temp_seen = []
	for name in parent:
		for bag in listofbags:
			children = bag.getChildren()
			if name in children:
				temp_seen.append(bag)
				bags_seen.add(bag)
	parent = []
	for a in temp_seen:
		parent.append(a.getName())

print(len(bags_seen))



