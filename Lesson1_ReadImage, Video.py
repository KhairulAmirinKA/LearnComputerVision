import cv2 as cv


# reading image
def read_image():
    img = cv.imread('photos/alicia.jpg')

    cv.imshow("Alicia comel", img)
    cv.waitKey(0)


# reading video
def read_video():
    capture = cv.VideoCapture('videos/Digimon Xros Wars Opening 1.mp4')

    while True:
        isTrue, frame = capture.read()  # frame by frame
        cv.imshow('Digimon video', frame)

        if cv.waitKey(10) & 0xFF == ord('d'):
            break  # when d is hit, break

    capture.release()
    cv.destroyAllWindows()



# read_image()

read_video()
