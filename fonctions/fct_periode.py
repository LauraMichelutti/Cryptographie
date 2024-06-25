from classe_lfsr import LFSR


def trouver_la_periode(seed, lfsr):
    tortue = LFSR(seed, lfsr)
    lievre = LFSR(seed, lfsr)
    # initialisation
    tortue.next()
    lievre.next()
    lievre.next()
    while tortue.valeurs != lievre.valeurs:
        tortue.next()
        lievre.next()
        lievre.next()
    tortue.next()
    lievre.next()
    lievre.next()
    mu = 1
    while tortue.valeurs != lievre.valeurs:
        mu = mu + 1
        tortue.next()
        lievre.next()
        lievre.next()
    return mu
