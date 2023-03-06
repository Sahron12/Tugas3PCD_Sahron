import cv2

# Load the images
img1 = cv2.imread('doraemon1.png')
img1 = cv2.resize(img1, (368, 368))
img2 = cv2.imread('doraemon2.png')
img2 = cv2.resize(img2, (368, 368))

# Average the images
avg_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the averaged image
cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()