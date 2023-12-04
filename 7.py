def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lista = [100, 92, 20, 1, 88, 15, 21]
posortowana_lista = bubble_sort(lista)
print("Posortowana lista:", posortowana_lista)
