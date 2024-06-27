from fct_renf import creation_seed, generateur_nb_al_renf
from classe_lfsr import LFSR
from fct_renf import generateur_peu_renf


def test_creation_seed():
    seed = [1, 0, 1, 0]
    lsfr = [0, 1, 1, 0]
    machine = LFSR(seed, lsfr)
    seeds = creation_seed(machine, 5, 4, 3)
    assert len(seeds[0]) == 5
    assert len(seeds[1]) == 4
    assert len(seeds[-1]) == 3


def test_fonction_nb_al_renf():
    seed = [1, 0, 1, 0]
    lsfr = [0, 1, 1, 0]
    machine = LFSR(seed, lsfr)
    seeds = creation_seed(machine, 4, 5, 6)
    lsfr1 = [1, 1, 0, 0]
    machine1 = LFSR(seeds[0], lsfr1)
    lsfr2 = [1, 0, 1, 1, 0]
    machine2 = LFSR(seeds[1], lsfr2)
    lsfr3 = [1, 0, 1, 1, 0, 1]
    machine3 = LFSR(seeds[-1], lsfr3)
    assert generateur_nb_al_renf(machine1, machine2, machine3, 10) == [
        0,
        1,
        0,
        0,
        1,
        1,
        1,
        1,
        0,
        1,
    ]


def test_gen_peu_renf():
    seed = [1, 0, 1, 0]
    lsfr = [0, 1, 1, 0]
    machine = LFSR(seed, lsfr)
    seeds = creation_seed(machine, 4, 5, 6)
    lsfr1 = [1, 1, 0, 0]
    machine1 = LFSR(seeds[0], lsfr1)
    lsfr2 = [1, 0, 1, 1, 0]
    machine2 = LFSR(seeds[1], lsfr2)
    assert generateur_peu_renf(machine1, machine2, 11) == [
        0,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        0,
    ]
