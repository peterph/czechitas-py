####################
### vysvedceni
vysv = {
    "M": 1,
    "Cj": 2,
    "Tv": 2,
}
print(vysv);

### prodeje knih
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"] + 10
# zkracene:
#sales["Vrah zavolá v deset"] += 10
print(sales)


####################
### tombola
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

l = int(input("Cislo listku: "))
if l in tombola:
    print("Tvoje vyhra: " + tombola[l])
else:
    print("Nevyhravas")


####################
### paranoidni vecirek
pwds = {
        "J": "taj",
        "N": "vic-taj",
        "K": "", # prazdne heslo!
    }

n = input("jmeno: ")
if n in pwds:
    p = input("heslo: ")
    if p == pwds[n]:
        print("ok")
    else:
        print("chyba!")
else:
    print("tebe neznam")
