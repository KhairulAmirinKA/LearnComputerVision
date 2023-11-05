# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv.imshow('live camera', frame)

    if cv.waitKey(10) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
