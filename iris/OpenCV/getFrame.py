import cv2
import numpy as np
import os

vc = cv2.VideoCapture('video.mp4')
c = 1

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = false

while rval:
    rval, frame = vc.read()
    
    if c < 50:
       cv2.imwrite(str(c) + '.jpg', frame)
       c = c + 1
       cv2.waitKey(10)
       if 0xFF == ord('q'):
           breakpoint()

vc.release()
cv2.destroyAllWindows()
