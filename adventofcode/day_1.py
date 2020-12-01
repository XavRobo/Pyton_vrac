with open("inputs/input1.txt", "r", encoding="utf-8") as g:
    data = list(map(int, g.readlines()))

data.sort()

# Part one
# forw = 0
# back  = 1

# while(1):
#     sum = data[-back]+data[forw]
#     if(sum == 2020):
#         print(data[-back],data[forw])
#         print(data[-back]*data[forw])
#         break
#     elif(sum < 2020):
#         forw += 1
#     else:
#         back += 1

# Part two
sol = []
res = []
for a in range(0,len(data)):
    for b in range(0,len(data)):
        if(b != a and b  > a):
            for c in range(0,len(data)):
                if(c != a and c!= b and c > b):
                    if(data[a]+data[b]+data[c]==2020):
                        sol.append([data[a],data[b],data[c]])
                        res.append(data[a]*data[b]*data[c])

print(sol)
print(res)
