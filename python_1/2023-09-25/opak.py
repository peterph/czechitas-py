nazev_hry = "Romeo a Julie"
cena_listku = 150
pocet_listku = 0

vek = int(input("Kolik Vam je let? "))

if (vek < 13):
    print("je mi lito, ale jste prilis mlad pro nakup listku")
else:
    pocet_listku = int(input("kolik chcete listku? "))
    celkova_cena = cena_listku * pocet_listku
    # Pokud je počet lístků alespoň 3, dostane zákazník slevu 10%
    if pocet_listku >= 3:
        zlevnena_cena = celkova_cena * 0.90
        print(f"Cena listků dohromady je {zlevnena_cena} z původních {celkova_cena}.")
    else:
        print(f"Cena listků dohromady je {celkova_cena}.")
