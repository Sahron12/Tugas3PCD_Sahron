import cv2

# Load the two images
img1 = cv2.imread('doraemon1.png')
img1 = cv2.resize(img1, (368, 368))
img2 = cv2.imread('doraemon2.png')
img2 = cv2.resize(img2, (368, 368))

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)

thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cv2.imshow('Difference Image', thresh)
cv2.waitKey(0)