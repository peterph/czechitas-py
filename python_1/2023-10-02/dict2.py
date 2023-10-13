####################
### Vysvědčení 2
# Uvažujme vysvědčení, které máme zapsané jako slovník.
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# prumer - secteme znamky pomoci funkce sum(), ktere predame vystup metody
# values() objektu typu dict
a = sum(school_report.values())/len(school_report)

# funkce sum() je vicemene cyklus, ktery bychom mohli zapsat nejak takto:
def sum(l):
    s = 0
    for e in l:
        s += e
    return s

# alternativne muzeme pouzit funkci mean() z modulu statistics:
import statistics
print(statistics.mean(school_report.values()))

# seznam jednicek: pro kazdy prvek ve slovniku se podivame, jestli ma hodnotu 1
# - pokud ano, vypiseme
# priklady:
# s pouzitim list.items()
print("Jednicky:")
for p, z in school_report.items():
    if z == 1:
        print("  " + p)
print("---")

# (implicitnim) pouzitim list.keys() - musime se klicem v kazdem kroku iterace
# odkazovat na hodnotu pomoci school_report[p]
print("Jednicky:")
for p in school_report:
    if school_report[p] == 1:
        print("  " + p)
print("---")

# TEASER START
# v praxi se pouzije spis zkraceny zapis pomoci list comprehension
jednicky = [predmet for predmet, znamka in school_report.items() if znamka == 1]
# vysledek:
# jednicky = ['Český jazyk', 'Anglický jazyk', 'Matematika', 'Dějepis']
# TEASER END


####################
### Čtenářský deník
# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si
# zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si
# eviduje - název knihy, počet stran a hodnocení od 0 do 10.
#
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

# projdeme vsechny prvky seznamu - zaznamy o knizkach a pro kazdy zaznam:
# 1) pricteme pocet stranek do celkoveho poctu (ktery prvotne nastavime na 0)
# 2) pokud je hodnota ulozena pod klicem "rating" vetsi nebo rovna (tedy
# "alespon") 8, udelame si "carku" do promenne good_reads (taky inicializovana
# na 0)
total = 0
good_reads = 0
for b in books:
    total += b["pages"]
    if b["rating"] >= 8:
        good_reads += 1
print(f"celkem stran: {total}")
print(f"dobre knizky: {good_reads}")

####################
### Poznávací značky
# V následujícím slovníků je evidence automobilů.
# Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu.
# Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno
# v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {
    "4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král",
    }

print("V Plzni registrovali:")
# projdeme vsechny polozky pomoci metody items():
# p = RZ (klic ve slovniku),
# o = majitel (hodnota asociovana s klicem)
for p, o in plates.items():
    # druhy znak (index v retezci: 1 je roven 'P')
    if p[1] == 'P':
        print("  " + o)
print("---")

####################
### Recepty
# Pohlédněte na následující reprezentaci receptu a
# Vypište pomocí funkce print kolik bude celé jídlo stát korun
# zaokrouhlené na celé koruny nahoru.

recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

prisady = recept['ingredience']
total = 0
for p in prisady:
    # u kazde prisady naz zajima treti polozka (index v zeznamu je 2)
    c = p[2]
    # .strip() sezere mezery z obou koncu,
    # .split(' ') rozdeli pomoci mezery na seznam (v nasem konkretnim pripade
    #     ne zcela nutne, protoze zadne mezery na zacatku nemame, ale jak
    #     jsem zminoval, je dobre alespon premyslet o tom, kde se muze cela
    #     vec rozbit)
    # [0] vezme prvni prvek vytvoreneho seznamu - to je uz kyzena cena
    ck = c.strip().split(' ')[0]
    # ale pozor! - jako string
    # protoze to muze byt i necele cislo, pouzijeme funkci float(),
    # ktera z retezce vytvori hodnotu typu float
    ckf = float(ck)
    total += ckf

# zkracene by slo vse vyse zapsat samozrejme i takto:
#for p in prisady:
#    total += float(p[2].strip().split(' ')[0])

print(f"nezaokrouhleno: {total}")

# zaokrouhleni nahoru - pouzijme funkci ceil() z modulu math
# ten natahneme do beziciho pythonu
import math
# a funkci muzeme vesele pouzit
print(f"nezaokrouhleno: {math.ceil(total)}")

# TEASER START
# v praxi to opet dopadne jinak, treba spis jako jeden ne uplne trivialne radek
# (ktery bude ale ~2x rychlejsi)
naklady = sum(map(lambda x: float(x[2].strip().split(' ')[0]), recept['ingredience']))
# TEASER END

