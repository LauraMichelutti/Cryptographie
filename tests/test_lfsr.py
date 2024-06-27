from classe_lfsr import LFSR


def test_initialisation():
    registre = LFSR([1, 0, 1, 0], [0, 1, 0, 1])
    assert registre.valeurs == [1, 0, 1, 0]
    assert registre.lfsr == [0, 1, 0, 1]
    assert registre.sortie == []
    assert registre.periode == 0


def test_next():
    registre = LFSR([1, 0, 1, 0], [0, 1, 0, 1])
    registre.next()
    assert registre.valeurs == [0, 1, 0, 1]
    assert registre.periode == 1
    assert registre.sortie == [0]


def test_fabrication_nb_al():
    registre = LFSR([1, 0, 1, 0], [0, 1, 0, 1])
    registre.fabrication_nb_al([0, 1])
    assert registre.sortie == [0, 1, 0, 1, 0, 0]


def test_chiffrage_dechif():
    registre = LFSR([1, 0, 1, 0], [0, 1, 0, 1])
    registre.fabrication_nb_al([0, 1])
    result = registre.chiffrage_dechiffrage([0, 1])
    assert result == [0, 1]
