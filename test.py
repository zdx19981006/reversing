import cv2 as cv
import Reverse
import numpy as np

if __name__ == '__main__':

    camera_path = "D://test.mkv"
    cap = cv.VideoCapture(camera_path)
    point_size=1
    point_color=(0,0,255)
    thickness=4
    while (cap.isOpened()):
        ret, frame = cap.read()
        Array=Reverse.getPointArray(30)
        for point in Array:
            cv.circle(frame,(point[0],point[1]),point_size,point_color,thickness)
        cv.imshow("hello",frame)
        cv.waitKey(20)

