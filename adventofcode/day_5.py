from math import *

with open("inputs/input5.txt", "r", encoding="utf-8") as f:
    data = list(map(str, f.readlines()))

def mil(l,r):
    return (r-l)/2

pot = []

for d in data:
    l = 0
    r = 127
    row = 0
    for i in range(7):
        if(d[i]=="B"):
            l += floor(mil(l,r))
        else:
            r -= ceil(mil(l,r))
    row = r
    
    l = 0
    r = 7
    col = 0
    for j in range(3):
        if(d[j+7]=="R"):
            l += floor(mil(l,r))
        else:
            r -= ceil(mil(l,r))
    col = r
    pot.append(row*8+col)
#Part One
# print(max(pot))

#Part Two
seats = range(min(pot),max(pot))
print(list(set(seats) - set(pot)))