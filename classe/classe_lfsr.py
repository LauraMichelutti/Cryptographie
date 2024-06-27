"""
1) Dans le LFSR, on met les 1 pour les (ou exclusif) en considèrant x0 tout 
à droite
2) Dans la seed, on met également x0 tout à droite afin que cela soit raccord 
avec le LFSR
"""


class LFSR:
    def __init__(self, seed, lfsr):
        self.valeurs = seed
        self.lfsr = lfsr
        self.sortie = []
        self.periode = 0

    def next(self):
        x = 0
        for i in range(len(self.lfsr)):
            x = (x + (self.lfsr[i] * self.valeurs[i])) % 2
        self.sortie.append(self.valeurs[-1])
        self.valeurs = [x] + self.valeurs[:-1]
        self.periode += 1

    def show(self):
        print("              ")
        print("Le LSFR est:", self.lfsr)
        print("Les valeurs actuelles sont: ", self.valeurs)
        print("L'ensemble des valeurs sorties sont: ", self.sortie)

    def __str__(self):
        return (
            "Le LSFR est: "
            + str(self.lfsr)
            + "  Les valeurs actuelles sont: "
            + str(self.valeurs)
            + "  L'ensemble des valeurs sorties est: "
            + str(self.sortie)
        )

    def fabrication_nb_al(self, message):
        n = len(message)
        for i in range(n + len(self.valeurs)):
            self.next()
        return self.sortie

    def fabriq_al_sans_mess(self, nb):
        for i in range(nb + len(self.valeurs)):
            self.next()
        return self.sortie

    def chiffrage_dechiffrage(self, message):
        resultat = []
        j = len(self.valeurs)
        for i in range(len(message)):
            resultat.append((self.sortie[i + j] + message[i]) % 2)
        return resultat
