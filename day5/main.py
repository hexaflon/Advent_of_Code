
"""data = ["    [D]    \n",
"[N] [C]    \n",
"[Z] [M] [P]\n",
" 1   2   3\n",
"\n",
"move 1 from 2 to 1\n",
"move 3 from 1 to 3\n",
"move 2 from 2 to 1\n",
"move 1 from 1 to 2\n"]"""



with open("input.txt") as file:
 data = file.readlines()

for i in range(0,len(data)):
    if "1" in data[i]:
        cargo = data[:i+1]
        data = data[i+2:]
        break

#print(cargo)
#print(data)
ammount_of_stacks = cargo[-1]
cargo = cargo[:-1]

#print(cargo)

stacks =[]
times = 0
number = "0"
changed = False

while ammount_of_stacks:

    if ammount_of_stacks[0] in "0123456789":
        number += ammount_of_stacks[0]
        ammount_of_stacks = ammount_of_stacks[1:]
        changed = False
    if ammount_of_stacks[0] == " " or ammount_of_stacks[0] == "" or ammount_of_stacks == "\n":
        ammount_of_stacks = ammount_of_stacks[1:]
        if not changed:
            changed = True
            times = int(number)
            number = ""
    elif len(ammount_of_stacks) == 1 or len(ammount_of_stacks) == 0:
        break


for i in range(0, times):
    stacks.append([])

for line in cargo:
    index = 0
    i = 0
    while i != len(line):
        if line[i]==" " and line[i+1]!="[":
            i+=3
            index += 1
        if line[i]=="[":
            stacks[index].append(line[i+1])
            index += 1
            i+=2
        i+=1

#part 1
"""def move_crates(ammount, from_crate, to_crate, crates):
    while ammount != 0:
        print(crates)
        if crates[from_crate] is not None:
            ammount -= 1
            crates[to_crate] = list(crates[from_crate][0]) + crates[to_crate]
            crates[from_crate] = crates[from_crate][1:]

        else:
            ammount -= 1
    return crates


for command in data:
    #print(command)
    command = command[5:]
    ammount = int(command[:command.find(" ")])
    #print(ammount)
    command = command[command.find(" ")+1+5:]
    from_crate = int(command[:command.find(" ")])
    #print(from_crate)
    command = command[command.find(" ")+1+3]
    to_crate = int(command)
    #print(to_crate)

    stacks = move_crates(ammount, from_crate-1, to_crate-1, stacks)"""


#part 2
def move_crate(ammount, from_crate, to_crate, crates):

    print(crates)
    if crates[from_crate] is not None:
        ammount -= 1
        crates[to_crate] = list(crates[from_crate][0]) + crates[to_crate]
        crates[from_crate] = crates[from_crate][1:]

    else:
        ammount -= 1
    return crates

def move_crates(ammount, from_crate, to_crate, crates):
    print(crates)
    if crates[from_crate] is not None:
        if len(crates[from_crate]) < ammount:
            ammount = len(crates[from_crate])

        crates[to_crate] = list(crates[from_crate][0:ammount]) + crates[to_crate]
        crates[from_crate] = crates[from_crate][ammount:]
    return crates



for command in data:
    #print(command)
    command = command[5:]
    ammount = int(command[:command.find(" ")])
    #print(ammount)
    command = command[command.find(" ")+1+5:]
    from_crate = int(command[:command.find(" ")])
    #print(from_crate)
    command = command[command.find(" ")+1+3]
    to_crate = int(command)
    #print(to_crate)
    if ammount == 1:
        stacks = move_crate(ammount, from_crate-1, to_crate-1, stacks)
    else:
        stacks = move_crates(ammount, from_crate - 1, to_crate - 1, stacks)

answer = ""
for i in stacks:
    answer += i[0][0]
print(answer)