#!/usr/bin/python3

# prace s globalnimi promennymi

# top je ona - globalni promenna (zije vne vsech funkci) - v drivejsich lekcich to mimochodem byly vsechny :)
X = 50

def pis(q):
    """vypise hodnotu q, zvetsenou o globalni hodnotu X
    """
    print(f"pis: {X + q}", end="")


def prepis(q):
    """zvetsi globalni promennou X o q a vypis ji
    """
    # bez nasledujici radky mi pythoni interpret nepovoli zapis do globalni promenne
    global X
    # ted uz do ni zapsat muzu
    X += q
    print(f"prepis {X}", end="")


def vypis_X():
    print(f" [X = {X}]")


vypis_X()
pis(30) # vypise 80
vypis_X()
pis(20) # vypise 70
vypis_X()
prepis(30) # vypise 80
vypis_X()
pis(20) # vypise... ano, spravne: 100, protoze predchazjici volani prepis() zmenilo hodnotu X
vypis_X()
