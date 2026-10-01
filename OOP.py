class Auto():
    """Klasse für Autos"""


    def __init__(self, marke, modell, jahr, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4
        self.tueren = tueren
        self.ps = ps

    def begruessung(self):
            print("Hallo, ich bin" + self.marke)

    def fahren(self):
        print("BrmBrmBrm" * int(self.ps/10))


class Sportwagen(Auto):
    def __init__(self, marke, modell, jahr, tueren, ps, folierung):
        super().__init__(marke, modell, jahr, tueren, ps)
        self.folierung = folierung
        self.auspuff = 2

    def turbo(self):
        print("Turbo")

    def fahren(self):


sw1 = Sportwagen("Seat", "Ibiza", 2020, 2, 500, "matt")
print(sw1.folierung)
print(sw1.auspuff)
sw1.turbo()
