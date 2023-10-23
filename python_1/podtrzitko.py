def f3():
    """funkce, ktera vraci trojici hodnot"""
    return "prvni", "2.", 3

f3()

# zajima me jen druha hodnota, tak pouziju podtrzitko, jako "odpadni"
# promennou - a klidne ji pouziju vickrat
# v tomhle pripade v ni bude ve vysledku int(3), protoze ta se priradi
# jako posledni
_, hodnota, _ = f3()
print(hodnota)

# Kdybych chtel jen prvni, tak:
hodnota, _, _ = f3()
print(hodnota)

# PROC?!
# kdybych pouzil:
hodnota = f3()
# bude obsah promenne hodnota cela trojice vracena funkci f3()
print(hodnota)

# a pokud bych v prvnim pripade (pouze druha hodnota je pro mne dulezita)
# pouzil "zkraceny zapis":
#_, hodnota = f3()
# skoncim chybou protoze pocet promennych nalevo (do kterych se prirazuje)
# neodpovida poctu napravo (ktere jsou prirazovany)
