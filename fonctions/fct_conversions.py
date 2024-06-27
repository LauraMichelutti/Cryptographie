def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xFF)
        v >>= 8
    return bytes(b[::-1])


def passage_str_to_bin(chaine):
    binaire = ""
    a_bytes = chaine.encode()
    binary_converted = "".join(["{0:08b}".format(x) for x in a_bytes])
    binaire = binary_converted
    return binaire


def passage_bin_to_str(binaire_str):
    a_bytes = bitstring_to_bytes(binaire_str)
    result = a_bytes.decode("utf-8")
    chaine = result
    return chaine


def passage_str_to_list(chaine):
    liste = []
    for elt in chaine:
        liste.append(int(elt))
    return liste


def passage_list_to_str(liste):
    chaine = ""
    for elt in liste:
        chaine += str(elt)
    return chaine


def passage_bin_to_hex(binaire_str):
    return hex(int(binaire_str, 2))


def dico_to_chaine(dico):
    chaine = ""
    for i in range(len(dico)):
        chaine += str(dico[i])
    return chaine


def retour_str(poly):
    chaine = ""
    for i in range(len(poly) - 1):
        if poly[i + 1] == 0:
            chaine += str(0)
        else:
            chaine += str(1)
    return chaine
