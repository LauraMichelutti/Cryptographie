from fct_conversions import passage_str_to_list
from classe_lfsr import LFSR
from classe_proba import Proba

# On veut trouver les résultat des chi2 de tous les polynomes de degré 3
tous_les_polynomes = ["1001", "1010", "1011", "1100", "1101", "1110", "1111"]

for elt in tous_les_polynomes:
    seed = [1, 1, 0]
    lfsr = passage_str_to_list(elt[1:])
    print(lfsr)
    machine = LFSR(seed, lfsr)
    suite = machine.fabriq_al_sans_mess(40)
    probabilite = Proba(suite)
    print("Resultat avec le polynôme", elt, ":")
    for i in range(3):
        print(probabilite.calcul_khi_pour_diff_grp(i+1))
        # print("\n")
    dico = probabilite.comparaison_2valeurs_acote(1)
    print(probabilite.calcul_khi2_degre1_valeurcote(0.5, dico))
    print("\n")