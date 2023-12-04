def sprawdz_liczbe(liczba):
    if liczba %2 == 0:
     print("liczba" ,liczba,"jest parzysta")
    else:
       print("liczba" ,liczba ,"nie jest parzysta ")
liczba =int(input("podaj liczbe :"))
sprawdz_liczbe(liczba)