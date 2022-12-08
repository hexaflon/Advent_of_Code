with open("input.txt") as file:
    data = file.readlines()

#data = ["A Y\n","B X\n","C Z\n"]

dictionary = {
    "Y": 3,
    "X": 0,
    "Z": 6
}

conditions = {
    "YA":4,
    "YB":5,
    "YC":6,
    "XA":3,
    "XB":1,
    "XC":2,
    "ZA":8,
    "ZB":9,
    "ZC":7
}


"""
dictionary = {
    "Y": 2,
    "X": 1,
    "Z": 3
}

conditions ={
    "AY": 6,
    "BY": 3,
    "CY": 0,
    "AX": 3,
    "BX": 0,
    "CX": 6,
    "AZ": 0,
    "BZ": 6,
    "CZ": 3
}
"""

def warunki(op, me):
    res = 0
    res += conditions[me+op]
    #res += dictionary[me]
    return res


p1 = ""
p2 = ""
points = 0

for choice in data:
    p1 = choice[0]
    p2 = choice[2]
    points += warunki(p1, p2)

print(points)

