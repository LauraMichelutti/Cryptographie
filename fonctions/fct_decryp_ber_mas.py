from fct_conversions import dico_to_chaine


def somme_termes(suite, delta, poly, t):
    somme = int(suite[t])
    # print(somme)
    for i in range(1, delta + 1):
        # print("s", t - i, "= ", suite[t - i])
        # print("p", i, "=", poly[i])
        somme += int(poly[i]) * int(suite[t - i])
        # print("somme av mod:", somme)
    if somme % 2 == 0:
        return 0
    else:
        return 1


def ou_exclusif(x, y):
    if (x + y) % 2 == 0:
        return 0
    else:
        return 1


def creation_dico(chaine):
    dico = {}
    for i in range(len(chaine)):
        dico[(len(chaine) - 1 - i)] = int(chaine[len(chaine) - 1 - i])
        # print(dico, "et ", chaine[len(chaine)-1-i], "avec i= ", i)
    return dico


def creation_dico_vide(deg):
    dico = {}
    for i in range(deg + 1):
        dico[deg - i] = 0
    return dico


def multiplication_binaire(bin1, t, m):
    dico1 = creation_dico(bin1)
    # print("dico", dico1)
    n = len(bin1) - 1
    new_dico = creation_dico_vide(n + t - m)
    # print("new_dico", new_dico)
    for cle in dico1:
        if dico1[cle] != 0:
            new_dico[cle + t - m] = 1
            new_dico[cle] = 0
    return new_dico


def addition_binaire(bin1, dico2):
    dico1 = creation_dico(bin1)
    # print("dico1: ", dico1)
    if len(bin1) - 1 < len(dico2) - 1:
        m = len(dico2) - 1
        grd = dico2
        n = len(bin1) - 1
    else:
        m = len(dico1) - 1
        grd = dico1
        n = len(dico2) - 1
    new_dico = creation_dico_vide(m)
    for i in range(n + 1):
        if dico1[i] == dico2[i]:
            new_dico[i] = 0
        else:
            new_dico[i] = 1
    for k in range(n + 1, m + 1):
        new_dico[k] = grd[k]
    return new_dico


def algo_ber_mas(suite):
    P = "1"
    P_prime = "1"
    delta = 0
    m = -1
    n = len(suite)
    for t in range(n):  # ca va jusqu'à n-1
        # print("\n")
        # print("t= ", t)
        # print("delta = ", delta)
        d = somme_termes(suite, delta, P, t)
        # print("d = ", d)
        if d != 0:
            T = P
            # print("m= ", m)
            # print("P_prime = ", P_prime)
            inter = multiplication_binaire(P_prime, t, m)
            # print("inter: ", inter)
            inter2 = addition_binaire(P, inter)
            P = dico_to_chaine(inter2)
            if 2 * delta <= t:
                delta = t + 1 - delta
                m = t
                P_prime = T
        # print("poly = ", P)
    return delta, P
