
str_stack = [];

with open("input.txt", "r") as f:
    for line in f:
        str_stack.append(int(line.strip()))

while str_stack:
    temp = str_stack.pop()
    diff = 2020 - temp
    if diff in str_stack:
        print(temp*diff)
        break
    else:
        continue
