def km_na_miile(km):
    mile = km * 0.621371
    return mile

def konwertuj_celsjusze_na_fahrenheity(celsjusze):
    fahrenheity = (celsjusze * 9/5) + 32
    return fahrenheity

def konwertuj_metry_na_stopy(metry):
    stopy = metry * 3.28084
    return stopy

def konwertuj_kilogramy_na_funty(kilogramy):
    funty = kilogramy * 2.20462
    return funty

def konwertuj_litry_na_galony(litry):
    galony = litry * 0.264172
    return galony

wybor = int(input("Wybierz kod (1-5): "))

if wybor == 1:
    km = int(input("Podaj kilometry: "))
    mile = km_na_miile(km)
    print(f"{km} kilometrów to {mile} mil")
elif wybor == 2:
    celsjusze = int(input("Podaj stopnie Celsjusza: "))
    fahrenheity = konwertuj_celsjusze_na_fahrenheity(celsjusze)
    print(f"{celsjusze} stopni Celsjusza to {fahrenheity} stopni Fahrenheita.")
elif wybor == 3:
    metry = int(input("Podaj metry: "))
    stopy = konwertuj_metry_na_stopy(metry)
    print(f"{metry} metrów to {stopy} stóp.")
elif wybor == 4:
    kilogramy = int(input("Podaj kilogramy: "))
    funty = konwertuj_kilogramy_na_funty(kilogramy)
    print(f"{kilogramy} kilogramów to {funty} funtów.")
elif wybor == 5:
    litry = int(input("Podaj litry: "))
    galony = konwertuj_litry_na_galony(litry)
    print(f"{litry} litrów to {galony} galonów.")
else:
    print("Nieprawidłowy wybór kodu.")
