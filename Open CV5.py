import cv2

# Wczytanie obrazu w skali szarości
image = cv2.imread('obraz_szary.jpg', 0)

# Zastosowanie algorytmu Canny do detekcji krawędzi
edges = cv2.Canny(image, 100, 200)

# Wyświetlenie wyniku
cv2.imshow('Detekcja krawędzi', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()