neobhodimo_kolichestvo_nailon = int(input())
neobhodimo_kolichestvo_boq = int(input())
kolichestvo_razreditel = int(input())
chasove = int(input())

cena_za_kolichestvo_nailon = (neobhodimo_kolichestvo_nailon + 2 ) * 1.50
cena_za_kolichestvo_boq = (neobhodimo_kolichestvo_boq + neobhodimo_kolichestvo_boq * 10/100) * 14.50
cena_za_razreditel_za_boq = kolichestvo_razreditel * 5
cena_za_torbichki = 0.40
razhodimateriali = cena_za_kolichestvo_nailon + cena_za_kolichestvo_boq + cena_za_razreditel_za_boq + cena_za_torbichki
cena_za_rabota_chas = (razhodimateriali * 30 / 100) * chasove
vsichkirazhodi = razhodimateriali + cena_za_rabota_chas

print(vsichkirazhodi)