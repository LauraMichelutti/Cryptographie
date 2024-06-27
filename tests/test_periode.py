from fct_periode import trouver_la_periode


def test_periode_lfsr():
    seed = [1, 0, 1]
    lfsr = [0, 1, 1]
    periode = trouver_la_periode(seed, lfsr)
    assert periode == 7
    lfsr2 = [1, 0, 0]
    periode2 = trouver_la_periode(seed, lfsr2)
    assert periode2 == 1
