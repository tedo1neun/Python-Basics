tax = int(input())

kecove_cena = tax - (40/100 * tax)
basketbolen_ekip_cena = kecove_cena - (20/100 * kecove_cena)
cena_basketbolna_topka = 25/100 * basketbolen_ekip_cena
cena_basketbolni_aksesoari = 20/100 * cena_basketbolna_topka

equipment_price =  tax + kecove_cena + basketbolen_ekip_cena + cena_basketbolna_topka + cena_basketbolni_aksesoari
print(equipment_price)