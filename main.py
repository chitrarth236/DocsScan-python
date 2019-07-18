import cv2
import numpy as np
import scanutils


clicks = list()
cv2.namedWindow('Image')
#mouse callback function
def get_points(event, x, y, flags, param):
    global clicks
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
        clicks.append([x , y])

# Path to your image
img = cv2.imread("newspaper.jpg")
cv2.setMouseCallback("Image",get_points)
while(1):
    cv2.imshow('Image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

maxWidth, maxHeight, rect, dst = scanutils.get_roi(clicks)

M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(img, M, (maxWidth, maxHeight))

cv2.imshow("Cropped",warped)
cv2.imwrite('cropped.jpg',warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
