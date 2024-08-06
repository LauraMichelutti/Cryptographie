from classe_lfsr import LFSR
from fct_conversions import passage_list_to_str, passage_list_deci_to_list_bin
from fct_conversions import separation_par_octet
from fct_conversions import passage_str_to_decimal, passage_bin_to_decimal
from fct_decryptage import ou_exclusif
from fct_conversions import passage_deci_to_str

message = "Virement de 100 euros pour Antoine"
message_bis = "Virement de 500 euros pour Andrea"
print("On sait que le message inconnu est sous la forme:")
print(" Virement de ??? euros à ???????")
print("Et on connaît le message: ", message_bis)

# On transforme le message en binaire

message1 = passage_list_deci_to_list_bin(passage_str_to_decimal(message))
message2 = passage_list_deci_to_list_bin(passage_str_to_decimal(message_bis))
print("\n", "AVOIR:  ", message2)

remplissage = "00000001"

if len(message) <= len(message_bis):
    long_max = len(message_bis)
    diff = len(message_bis) - len(message)
    for i in range(diff):
        message1.append(remplissage)
else:
    long_max = len(message)
    diff = len(message) - len(message_bis)
    for i in range(diff):
        message2.append(remplissage)

# Creation LFSR
longueur = long_max
seed = [1, 0, 1, 1]
lsfr = [1, 0, 0, 1]
machine = LFSR(seed, lsfr)
cle = machine.fabriq_al_sans_mess(8 * longueur - len(seed))
cle = passage_list_to_str(cle)
cle_octet = separation_par_octet(cle)
if cle_octet[0] == "00000000":
    cle_octet = cle_octet[1:]
print("\n", "La clé par octet est:", cle_octet, "\n")

# chiffrage
mess1_pu = []
for i in range(len(message1)):
    mess1_pu.append(ou_exclusif(message1[i], cle_octet[i]))
print("Le message crypté 1 est: ", mess1_pu, "\n")

mess2_pu = []
for i in range(len(message2)):
    mess2_pu.append(ou_exclusif(message2[i], cle_octet[i]))
print("Le message crypté 2 est: ", mess2_pu)


# Infos clé & message connu
print("\n", "On cherche la clé utilisée pour chiffrer 500")
nb_500_coder = passage_list_deci_to_list_bin(passage_str_to_decimal("500"))
print("Le 500 coder est:", nb_500_coder)

cle_partielle = []
for i in range(3):
    cle_partielle.append(ou_exclusif(mess2_pu[12 + i], nb_500_coder[i]))
print("Voici la clé utilisé:", cle_partielle)

nouveau_nb = input("Choisissez un nombre entre 100 et 999: ")

new_bin = passage_list_deci_to_list_bin(passage_str_to_decimal(nouveau_nb))

nouveau_elt = []
for i in range(len(new_bin)):
    nouveau_elt.append(ou_exclusif(cle_partielle[i], new_bin[i]))
print("Le nouveau élèment est: ", nouveau_elt, "\n")


# Création du message modifié
mess_modif = mess1_pu[0:12] + nouveau_elt + mess1_pu[12 + len(new_bin) :]
print("Voici le message modifié: ", mess_modif, "\n")


# Résultats
print("Voici le message envoyé initialement: ", message)
mess_recu = []
for i in range(len(mess_modif)):
    mess_recu.append(ou_exclusif(mess_modif[i], cle_octet[i]))
inter = passage_deci_to_str(passage_bin_to_decimal(mess_recu))
final = passage_list_to_str(inter)
print("Voici le message décrypté après modification: ", final)
