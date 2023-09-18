import cv2
import numpy as np
img = cv2.imread('D:/OnlineCourses/ComputerVision_Udacity/02_Repo/ComputerVision/01_Inputs/img_1.jpg')

#add noise to image
mean = 0
stddev = 100
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise,mean,stddev)

noisy_img = cv2.add(img, noise)

cv2.imshow('noisy', noisy_img)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

