import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os


class MyImageProcessingProject:

    def getImageSize(self, image_location):
        img = Image.open(image_location)
        img_width, img_height = img.size
        print(str(img_width), " * ", str(img_height))


    def getPixelValue(self, image_location):
        img = Image.open(image_location)
        image_pixel = img.load()

    def loadImage(self, img_loc):
        actual_image =cv2.imread(img_loc)
        grey_image = cv2.cvtColor(actual_image, cv2.COLOR_BGR2GRAY)
        return grey_image

    def image_convolution(self, image_mat, kernel_mat):
        #kernel_mat = np.flipud(np.fliplr(kernel_mat))
        output_image = np.zeros_like(image_mat)
        image_padded = np.zeros((image_mat.shape[0] + 2, image_mat.shape[1] + 2))
        image_padded[1:-1, 1:-1] = image_mat

        for x in range(image_mat.shape[1]):
            for y in range(image_mat.shape[0]):
                output_image[y, x] = (kernel_mat * image_padded[y: y + 3, x: x + 3]).sum()

        return output_image



my_proj = MyImageProcessingProject()
image_location = 'src/input_img.jpg'

input_image = my_proj.loadImage(image_location)

image_edge1 = my_proj.image_convolution(input_image, kernel_mat=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
cv2.imwrite('src' + 'edge_detection_4.jpg', image_edge1)



