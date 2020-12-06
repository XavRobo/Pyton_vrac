import re

L = []
with open("inputs/input4.txt", "r", encoding="utf-8") as f:
    L= f.read().split("\n\n")

keys = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
eyc = ["amb","blu","brn","gry","grn","hzl","oth"]
counter = 0

#Part One
# for l in L:
#     if(all(key in l for key in keys )):
#         counter += 1



#Part Two
for l in L:
    if(all(key in l for key in keys )):
        val = re.split(' |\n',l)
        dic = {}
        for a in val:
            key,v = a.split(":")
            dic.update({key:v})
        if(1920<=int(dic["byr"])<=2002 and 2010<=int(dic["iyr"])<=2020 and 2020<=int(dic["eyr"])<=2030 and ((dic["hgt"][-2:]=="cm" and 150 <= int(dic["hgt"][:-2])<= 193) or (dic["hgt"][-2:]=="in" and 59 <= int(dic["hgt"][:-2])<= 76)) and (len(dic["hcl"])==7 and dic["hcl"][0] == "#" and dic["hcl"][1:].isalnum()) and (dic["ecl"] in eyc) and len(dic["pid"]) == 9):
            counter += 1

print(counter)