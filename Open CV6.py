import cv2

# Wczytanie obrazu
image = cv2.imread('12.jpg')

# Konwersja obrazu na skalę szarości
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Wczytanie klasyfikatora kaskadowego Haara
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detekcja twarzy
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Narysowanie prostokąta wokół każdej wykrytej twarzy
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Wyświetlenie obrazu z zaznaczonymi twarzami
cv2.imshow('Detekcja twarzy', image)
cv2.waitKey(0)
cv2.destroyAllWindows()