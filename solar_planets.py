import cv2
img=cv2.imread("P-104\solar system.png")
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.putText(img,
            "SUN",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )