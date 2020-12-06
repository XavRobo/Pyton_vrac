L = []
with open("inputs/input6.txt", "r", encoding="utf-8") as f:
    L= f.read().split("\n\n")

counter = 0

# Part One
for l in L:
    s = set(l)
    s.discard('\n')
    counter += len(s)

# Part Two
# for l in L:
#     s = l.split("\n")
#     if(len(s)==1):
#         counter += len(s[0])
#     else:
#         res = set(s[0]).intersection(*[set(e) for e in s[1:]])
#         counter += len(res)

print(counter)