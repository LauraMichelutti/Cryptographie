from polynomes.fct_division_pgcd_e import trouver_le_degre, creation_dico
from polynomes.fct_division_pgcd_e import division_euclidienne, dico_vide_taille_donnée
from polynomes.fct_division_pgcd_e import find_pgcd, creation_Xe_poly
from polynomes.fct_division_pgcd_e import trouver_e


def test_creation_dico():
    chaine2 = "1000001"
    chaine = "0000"
    chaine3 = "11"
    poly3 = creation_dico(chaine3)
    poly1 = creation_dico(chaine)
    poly = creation_dico(chaine2)
    assert poly == {7: 1, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 1, 0: 1}
    assert poly1 == {4: 0, 3: 0, 2: 0, 1: 0, 0: 1}
    assert poly3 == {2: 1, 1: 1, 0: 1}


def test_trouver_le_degre():
    poly = "10010"
    assert trouver_le_degre(poly) == 4
    poly1 = "111"
    assert trouver_le_degre(poly1) == 3
    poly2 = {7: 1, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 1, 0: 1}
    assert trouver_le_degre(poly2) == 7
    poly3 = {4: 0, 3: 0, 2: 0, 1: 0, 0: 1}
    assert trouver_le_degre(poly3) == 0


def test_dico_vide():
    deg = 4
    poly = dico_vide_taille_donnée(deg)
    assert poly == {4: 0, 3: 0, 2: 0, 1: 0, 0: 0}


def test_division_euclidienne_sans_reste():
    chaine1 = "1011001001"
    chaine2 = "1000001"
    poly1 = creation_dico(chaine1)
    poly2 = creation_dico(chaine2)
    assert division_euclidienne(poly1, poly2) == (
        {
            3: 1,
            2: 0,
            1: 0,
            0: 1,
        },
        {10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0},
    )
    chaine3 = "01001"
    chaine4 = "10000"
    poly3 = creation_dico(chaine3)
    poly4 = creation_dico(chaine4)
    assert division_euclidienne(poly3, poly4)[0] == {4: 1, 3: 1, 2: 1, 1: 0, 0: 0}


def test_avec_reste_division_euclidienne():
    chaine1 = "1001"
    chaine2 = "1010"
    poly1 = creation_dico(chaine1)
    poly2 = creation_dico(chaine2)
    assert division_euclidienne(poly1, poly2)[0] == {1: 1, 0: 0}
    assert division_euclidienne(poly1, poly2)[1] == {4: 0, 3: 0, 2: 1, 1: 0, 0: 1}


def test_division_eucli_par_1():
    chaine3 = "01"
    chaine4 = "00"
    poly3 = creation_dico(chaine3)
    poly4 = creation_dico(chaine4)
    assert division_euclidienne(poly3, poly4) == (
        {2: 1, 1: 0, 0: 1},
        {2: 0, 1: 0, 0: 0},
    )


def test_trouver_pgcd():
    chaine3 = "1001"
    chaine4 = "1010"
    poly3 = creation_dico(chaine3)
    poly4 = creation_dico(chaine4)
    assert find_pgcd(poly3, poly4) == {4: 0, 3: 0, 2: 0, 1: 0, 0: 1}
    chaine1 = "010101"
    chaine2 = "100110"
    poly1 = creation_dico(chaine1)
    poly2 = creation_dico(chaine2)
    assert find_pgcd(poly1, poly2) is None


def test_creation_Xe_poly():
    assert creation_Xe_poly(3) == {3: 1, 2: 0, 1: 0, 0: 1}


def test_trouver_e_poly():
    chaine1 = "101"
    poly1 = creation_dico(chaine1)
    assert trouver_e(poly1) == (7, {4: 1, 3: 0, 2: 1, 1: 1, 0: 1})
    chaine2 = "011"
    poly2 = creation_dico(chaine2)
    assert trouver_e(poly2) == (7, {4: 1, 3: 1, 2: 1, 1: 0, 0: 1})
    chaine3 = "001"
    poly3 = creation_dico(chaine3)
    assert trouver_e(poly3) == (3, {0: 1})
