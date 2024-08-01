from classe_lfsr import LFSR
from fct_conversions import passage_list_to_str

# Conditions
print("On regarde la suite générée par le lFSR:")
print("- de coefficient de connexion: (0, 1, 1, 1, 0, 0)")
print("- d'état initial: (1, 1, 0, 1, 0, 0)")

# Creation LFSR
seed = [1, 1, 0, 1, 0, 0]
lfsr = [0, 1, 1, 1, 0, 0]
machine = LFSR(seed, lfsr)
result = machine.fabriq_al_sans_mess(30)
print("\n", "Ce LFSR génère la suite:")
print(passage_list_to_str(result))
