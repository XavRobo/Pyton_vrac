import re

L = []
with open("inputs/input4.txt", "r", encoding="utf-8") as f:
    L= f.read().split("\n\n")

keys = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
counter = 0

#Part One
# for l in L:
#     if(all(key in l for key in keys )):
#         counter += 1

#Part Two
for l in L:
    if(all(key in l for key in keys )):
        val = re.split(' |\n',l)
        print(val)
        dic = {}
        for a in val:
            key,v = a.split(":")
            dic.update({key:v})
        if(1920<=dic["byr"]<=2002 and 2010<=dic["iyr"]<=2020 and 2020<=dic["eyr"]<=2030)

print(counter)