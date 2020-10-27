class Bev:
    generation = 0
    jung = 0
    erwachsen = 0
    alt = 0

    def gen(self):
        self.generation += 1
        self.alt = self.erwachsen / 3
        self.erwachsen = self.jung / 2
        self.jung = 4 * self.erwachsen + 2 * self.alt

    def display_gen(self):
        print("gen %d: jung %d erwachsen %d alt %d" % (self.generation, self.jung, self.erwachsen, self.alt) )

    def __init__(self, j, e, a):
        self.jung = j
        self.erwachsen = e
        self.alt = a
