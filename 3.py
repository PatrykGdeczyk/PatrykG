ciag = "Ala ma kota"
wyrazy = ciag.split()
liczba_wyrazow = len(wyrazy)
print("liczba wyrazow wynosi: ",liczba_wyrazow)

liczba_liter = len(ciag)
print("liczba liter wynosi: ",liczba_liter)

czestotliwosc = {}
for litera in ciag:
    if litera in czestotliwosc:
        czestotliwosc[litera] += 1
    else:
        czestotliwosc[litera] = 1

print("Częstotliwość występowania liter:")
for litera, liczba_wystapien in czestotliwosc.items():
    print(litera, "-", liczba_wystapien)