import cv2 as cv

img = cv.imread('boy.bmp',0)
img_gaussian = cv.GaussianBlur(img,(5,5),0)
_, thresh1 = cv.threshold(img_gaussian, 127, 255, cv.THRESH_BINARY)
thresh2 = cv.adaptiveThreshold(img_gaussian, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2); #threshold value is the mean of neighbourhood pixel values.
thresh3 = cv.adaptiveThreshold(img_gaussian, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2); #threshold value is the weighted sum of neighbourhood pixel values


cv.imshow("Original Image", img)
cv.imshow("Denoised Image",img_gaussian)
cv.imshow("Global Thresholding", thresh1)
cv.imshow("Adap Mean", thresh2)
cv.imshow("Adap Gauss", thresh3)

cv.waitKey(0)
cv.destroyAllWindows()    

#OBSERVATION
#Unlike the global thresholding technique, adaptive thresholding chooses different threshold values 
#for every pixel in the image based on an analysis of its neighboring pixels. This helps in getting 
#improved results in case of images with varying contrast levels where a global thresholding technique will not work satisfactorily.      


