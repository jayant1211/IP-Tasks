import cv2

img = cv2.imread("3.jpg")
b,g,r=cv2.split(img)
equb = cv2.equalizeHist(b)
equg = cv2.equalizeHist(g)
equr = cv2.equalizeHist(r)
equ = cv2.merge((equb,equg,equr))
cv2.imshow("Input",img)
cv2.imshow("Output",equ)
cv2.waitKey()