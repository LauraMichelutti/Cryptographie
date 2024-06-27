def creation_seed(machine, a, b, c):
    seeds = []
    # creation seed1
    for i in range(a + len(machine.valeurs)):
        machine.next()
    seeds.append(machine.sortie[-a:])
    print(seeds)
    # creation seed2
    for i in range(b):
        machine.next()
    seeds.append(machine.sortie[-b:])
    for i in range(c):
        machine.next()
    seeds.append(machine.sortie[-c:])
    return seeds


def generateur_nb_al_renf(machine1, machine2, machine3, longueur):
    liste = []
    m = max(len(machine1.valeurs), len(machine2.valeurs), len(machine3.valeurs))
    for e in range(m + 1):
        machine1.next()
        machine2.next()
        machine3.next()
    for i in range(longueur):
        machine1.next()
        if machine1.sortie[-1] == 1:
            machine2.next()
            machine3.next()
            if (machine2.sortie[-1] + machine3.sortie[-1]) % 2 == 0:
                liste.append(0)
            else:
                liste.append(1)
        else:
            machine3.next()
            if (machine2.sortie[-1] + machine3.sortie[-1]) % 2 == 0:
                liste.append(0)
            else:
                liste.append(1)
    return liste


def generateur_peu_renf(machine1, machine2, longueur):
    liste = []
    m = max(len(machine1.valeurs), len(machine2.valeurs))
    for e in range(m + 1):
        machine1.next()
        machine2.next()
    print("sortie2: ", machine2.sortie)
    print("sortie1: ", machine1.sortie)
    print("PASS")
    for i in range(longueur):
        machine1.next()
        print("sortie1:", machine1.sortie)
        if machine1.sortie[-1] == 1:
            machine2.next()
            liste.append(machine2.sortie[-1])
        else:
            liste.append(machine2.sortie[-1])
        print("liste:", liste)
    return liste
