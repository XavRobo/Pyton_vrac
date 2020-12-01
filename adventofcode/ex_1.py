with open("inputs/input1.txt", "r", encoding="utf-8") as g:
    data = list(map(int, g.readlines()))

data.sort()
print(data)

forw = 0
back  = 1

while(1):
    sum = data[-back]+data[forw]
    if(sum == 2020):
        print(data[-back],data[forw])
        print(data[-back]*data[forw])
        break
    elif(sum < 2020):
        forw += 1
    else:
        back += 1
