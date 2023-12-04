import cv2
# Wczytaj obraz
image = cv2.imread('1.png')

# Współrzędne i wymiary regionu do przycięcia
x = 120
y = 120
width = 200
height = 200

# Przytnij obraz do określonego regionu
cropped_image = image[y:y+height, x:x+width]

# Wyświetl przytnięty obraz
cv2.imshow('Przytnięty obraz', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('obraz_obrocony.jpg', cropped_image)