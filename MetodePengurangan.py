import cv2

# Load the images
img1 = cv2.imread('doraemon1.png')
img1 = cv2.resize(img1, (368, 368))
img2 = cv2.imread('doraemon2.png')
img2 = cv2.resize(img2, (368, 368))

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Subtract the grayscale images
diff = cv2.absdiff(gray1, gray2)

# Display the original images and the difference image side by side
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Difference', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()