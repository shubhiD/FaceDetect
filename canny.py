#Canny Edge detection is a multistage algo
#1. Noise reduction : for noise reduciton we use a 5x5 gaussian filter
#2. Finding intensity gradient of the image. The smoothed image is then filtered with a sobel kernel to get first direvaitve in both horizontal and vertical direction. From these two images we can find edge gradent and directionfor each pixel as follows
#Edge_Gradient (G) = sqrt(Gx^2 + Gy^2), Angle(theta) = tan^-1(Gy/Gx)
#Gradient direction is always perpendicular to edges.
#Non maximum suppression after getting gradient magnitude and directiona full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient if it forms a local maximum it is considered for next stage otherwise it is suppressed. Thus you get a binary image with "thin edges"
#4 Hyarterises thresholding: this stage decides which all edges are really edges and which are not. for this we need two threshold values minVal and maxVal Any edges with value greater than maxVal is sure to be the edge and one below minVal are sure not edges so discarded. This stage also removes small pixels assuming that edges are long lines so what we finally get is strong edges in the image
#In openCV all the above is put in cv2.Canny(). First arg is our input image. Second and third val are minVal and maxVal next is aperture_size. It is the size of cobel kernel used for find image gradients. By default is 3. last arg is L2gradient which specifies the equation for finding gradient magnitude.  

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Lenna.png', 0)
edges = cv.Canny(img, 50, 100, True, 3)
plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()