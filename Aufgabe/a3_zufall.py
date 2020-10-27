from random import randint

def spiel():
    wahl = str(input("Tipp: {'Z', 'K'}: "))
    wahl = wahl.capitalize()
    tipp = 0
    while 1:
        if(wahl == 'Z'):
            tipp = 1
            break
        elif(wahl == 'K'):
            tipp = 0
            break
        else:
            wahl = str(input("Nochmal Tipp: {'Z', 'K'}: "))
            wahl = wahl.capitalize()
    seite = randint(0,1)
    if(seite == 0):
        print("Kopf ist gefallen.")
    else:
        print("Zahl ist gefallen.")
    if(tipp == seite):
        print("Du hast gewonnen.")
    else:
        print("Du hast verloren.")

def d6_6(val):
    n6 = 0
    for i in range(0,val):
        n6 += 1
        while(randint(1,6)!=6):
            n6 += 1
    
    return n6/val

#spiel()
print(d6_6(10000))
