import cv2
import numpy as np

def autoAdjustments(img):
    #with trackbar
    new_img = np.zeros(img.shape, img.dtype)
    cv2.namedWindow('Output')
    def trackbar(x):
        pass
    cv2.createTrackbar('Alpha','Output',50,300,trackbar)
    cv2.createTrackbar('Beta','Output',0,255,trackbar)

    while (True):
        print(img.mean())
        r = cv2.getTrackbarPos('Alpha', 'Output')
        alpha = r/100
        beta = cv2.getTrackbarPos('Beta', 'Output')

        new_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        print("Alpha: ",alpha)
        print("Beta: ",beta)
        cv2.imshow("Input", input)
        cv2.imshow("Output", new_img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
input = cv2.imread("5.jpg")
autoAdjustments(input)
