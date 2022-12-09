"""data = 'nppdvjthqldpwncqszvftbrmjlhg'"""

with open("input.txt") as file:
    data = file.readline()

#part 1
"""for i in range(0, len(data)-4):
    #print(data[i:i+4])
    if len(set(data[i:i+4])) == 4:
        print(i+4)
        break"""


for i in range(0, len(data)-14):
    #print(data[i:i+14])
    if len(set(data[i:i+14])) == 14:
        print(i+14)
        break