import cv2

# Wczytaj obraz kolorowy
image = cv2.imread('1.png')

# Przekonwertuj obraz na skalę szarości
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Wyświetl oba obrazy
cv2.imshow('Obraz kolorowy', image)
cv2.imshow('Obraz w skali szarości', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('1.png', gray_image)