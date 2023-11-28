# tombola
import random

for x in range(5):
    print(random.randint(1, 1000))

# s kontrolou opakovani

# promenna na ukladani vylosovanych listku
vyhry = {}

# dokud nevylosuji 3, pokracuji
while len(vyhry) < 3:
    x = random.randint(0, 999)
    # pokud vylosovane cislo nebylo jiz nalezeno, pridam si ho na seznam
    # (cti: # do slovniku) - na zacatku dalsiho cyklu tak bude len(vyhry)
    # o jednu vetsi
    if x not in vyhry:
        vyhry[x] = True
print(list(vyhry.keys()))

"""
stejne tak dobre muzu na seznam vylosovanych listku pouzit typ list, ale pro
radove vetsi data bude citelny rozdil ve vykonu - operace:

    x not in vyhry

je totiz pro seznam obecne casove narocnejsi nez pro slovnik. Strucne: seznam
musi projit cely a kazdy prvek porovnat, pro slovnik se pouzije vhodny
hashovaci algoritmus, ktery klici priradi specifickou hodnotu a ta se pouzije
pro rychly pristup k datum.
"""


# list/dict comprehension

# delitelnost
for x in range(0, 40):
    if ((x % 3) == 0) and ((x % 4) == 0):
        print(f"{x} je delitelne 3 a 4 zaroven")
    if ((x % 5) == 0) or ((x % 6) == 0):
        print(f"{x} je delitelne 5 nebo 6")

# seznamy cisel
cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
print(cisla)
c2 = [2*x for x in cisla]
print(f"krat 2: {c2}")
cm = [-x for x in cisla]
print(f"minus: {cm}")
csq = [x**2 for x in cisla]
print(f"na druhou: {csq}")
cstr = [str(x) for x in cisla]
print(f"jako retezce: {cstr}")

# jmena
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
print(jmena)
jl = [len(x) for x in jmena]
print(f"delky: {jl}")
jv = [x.upper() for x in jmena]
print(jv)
je = [x.lower() + "@email.cz" for x in jmena]
print(je)

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumery = [ (t[0] + t[1] + t[2] + t[3])/4 for t in teploty ]
print(prumery)

ranni = [ t[0] for t in teploty ]
pol_noc = [ [t[1], t[3]] for t in teploty ]
print(pol_noc)

seznam = ['12.03.2014', '10.01.2015', '06.06.1986']
print(['/'.join(datum.split('.')) for datum in seznam])

