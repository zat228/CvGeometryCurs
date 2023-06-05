from __future__ import print_function
from __future__ import division
import cv2
alpha_slider_max = 300
img = cv2.imread("1.png")
imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
template = cv2.imread("5.png")


def on_trackbar(val):
    ret, thresh1 = cv2.threshold(imgray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow("title_window", thresh1)


cv2.namedWindow("title_window")
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv2.createTrackbar(trackbar_name, "title_window", 0, alpha_slider_max, on_trackbar)
on_trackbar(0)


cv2.waitKey(0)