import cv2
import numpy as np

img = cv2.imread('unknown.jpeg')
window_name = 'image'
img_blur = cv2.blur (img, (3,3))


cv2.imshow(window_name,img)


cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows()





