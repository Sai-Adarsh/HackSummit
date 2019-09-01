import sys
import cv2

fname=sys.argv[1]

print("FILENAME: "+fname)

img=cv2.imread(fname)

img=cv2.applyColorMap(img,cv2.COLORMAP_JET)
img=cv2.bitwise_not(img)

cv2.imwrite(fname,img)
