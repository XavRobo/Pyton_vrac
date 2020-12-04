with open("inputs/input3.txt", "r", encoding="utf-8") as g:
    data = list(map(str, g.readlines()))

arbre1 = 0
x1 = 1
y = 1

arbre2 = 0
x2 = 3

arbre3 = 0
x3 = 5

arbre4 = 0
x4 = 7

arbre5 = 0
x5 = 1
y2 = 2

while(y<len(data)):
    if(data[y][x1]=="#"):
        arbre1 += 1
    x1 += 1
    x1 = x1%(len(data[y])-1)
    if(data[y][x2]=="#"):
        arbre2 += 1
    x2 += 3
    x2 = x2%(len(data[y])-1)
    if(data[y][x3]=="#"):
        arbre3 += 1
    x3 += 5
    x3 = x3%(len(data[y])-1)
    if(data[y][x4]=="#"):
        arbre4 += 1
    x4 += 7
    x4 = x4%(len(data[y])-1)
    y +=1

while(y2<len(data)):
    if(data[y2][x5]=="#"):
        arbre5 += 1
    x5 += 1
    x5 = x5%(len(data[y2])-1)
    y2 += 2

print("arbres: %d, %d, %d, %d, %d"%(arbre1,arbre2,arbre3,arbre4,arbre5))
arbre = arbre1*arbre2*arbre3*arbre4*arbre5
print("resultat: %d"%arbre)