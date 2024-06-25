from classe_proba import Proba
from classe_lfsr import LFSR
from random import randint

mess_humain = input("Donnez un nobre binaire que vous pensez aléatoire: ")
liste_humain = []
for elt in mess_humain:
    liste_humain.append(int(elt))

seed = [1, 1, 1, 0, 1]
lfsr = [1, 1, 0, 0, 1]
machine = LFSR(seed, lfsr)
message = []
for i in range(len(liste_humain)):
    message.append(randint(0, 1))
print(message)

machine_lsfr = LFSR(seed, lfsr)
clé = machine_lsfr.fabrication_nb_al(message)

# Etude Khi1
proba_lsfr = Proba(clé)
proba_randint = Proba(message)
proba_humain = Proba(liste_humain)
X = proba_lsfr.calcul_khi_pour_diff_grp(1)
Y = proba_randint.calcul_khi_pour_diff_grp(1)
V = proba_humain.calcul_khi_pour_diff_grp(1)
print(X, "\n", Y, "\n", V)

liste = [X, Y, V]
for i in range(len(liste)):
    if liste[i] < 7.88:
        print("Le modèle", i, "est validé pour les 0 et les 1.")
    else:
        print("Le modèle", i, "n'est pas validé pour les 0 et les 1.")

# Etude de Khi2
W = proba_lsfr.calcul_khi_pour_diff_grp(2)
Z = proba_randint.calcul_khi_pour_diff_grp(2)
Q = proba_humain.calcul_khi_pour_diff_grp(2)
print(W, "\n", Z, "\n", Q)

liste = [W, Z, Q]
for i in range(len(liste)):
    if liste[i] < 10.60:
        print("Le modèle", i, "est validé pour les couples.")
    else:
        print("Le modèle", i, "n'est pas validé pour les couples.")

# Etude du Khi3
H = proba_lsfr.calcul_khi_pour_diff_grp(3)
U = proba_randint.calcul_khi_pour_diff_grp(3)
P = proba_humain.calcul_khi_pour_diff_grp(3)
print(H, "\n", U, "\n", P)

liste = [H, U, P]
for i in range(len(liste)):
    if liste[i] < 12.84:
        print("Le modèle", i, "est validé pour les triplets.")
    else:
        print("Le modèle", i, "n'est pas validé pour les triplets.")
