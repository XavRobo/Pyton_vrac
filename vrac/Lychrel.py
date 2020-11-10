class Result:
    comp = 0
    suite = []

    def display(self):
        print("apres " + str(self.comp) + " iterations la suite de nombre convergente: ")
        print(self.suite)

def lychrel(x):
    res = Result()
    res.suite.append(x)
    compteur = 0
    string = str(x)
    nstring = string[::-1]
    while (string != nstring):
        val = int(string)+int(nstring)
        res.suite.append(val)
        string = str(val)
        nstring = string[::-1]
        compteur += 1
    res.comp = compteur
    return res

lychrel(89).display()

