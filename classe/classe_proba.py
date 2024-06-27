class Proba:
    def __init__(self, liste):
        self.liste = liste
        self.chaine = ""

    def liste_to_chaine(self):
        chaine = ""
        for elt in self.liste:
            chaine += str(elt)
        return chaine

    def apparition_gen(self, k):
        chaine = self.liste_to_chaine()
        m = len(chaine)
        dico = {}
        for i in range(m - k + 1):
            if chaine[i: i + k] in dico:
                dico[chaine[i: i + k]] += 1
            else:
                dico[chaine[i: i + k]] = 1
        return dico

    def calcul_khi_pour_diff_grp(self, k):
        dico_gen = self.apparition_gen(k)
        X = 0
        m = len(self.liste) - k + 1
        sum_liste = []
        for cle in dico_gen:
            sum_liste.append(((dico_gen[cle] - (m / 2**k)) ** 2) / (m / 2**k))
        j = len(sum_liste)
        while j < 2**k:
            sum_liste.append(((0 - (m / 2**k)) ** 2) / (m / 2**k))
            j += 1
        for elt in sum_liste:
            X += elt
        return X

    def comparaison_2valeurs_acote(self):
        compteur = 0
        for i in range(len(self.liste) - 1):
            if self.liste[i] == self.liste[i + 1]:
                compteur += 1
        return compteur / len(self.liste)
