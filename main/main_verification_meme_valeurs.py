from classe_lfsr import LFSR
from fct_conversions import passage_str_to_list, passage_list_to_str

# Comparaison et vérification de résultats
print("Vérifions qu'avec une certaine seed, 2 polynômes différents peuvent renvoyer une même suite d'aléatoire")
print("\n")

# Création graine commune
chaine = "1001001001"
seed = passage_str_to_list(chaine)
print("Voilà la seed utilisée: ", seed)
longueur = int(input("Donnez la longueur de nombre aléatoire que vous voulez comparer: "))
print("longueur nb al = ", longueur)

# Cas 1: grand polynome
print("\n", "Commençons par regarder la suite aléatoire du plus grand: ")
chaine1 = "1011001001"
lsfr = passage_str_to_list(chaine1)
print("On étudie le LFSR suivant: ", lsfr)

machine1 = LFSR(seed, lsfr)
valeurs1 = machine1.fabriq_al_sans_mess(longueur)
list1 = passage_list_to_str(valeurs1)
print("On obtient les valeurs: ", list1)

# Cas 2: petit polynome
print("\n", "On étudie maintenant le LFSR plus petit:")
chaine2 = "001"
lsfr2 = passage_str_to_list(chaine2)
print("On étudie le LFSR suivant: ", lsfr2)
machine2 = LFSR(seed, lsfr2)
valeurs2 = machine2.fabriq_al_sans_mess(longueur)
list2 = passage_list_to_str(valeurs2)
print("On obtient les valeurs: ", list2)

# Comparaison
print("\n", "Les valeurs observées sont-elles les mêmes?")
if valeurs1 == valeurs2:
    print("OUI")
else:
    print("NON")
