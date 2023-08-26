import cv2

img = cv2.imread('D:/OnlineCourses/ComputerVision_Udacity/02_Repo/ComputerVision/01_Inputs/img_1.jpg')

cv2.imshow('Display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_dimensions = img.shape
image_class = img.dtype
#first dimension represents height, second dimension represents width, third dimension represents number of channels
print(image_dimensions)
#represents the data type of the pixel element
print(image_class)


modified_img = cv2.rectangle(img, (50, 200), (50, 200), (255, 0, 0), 1)
cv2.imshow('Modified Display',modified_img)
cv2.waitKey(0)
cv2.destroyAllWindows()