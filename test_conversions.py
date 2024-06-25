from fct_conversions import dico_to_chaine, passage_str_to_bin
from fct_conversions import passage_bin_to_str, passage_str_to_list
from fct_conversions import passage_list_to_str, passage_bin_to_hex
from fct_conversions import retour_str
from polynomes.fct_division_pgcd_e import creation_dico


def test_passage_str_to_bin():
    chaine = "hey"
    bin = passage_str_to_bin(chaine)
    assert bin == "011010000110010101111001"


def test_passage_bin_to_str():
    bin = "011010000110010101111001"
    chaine = passage_bin_to_str(bin)
    assert chaine == "hey"


def test_str_to_list():
    bin_str = "10110"
    bin_list = passage_str_to_list(bin_str)
    assert bin_list == [1, 0, 1, 1, 0]


def test_dico_to_chaine():
    assert dico_to_chaine({2: 0, 1: 0, 0: 1}) == "100"
    assert dico_to_chaine({3: 1, 2: 1, 1: 0, 0: 1}) == "1011"
    assert dico_to_chaine({0: 0}) == "0"


def test_list_to_str():
    liste = [1, 0, 1, 0, 0]
    chaine = passage_list_to_str(liste)
    assert chaine == "10100"


def test_passage_bin_to_hex():
    bin_str = "0101101"
    hexa = passage_bin_to_hex(bin_str)
    assert hexa == hex(45)


def test_retour_binaire():
    poly = {3: 1, 2: 0, 1: 0, 0: 1}
    chaine = retour_str(poly)
    chaine1 = "100101"
    poly_bis = creation_dico(chaine1)
    assert chaine == "001"
    assert retour_str(poly_bis) == chaine1
