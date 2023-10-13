import json

# otevru si soubor a nactu ho
with open('zavod1.json', encoding='utf-8') as zavf:
    runners = json.load(zavf)

# sem budu ukladat dobehnuvsi, zatim tam neni nikdo :)
fin = []

# projdu seznam a kdo dobehnul, toho pridam do seznamu
for r in runners:
    # r je slovnik a vypada takhle (viz zdroj dat):
    #
    # {
    #   "jmeno": "jmeno zavodnika", # str
    #   "rocnik": rok,              # int
    #   "casy": {                   # dict
    #       "oficialni": cas,       # str, 'DNF' pokud zavodnik nedokoncil
    #       "1. kolo": cas,         # str
    #       "2.kolo": cas,          # str
    #   }
    # }
    #
    # cas, mne zajima je tedy v r['casy']['oficialni']
    cas = r['casy']['oficialni']
    # dobehl?
    if cas == 'DNF':
        # ne, jdu na dalsi prvek (koncim stavajici pruchod cyklem)
        continue
    # pokud dobehl kod az sem (stale jsme v for cyklu), znamena to, ze zavodnik
    # dobehl ulozim si do seznamu dvojici: (jmeno, cas)
    fin.append( (r['jmeno'], r['casy']['oficialni']) )
    # fin.append() je metoda datoveho typu list, ktera pripoji dalso prvek na
    # konec seznamu.
    #     fin.append(x)
    # je totez co
    #     fin = fin + x
    # samozrejme by mi nic nebranilo, ulozit si tam kompletni informaci o
    # zavodnikovi, aby byla rovno k dispozici:
    # fin.append(r)

# --- data zkontrolovana

# predpokladam, ze data byla serazena (pro neserazena data koukni na
# py_lesson-zavod2.py), takze v mem seznamu, bude informace o druhem v poradi
# prvek s indexem 1. Ten obsahuje jako prvni prvek jmeno (index 0) a druhy
# prvek cas (index 1) takze ve vysleky me zajima prvek s indexem 0 z objektu na
# indexu 1 v seznamu: fin[1][0]
print(f"stribrna: {fin[1][0]}")

