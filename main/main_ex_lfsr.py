from classe_lfsr import LFSR
from fct_conversions import passage_list_to_str

# Conditions
print("On regarde la suite générée par le lFSR:")
print("- de coefficient de connexion: (1, 0, 0, 1, 1)")
print("- d'état initial: (1, 1, 0, 1, 0)")

# Creation LFSR
seed = [1, 1, 0, 1, 0]
lfsr = [1, 0, 0, 1, 1]
machine = LFSR(seed, lfsr)
result = machine.fabriq_al_sans_mess(20)
print("\n", "Ce LFSR génère la suite:")
print(passage_list_to_str(result))
