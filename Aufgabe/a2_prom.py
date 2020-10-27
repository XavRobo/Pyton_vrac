class Getraenke:
    volume = 1 #in liter
    volan_alk = 5 #in percent

    def __init__(self, vol, volan):
        self.volume = vol
        self.volan_alk = volan

    def m_alk(self):
        return 10 * self.volume * self.volan_alk * 0.8

biermix = Getraenke(float(input('Aufgenommene Flüssigkeitsmenge in Liter: ')), float(input('Alkoholgehalt des Getränks in Prozent: ')))

def blalkon(get, m_per, fac_red):
    return get.m_alk() / (m_per * fac_red)

print(biermix.m_alk())
print(blalkon(biermix, float(input('Körpermasse in kg: ')), 0.6))