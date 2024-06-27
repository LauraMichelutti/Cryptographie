def creation_dico(chaine):
    dico = {}
    for i in range(len(chaine)):
        dico[(len(chaine) - i)] = int(chaine[len(chaine) - 1 - i])
        # print(dico, "et ", chaine[len(chaine)-1-i], "avec i= ", i)
    dico[0] = 1
    return dico


def trouver_le_degre(poly):
    if type(poly) is str:
        deg = 0
        for i in range(len(poly)):
            # print("i: ", i)
            # print(poly[i])
            if poly[i] == "1":
                deg = i + 1
        return deg
    if type(poly) is dict:
        for cle in poly:
            # print("la cle: ", cle)
            if poly[cle] == 1:
                return cle
        return 0


def dico_vide_taille_donnée(deg):
    chaine = ""
    if deg != 0:
        for i in range(deg):
            chaine += "0"
        dico = creation_dico(chaine)
        dico[0] = 0
    else:
        dico = {0: 0}
    return dico


def division_euclidienne(poly1, poly2):
    degre_poly1 = trouver_le_degre(poly1)
    degre_poly2 = trouver_le_degre(poly2)
    # print(degre_poly1, degre_poly2)
    n = degre_poly1
    rep = dico_vide_taille_donnée(degre_poly1 - degre_poly2)
    compteur = 0
    while degre_poly1 >= degre_poly2 and compteur < 2:
        inter = dico_vide_taille_donnée(n)
        # print(inter)
        coeff = degre_poly1 - degre_poly2
        # print("coeff: ", coeff)
        rep[coeff] = 1
        # print("rep: ", rep)
        # creation inter
        for indice in poly2:
            if poly2[indice] == 1:
                valeur = coeff + indice
                inter[valeur] = 1
        # print("intermediaire: ", inter)
        # soustraction du poly et de l'inter
        for degre in poly1:
            # print("degree: ", degre)
            if degre <= degre_poly1:
                if inter[degre] == 1 and poly1[degre] == 1:
                    poly1[degre] = 0
                elif inter[degre] == 1 and poly1[degre] == 0:
                    poly1[degre] = 1
            # print("nouveau poly1: ", poly1)
            # print("inter: ", inter)
        degre_poly1 = trouver_le_degre(poly1)
        if degre_poly1 == 0:
            compteur += 1
        # print("new_degree: ", degre_poly1)
    return rep, poly1


def find_pgcd(poly1, poly2):
    compteur = 0
    # initialisation
    liste_reste = []
    liste_divisés = [poly1]
    liste_diviseur = [poly2]
    liste_quotient = [division_euclidienne(poly1, poly2)[0]]
    reste = division_euclidienne(poly1, poly2)[1]
    print("liste_reste: ", liste_reste)
    if trouver_le_degre(reste) == 0 and reste[0] == 0:
        liste_reste.append(0)
    else:
        liste_reste.append(reste)
    while liste_reste[-1] != 0:
        compteur += 1
        divisé = liste_diviseur[-1]
        diviseur = liste_reste[-1]
        # mise à jour des listes
        liste_divisés.append(divisé)
        liste_diviseur.append(diviseur)
        liste_quotient.append(division_euclidienne(divisé, diviseur)[0])
        reste = division_euclidienne(divisé, diviseur)[1]
        print("reste: ", reste)
        if trouver_le_degre(reste) == 0 and reste[0] == 0:
            liste_reste.append(0)
        else:
            liste_reste.append(reste)
        print("liste_reste_bis: ", liste_reste)
    print("liste_quotient: ", liste_quotient)
    # Calcul pgcd
    if compteur == 0:
        print("Les 2 polynomes sont multiples")
    else:
        pgcd = liste_reste[-2]
        return pgcd


def creation_Xe_poly(deg):
    poly2 = dico_vide_taille_donnée(deg)
    poly2[0] = 1
    poly2[deg] = 1
    return poly2


def trouver_e(poly):
    n = trouver_le_degre(poly)
    for e in range(n, (2**n)):
        # print("e: ", e)
        poly1 = poly
        poly2 = creation_Xe_poly(e)
        # print("poly2 = ", poly2)
        quotient, reste = division_euclidienne(poly2, poly1)
        # print("reste: ", reste)
        # print("degre: ", trouver_le_degre(reste))
        if trouver_le_degre(reste) == 0 and reste[0] == 0:
            return e, quotient
            # print(liste)
