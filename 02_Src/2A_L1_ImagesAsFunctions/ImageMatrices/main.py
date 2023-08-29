import cv2

img = cv2.imread('D:/OnlineCourses/ComputerVision_Udacity/02_Repo/ComputerVision/01_Inputs/img_1.jpg')


image_dimensions = img.shape
image_class = img.dtype
#first dimension represents height, second dimension represents width, third dimension represents number of channels
print(image_dimensions)
#represents the data type of the pixel element
print(image_class)

img_red = img[:,:,0]
img_green = img[:,:,1]
img_blue = img[:,:,2]

image_red_dimensions = img_red.shape
print(image_red_dimensions)

cv2.imshow('original', img)
cv2.imshow('Red_window', img_red)
cv2.imshow('Green_window', img_green)
cv2.imshow('Blue_window', img_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

