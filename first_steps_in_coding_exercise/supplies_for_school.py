broi_paketi_himikali = int(input())
broi_paketi_markeri = int(input())
litri_za_pochistvane = int(input())
procent_namalenie = int(input())

cena_za_paket_himikal = broi_paketi_himikali * 5.80
cena_za_paket_markeri = broi_paketi_markeri * 7.20
cena_za_litur_pochistvane = litri_za_pochistvane * 1.20

price = (cena_za_paket_himikal + cena_za_paket_markeri + cena_za_litur_pochistvane)
total_price_with_discount = price - (price * procent_namalenie / 100)
print(total_price_with_discount)
