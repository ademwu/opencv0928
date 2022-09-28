# OpenCV的影像梯度與邊緣偵測
# 讀圖
import cv2
import numpy as np
img1 = cv2.imread("853e6c09ed811fc1255850fd038b6fa4_c_700_395.png", 0)  # (flag = 0 or 1 or -1)
ret, img = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img)

# Canny邊緣偵測
canny1 = cv2.Canny(img1, 0, 100)
cv2.imshow("canny1", canny1)
canny2 = cv2.Canny(img1, 150, 200)
cv2.imshow("canny2", canny2)
canny3 = cv2.Canny(img1, 60, 150)
cv2.imshow("canny3", canny3)

cv2.waitKey(0)
cv2.destroyAllWindows()