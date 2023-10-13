import json

# otevru si soubor a nactu ho
with open('zavod2.json', encoding='utf-8') as zavf:
    runners = json.load(zavf)

# sem budu ukladat dobehnuvsi, zatim tam neni nikdo :)
fin = {}

# projdu seznam a kdo dobehnul, toho pridam do slovniku - klicem bude cas,
# hodnota bude seznam jmen (protoze zavodniku se stejnym casem muze byt vice)
for r in runners:
    # stejne jako predchazejici
    cas = r['casy']['oficialni']
    # dobehl?
    if cas == 'DNF':
        # ne, jdu na dalsi prvek (koncim stavajici pruchod cyklem)
        continue
    # pokud dobehl kod az sem (stale jsme v for cyklu), chci pridat do slovniku
    # k danemu klici aktualni jmeno
    # pokud ale dany cas ve slovniku jeste neni, musim vytvorit seznam
    # obsahujici aktualni jmeno kod by tedy vypal nejak takto:
    """
    if cas in fin:
        fin[cas].append(r['jmeno'])
    else:
        fin[cas] = [r['jmeno']]
    """
    # to ale neni uplne elegantni - co kdyz v nejakou chvili budu chtit provest
    # slozitejsi operaci, nez jen pripojeni k seznamu?
    # radeji se pokusim rozdelit kroky tak, abych provadel vzdy stejnou akci
    # pro kazdy zaznam a pripadne odlisnosti izoloval
    if cas not in fin:
        # zajistim, aby v kazdem pripade existoval seznam, do ktereho mohu
        # pridavat
        fin[cas] = []
    # a ted to mohu vesele provest co potrebuji bez ohledu na to, zda jde o
    # prvniho nebo nejakeho nasledneho zavodnika s danym casem
    fin[cas].append(r['jmeno'])

# nyni mam slovnik, ktery vypada takto:
# {
#   "3:00:09": [
#     "Brunner Radek",
#     "Prazak Stanislav"
#   ],
#   "3:05:21": [
#     "Zeleny Michal"
#   ],
#   "2:57:37": [
#     "Dvorak Kamil"
#   ],
#   "3:11:44": [
#     "Urban Jaroslav"
#   ],
#   "3:12:21": [
#     "Andrle Jakub"
#   ]
# }

# seradim si casy - klice pomoci sunkce sorted(), ktera vraci serazen
casy = sorted(fin.keys())

# o stribro se deli ti, co dobehli v case casy[1], takze:
print("druhy nejlepsi cas mel(i): {}".format(", ".join(fin[casy[1]])))

# TODO
# bonus ukol - zkuste si rozmyslet nasledujici:
#
# 1) proc asi funguje razeni casu, kdyz to jsou retezce - Python a priori nevi,
#    ze je ma intepretovat jako cas
#
# 2) jak by se razeni mohlo rozbit, zkuste nalezt alespon jeden priklad
#    vyznamove korektniho vstupu (takoveho, ktery by kod interpretoval jinak,
#    nez clovek implicitne vidici za timto retezcem casovy udaj)
#
# 3) co s ohledem na nalezeny protipriklad udelat, aby "to fungovalo"
