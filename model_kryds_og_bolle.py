import random


class KrydsOgBolle:
    def __init__(self):
        self.braet = ""
        self.spiller = ""
        self.nulstil_braet()

    def nulstil_braet(self):
        self.braet = "---------"
        self.random_spiller()

    def random_spiller(self):
        self.spiller = random.choice("XO")

    def skift_spiller(self):
        self.spiller = "X" if self.spiller == "O" else "O"

    def saet_plads(self, plads, spiller):
        self.braet = self.braet[:plads] + spiller + self.braet[plads + 1 :]

    def er_braettet_fyldt(self):
        return False if "-" in self.braet else True

    def _print_braet(self):
        for raekke in range(3):
            print(self.braet[raekke * 3 : raekke * 3 + 3])

    def tjek_vinder(self):
        vinder = None
        # Tjekker raekker
        for raekke in range(3):
            if self.braet[raekke * 3 : raekke * 3 + 3] in ("OOO", "XXX"):
                vinder = self.braet[raekke * 3]
                return vinder
        # Tjekker soejler
        for soejle in range(3):
            tjek = ""
            for raekke in range(3):
                tjek = tjek + self.braet[soejle + 3 * raekke]
            if tjek in ("OOO", "XXX"):
                vinder = tjek[0]
                return vinder
        # Tjekker 1. diagonal
        tjek = ""
        for i in range(3):
            tjek = tjek + self.braet[i * 4]
        if tjek in ("OOO", "XXX"):
            vinder = tjek[0]
            return vinder
        # Tjekker 2. diagonal
        tjek = ""
        for i in range(3):
            tjek = tjek + self.braet[2 + i * 2]
        if tjek in ("OOO", "XXX"):
            vinder = tjek[0]
            return vinder


