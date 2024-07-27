from fct_conversions import passage_str_to_list
from fct_periode import trouver_la_periode

tous_les_polynomes = ["1001", "1010", "1011", "1100", "1101", "1110", "1111"]
seeds = ["001", "010", "011", "100", "101", "110", "111"]

for elt in tous_les_polynomes:
    lfsr = passage_str_to_list(elt[1:])
    for graine in seeds:
        seed = passage_str_to_list(graine)
        print("Pour une seed =", graine, "et un lfsr =", elt)
        print("On a une période =", trouver_la_periode(seed, lfsr))
    print("\n")
