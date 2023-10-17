#!/usr/bin/python3

# prevody stupnu
def c2f(c):
    """prevod Celsiovy stupnice na Fahrenheitovu
    """
    # x [°F] = 9/5 * x[°C] + 32
    f = ((9 / 5) * c) + 32
    return f

def f2c(f):
    """prevod Fahrenheitovy stupnice na Celsiovu
    """
    return (5 / 9) * (f - 32)

# testovaci vypis pro nekolik zajimavych hodnot
# formatovane retezce (f"...") umi vic, nez jen vypsat hodnotu - lze
# specifikovat jak ma vystup vypadat
# s vyhodou lze vyuzit {var:fmt} - pred dvojteckou vyraz k vypsani, za
# dvojteckou format - napr. {x:10d} vyupise cele cislo v promenne x jako
# alespon 10 znaku dlouhy retezec (odsazeny mezerami)
#
# vice k formatum na:
# https://docs.python.org/3/library/string.html#formatstrings
#
# nebo pretlumocene:
# https://realpython.com/python-formatted-output/#the-format_spec-component

for n in [0, 10, 32, 40, 100, 212, 451]:
    print(f"{n:4d} °F = {f2c(n):7.2f} °C")
#              ^^               ^^^^
#   cele cislo na sirku     desetinne cislo (f = float), celkova sirka alespon
#   4 znaku                 7 znaku, z toho 2 desetinna mista, jedna tecka
#                           a nezapomenout na pripadne minus

print("-------------")

for n in [-10, 0, 10, 32, 40, 100, 233]:
    print(f"{n:4d} °C = {c2f(n):10.1f} °F")

