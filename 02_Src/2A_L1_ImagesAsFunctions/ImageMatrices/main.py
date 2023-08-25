import cv2

img = cv2.imread('D:/OnlineCourses/ComputerVision_Udacity/02_Repo/ComputerVision/01_Inputs/img_1.jpg')


img[:,150] = (0, 0, 255)
cv2.imshow('Display', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

