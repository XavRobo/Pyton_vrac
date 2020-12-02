import re

with open("inputs/input2.txt", "r", encoding="utf-8") as g:
    data = list(map(str, g.readlines()))

count = 0
#PART ONE
# for d in data:
#     line = re.split('-|: | ',d[:-1])
#     if(int(line[0]) <= line[3].count(line[2]) <=  int(line[1])):
#         count += 1

#PART TWO
for d in data:
    line = re.split('-|: | ',d[:-1])
    if((line[3][int(line[0])-1]==line[2]) ^ (line[3][int(line[1])-1]==line[2])):
        count += 1

print(count)
