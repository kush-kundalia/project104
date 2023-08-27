import cv2
import numpy as np
mer="Mercury"
ven="Venus"
ear="Earth"
mar="Mars"
jup="Jupiter"
sat="Saturn"
ura="Uranus"
nep="Neptune"
sun="Sun"
img = cv2.imread("solar-system.jpg")

cv2.putText(img, sun, (80,30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.25, (0,0,255))
cv2.putText(img, mer, (110,260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, ven, (190,165), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, ear, (290,260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, mar, (380,165), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, jup, (550,400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, sat, (700,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, ura, (950,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))
cv2.putText(img, nep, (1115,280), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (255,255,255))

cv2.imshow("output", img)
cv2.waitKey(0)