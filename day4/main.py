with open("input.txt") as file:
   data = file.readlines()

#data = ["2-4,6-8\n", "2-3,4-5\n", "5-7,7-9\n", "2-8,3-7\n", "6-6,4-6\n", "2-6,4-8\n"]
#part1
"""
def check(line):
    a_start = int(line[:line.find("-")])
    line = line[line.find("-")+1:]
    a_end = int(line[:line.find(",")])
    line = line[line.find(",")+1:]
    b_start = int(line[:line.find("-")])
    line = line[line.find("-")+1:]
    b_end = int(line[:len(line)])
    #print(a_start," ",a_end," ",b_start," ",b_end)
    if a_start <= b_start and a_end >= b_end:
        return 1
    if b_start <= a_start and b_end >= a_end:
        return 1
    if a_start == b_start and b_end == a_end:
        return 1
    return 0


res = 0
for assignment in data:
    res += check(assignment)
print(res)
"""

#part 2
def check(line):
    a_start = int(line[:line.find("-")])
    line = line[line.find("-")+1:]
    a_end = int(line[:line.find(",")])
    line = line[line.find(",")+1:]
    b_start = int(line[:line.find("-")])
    line = line[line.find("-")+1:]
    b_end = int(line[:len(line)])
    #print(a_start," ",a_end," ",b_start," ",b_end)
    if a_start>b_end or b_start > a_end:
        return 0

    return 1


res = 0
for assignment in data:
    res += check(assignment)
print(res)
