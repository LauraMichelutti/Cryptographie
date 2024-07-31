from classe_lsfr import LSFR
from fonctions_decryp import ou_exclusif, ajout_de_solution
from fonctions_conversions import passage_list_to_str
from fonctions_conversions import separation_par_octet
from fonctions_conversions import passage_list_deci_to_list_bin
from fonctions_conversions import passage_str_to_decimal
from fonctions_decryp import information_sur_un_message, affichage

# Messages
"""Seules les phrases contenant des lettres maj ou min avec des chiffres"""
"""des virgules, des apostrophes, des : et des accents sont autorisées"""
"""Faites rentrer des phrases ayant un lieu avec un thème à quelqu'un"""
message1 = input("Donnez une phrase: ")
message2 = input("Donnez une phrase: ")

longueur_max = max(len(message1), len(message2))
longueur_min = min(len(message1), len(message2))
print("Le plus grand message a une longueur de:", longueur_max)
print("Le plus petit message a une longueur de:", longueur_min)


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

message1 = passage_list_deci_to_list_bin(passage_str_to_decimal(message1))
message2 = passage_list_deci_to_list_bin(passage_str_to_decimal(message2))

print("Le message1 est:", message1)
print("Le message2 est:", message2)

# Creation LFSR
longueur = len(message1)
seed = [1, 0, 1, 1]
lsfr = [1, 0, 0, 1]
machine = LSFR(seed, lsfr)
cle = machine.fabriq_al_sans_mess(8 * longueur - len(seed))
cle = passage_list_to_str(cle)
cle_octet = separation_par_octet(cle)
if cle_octet[0] == "00000000":
    cle_octet = cle_octet[1:]
print("\n", "La clé par octet est:", cle_octet, "\n")

print("La longueur de la clé est de: ", len(cle_octet))
print("La longueur des messages est: ", len(message2))

print("\n")
print("Le message1 est:", message1)
print("Le message2 est:", message2)

# chifrrage
mess1_pu = []
for i in range(len(message1)):
    mess1_pu.append(ou_exclusif(message1[i], cle_octet[i]))

print("\n")
mess2_pu = []
for j in range(len(message2)):
    mess2_pu.append(ou_exclusif(message2[j], cle_octet[j]))


print("le premier message crypté est:", "\n", mess1_pu)
print("le deuxième message crypté est:", "\n", mess2_pu)

# creation du ou_exclu des 2 messages cryptés
mess1_ou_mess2 = []
for i in range(len(mess1_pu)):
    mess1_ou_mess2.append(ou_exclusif(mess1_pu[i], mess2_pu[i]))
print("\n", "Le ou_exclu sur les 2 messages publics:", "\n", mess1_ou_mess2)


# Supposons qu'on connaît un mot mais pas sa place
rep = ""
new_result = []
compteur = 0
nb_reponse = []
while rep != "non":
    compteur += 1
    mot = input("Quelles sont les infos connues: ")
    mot_connubin = passage_list_deci_to_list_bin(passage_str_to_decimal(mot))
    print("mot connu: ", mot_connubin)
    fonction = information_sur_un_message(mot_connubin, mess1_ou_mess2)
    if fonction != []:
        print("\n", "Les possibilités sont: ")
        affichage(fonction)
        avs = input("Certaines possibilités vous semblent-t-elles étranges? ")
        if avs == "oui":
            nombre = int(input("Combien voulez vous en supprimer? "))
            for i in range(nombre):
                indice = int(input("Lequel voulez-vous supprimer? "))
                fonction.pop((indice-1))
                affichage(fonction)
    else:
        print("Il n'y a pas de possibilité dans ce cas")
    new_result = ajout_de_solution(new_result, fonction)
    print("new_fonction: ", new_result)
    nb_reponse.append(len(fonction))
    print("\n", "Pour l'instant, vous avez ces possibilités: ")
    affichage(new_result)
    print("Le compteur est à: ", compteur)
    if compteur > 1:
        correction = input("Voulez-vous supprimer des possibilités? ")
        if correction == "oui":
            nombre = int(input("Combien voulez vous en supprimer? "))
            for i in range(nombre):
                indice = int(input("Lequel voulez-vous supprimer? "))
                new_result.pop(indice-1)
                affichage(new_result)

    rep = input("Voulez-vous continuez? ")
avis = input("Pensez vous avoir trouvé les messages? ")
if avis == "oui":
    result_final = []
    numero = 1
    for elt in new_result:
        inter = passage_list_to_str(elt[0])
        result_final.append(inter)
        print("Le message", numero, "= ", inter)
