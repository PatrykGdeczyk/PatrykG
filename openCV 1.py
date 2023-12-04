import cv2

# Wczytanie obrazu z dysku
image = cv2.imread('12.jpg')

# Sprawdzenie, czy obraz został wczytany poprawnie
if image is not None:
    # Wyświetlenie obrazu
    cv2.imshow('Obraz', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Nie można wczytać obrazu.')
