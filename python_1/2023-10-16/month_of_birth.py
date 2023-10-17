#!/usr/bin/python3

# mesic narozenin z rodneho cisla, pouzijeme modul 'calendar', protoze jsme
# lini psat, co nam uz nekdo napsal (a lepe)
import calendar


def mob(rc):
    """vypise mesic narozeni z rodneho cisla
    vrati False, pokud je mesic 'mimo'
    """
    m = int(rc[2:4])
    # u zen se k poradovemu cislu mesice pridava 50
    if m > 50:
        m -= 50

    # kontrola, ze mesic je rozumny (abychom pripadne neskoncili vyjimkou
    # IndexError), pripadne necim horsim: pokud by podminka nahore byla
    # napriklad:
    #   if m > 12:
    #       m -= 50
    # pak by pro vstup '9048....' byla hodnota m = -2, zcela validni index do
    # seznamu mesicy (konkretne samozrejme listopad, jako druhy od konce)
    if m < 1 or m > 12:
        return False
    else:
        return calendar.month_name[m]


print(mob('905410/1234'))

