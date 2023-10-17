#!/usr/bin/python3

def ramecek(text, ram='*'):
    """vypis etxt zvolenym znakem
    @text - text, ktery ma byt oramovan
    @znak - znak kterym ma byt ramecek nakreslen
    """
    # predpokladame, ze @znak je retezec, ale muze zaludne obsahovat vice
    # znaku, takze si vezmeme pouze prvni
    # NOTE: uzivatel muze take zadat prazdny retezec - v tom pripade dojde k
    # chybe, stejne jako kdyz nam da odkaz na cokoliv jineho, nez retezec
    # (treba cislo)
    ram = ram[0]
    
    # kolik znaku je potreba na vodorovnou cast ramecku: delak textu ve znacich
    # + na kazde strane 2 dalsi znaky na svisly ramecek a mezeru mezi rameckem
    # a textem
    delka = len(text) + 4

    print(delka * ram)
    print(f'{ram} {text} {ram}')
    print(delka * ram)
    # neni nutno psat explicitne, ale stare zvyhy umiraji pomalu (pokud vubec)
    return


for t in ['ahoj', 'nazdar', 'na shledanou']:
    ramecek(t, 'XX')

