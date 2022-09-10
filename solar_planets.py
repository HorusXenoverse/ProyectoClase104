import cv2

import numpy as np

planets = cv2.imread("solar-system.jpg")


texto = "Sol"
cv2.putText(planets, texto, (80,100), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 5, color=(0,0,255) )

texto2 = "Mercurio"
cv2.putText(planets, texto2, (120,240), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.5, color=(255,255,255) )

texto3 = "Venus"
cv2.putText(planets, texto3, (195,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

texto4 = "Tierra"
cv2.putText(planets, texto4, (280,260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

texto5 = "Marte"
cv2.putText(planets, texto5, (380,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

texto6 = "Jupiter"
cv2.putText(planets, texto6, (570,380), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

texto7 = "Saturno"
cv2.putText(planets, texto7, (750,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

texto8 = "Urano"
cv2.putText(planets, texto8, (970,290), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

texto9 = "Neptuno"
cv2.putText(planets, texto9, (1100,280), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale= 0.8, color=(255,255,255) )

cv2.imshow("Solar planets", planets)
cv2.waitKey(0)