import numpy as np
import cv2
import glob

path=glob.glob("E:\Pictures/*jpg") #let us use some other path that has more no. of images
image=[] #make a empty list
for img in path:
    n=cv2.imread(img) #it will read each image from the folder one by one
    image.append(n) #now it will add each image to the list image

#lets resize each image
for i in range(0,len(image)):
    image[i]=cv2.resize(image[i],(400,400)) #this will resize each image in the image list
    # lets us use canny edge in these images
    image[i]=cv2.Canny(image[i],50,255)
#now lets show these images
for i in range(0,len(image)):
    cv2.imshow(str(i),image[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
