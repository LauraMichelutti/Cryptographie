from fct_conversions import passage_list_to_str, passage_list_deci_to_list_bin
from fct_conversions import passage_str_to_decimal, separation_par_octet
from fct_conversions import passage_deci_to_str, passage_bin_to_decimal
from classe_lfsr import LFSR
from fct_decryptage import ou_exclusif


# Messages
"""Seules les phrases contenant des lettres maj ou min avec des chiffres"""
"""des virgules, des apostrophes, des : et des accents sont autorisées"""
"""Faites rentrer des phrases ayant un lieu avec un thème à quelqu'un"""
message1 = "Elle va sur la plage"
message2 = "Il mange une glace"

# Mettre les message a la même longueur (ajouter des espaces)
if len(message1) < len(message2):
    diff = len(message2) - len(message1)
    arriere = [" " * diff]
    arriere = passage_list_to_str(arriere)
    message1 = message1 + arriere
elif len(message1) > len(message2):
    diff = len(message1) - len(message2)
    arriere = [" " * diff]
    arriere = passage_list_to_str(arriere)
    message2 = message2 + arriere

if len(message1) == len(message2):
    print(True)
else:
    print(False)

# Mise en forme sous octets binaires
message1bin = passage_list_deci_to_list_bin(passage_str_to_decimal(message1))
message2bin = passage_list_deci_to_list_bin(passage_str_to_decimal(message2))

print("Le message1 est:", passage_list_to_str(message1bin))
print("Le message2 est:", passage_list_to_str(message2bin))
print("\n")

# Creation LFSR
longueur = len(message1)
seed = [1, 0, 1, 1]
lsfr = [1, 0, 0, 1]
machine = LFSR(seed, lsfr)
cle = machine.fabriq_al_sans_mess(8 * longueur - len(seed))
cle = passage_list_to_str(cle)
cle_octet = separation_par_octet(cle)
if cle_octet[0] == "00000000":
    cle_octet = cle_octet[1:]
print("La cLé est:", cle)

# chifrrage
mess1_pu = []
for i in range(len(message1bin)):
    mess1_pu.append(ou_exclusif(message1bin[i], cle_octet[i]))

print("\n")
mess2_pu = []
for j in range(len(message2bin)):
    mess2_pu.append(ou_exclusif(message2bin[j], cle_octet[j]))


print("le premier message crypté est:", "\n", passage_list_to_str(mess1_pu))
print("le deuxième message crypté est:", "\n", passage_list_to_str(mess2_pu))

# XOR des 2 messages cryptés
xor2mess = []
for i in range(len(mess1_pu)):
    xor2mess.append(ou_exclusif(mess1_pu[i], mess2_pu[i]))


print("Le XOR des 2 messages cryptés est:", passage_list_to_str(xor2mess))

# Trouver le deuxième message
print("\n", "Vous connaissez le message: Elle va sur la plage")
messtrouvé = []
for j in range(len(xor2mess)):
    messtrouvé.append(ou_exclusif(xor2mess[j], message1bin[j]))

messtrouvé = passage_deci_to_str(passage_bin_to_decimal(messtrouvé))
messtrouvé = passage_list_to_str(messtrouvé)
print("Et en appliquant un XOR, vous trouvez le message", messtrouvé)
