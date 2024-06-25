from fct_decryp_ber_mas import somme_termes, ou_exclusif
from fct_decryp_ber_mas import creation_dico, creation_dico_vide
from fct_decryp_ber_mas import addition_binaire, multiplication_binaire


def test_ou_exclu():
    x = 0
    y = 0
    z = 1
    w = 1
    assert ou_exclusif(x, y) == 0
    assert ou_exclusif(y, z) == 1
    assert ou_exclusif(z, w) == 0


def test_somme_termes():
    suite = "0111"
    poly = "1010"
    t = 2
    delta = 2
    assert somme_termes(suite, delta, poly, t) == 1
    assert somme_termes(suite, 0, poly, t) == 1


def test_creation_dico():
    assert creation_dico("101") == {2: 1, 1: 0, 0: 1}
    assert creation_dico_vide(5) == {5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}


def test_multiplication_binaire():
    assert multiplication_binaire("11", 3, 1) == {3: 1, 2: 1, 1: 0, 0: 0}


def test_addition_binaire():
    assert addition_binaire("00001", {3: 1, 2: 1, 1: 0, 0: 1}) == {
        4: 1,
        3: 1,
        2: 1,
        1: 0,
        0: 1,
    }
    assert addition_binaire("101", {2: 1, 1: 0, 0: 0}) == {2: 0, 1: 0, 0: 1}
