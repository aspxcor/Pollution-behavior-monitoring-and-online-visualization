import cv2

img = cv2.imread('3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

engine = cv2.CascadeClassifier('cascade.xml')
pipeline = engine.detectMultiScale(img, scaleFactor=1.1, minNeighbors=100, minSize=(10, 10))

for (x, y, w, h) in pipeline:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

