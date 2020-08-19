
#  import cv2
from cv2 import cv2 as cv
from matplotlib import pyplot as plt


# def test(img)
img = cv.imread('test.jpg')
# img = cv.imread('temp01.jpg')
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
engine = cv.CascadeClassifier('cascade.xml')

# engine.load('C:/Users/23672/Desktop/实习文件/mysite/AI/CV/cascade.xml')


pipeline = engine.detectMultiScale(img, scaleFactor=1.3, minNeighbors=100, minSize=(100, 100))

for (x, y, w, h) in pipeline:
    img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

# cv.imshow('img', img)
cv.imwrite('../static/AI/result.jpg',img)
# plt.figure()
# plt.imshow(img)
# plt.imshow(img)
print('已识别排水管位置')
# cv.waitKey(0)
# cv.destroyAllWindows()



# %%
