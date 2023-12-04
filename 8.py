suma = 0

while True:
    liczba = input("Wprowadź liczbę lub wpisz 'stop' aby zakończyć: ")
    
    if liczba == "stop":
        break
    
    try:
        liczba = int(liczba)
        suma += liczba
    except ValueError:
        print("Wprowadzona wartość nie jest liczbą. Spróbuj ponownie.")

print("Suma wprowadzonych liczb to:", suma)