#
with open("input.txt") as file:
    data = file.readlines()

for linia in data:
    print(linia)
#1st part
"""
max = 0
elf = 0

for food in data:
    if food != "\n":
        elf += int(food)
    else:
        if max < elf:
            max = elf
        elf=0
"""
#2nd part


max = []
max.append(0)
elf = 0
for food in data:
    if food != "\n":
        elf += int(food)
    else:
        max.append(elf)
        elf = 0
max.sort(reverse=True)

print(sum(max[0:3]))