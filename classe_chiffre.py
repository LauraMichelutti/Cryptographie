from classe_lfsr import LFSR


class Chiffre(LFSR):
    def __init__(self, seed, LSFR):
        super().__init__(seed, LSFR)

    def chiffrer_dechiffrer(self, message):
        result = []
        for i in range(4):
            self.next()
            # print(self)
        for elt in message:
            self.next()
            # print(
            #  "Pour k=", self.periode, "  Les valeurs actuelles sont: ",
            # self.valeurs)
            if (self.sortie[-1] + int(elt)) % 2 == 0:
                result.append(0)
            else:
                result.append(1)
        return result
