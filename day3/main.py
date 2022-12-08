#data = ["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n",
#        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n", "ttgJtRGJQctTZtZT\n", "CrZsJsPPZsGzwwsLwLmpwMDw\n"]

with open("input.txt") as file:
    data = file.readlines()


prio = {}

for i in range(1, 26+1):
    prio[chr(96+i)] = i

for i in range(27, 52+1):
    prio[chr(38+i)] = i
#part 1
"""
def check(rucksack):
    length = int((len(rucksack)-1)/2)
    item1 = rucksack[0:length]
    item2 = rucksack[length:len(rucksack)]

    letter = ""
    for i in range(0, length):
        if item1[i] in item2:
            letter = item1[i]
            break

    return prio[letter]


priority = 0

for rucksack in data:
    priority += check(rucksack)

print(priority)
"""


#part 2
def check(rucksack):
    letter = ""
    for i in range(0, len(rucksack[0])-1):
        if rucksack[0][i] in rucksack[1] and rucksack[0][i] in rucksack[2]:
            letter = rucksack[0][i]

            break

    return prio[letter]


priority = 0
rucksacks = []
for rucksack in data:
    if len(rucksacks) != 3:
        rucksacks.append(rucksack)
    if len(rucksacks) == 3:
        priority += check(rucksacks)
        rucksacks = []

print(priority)