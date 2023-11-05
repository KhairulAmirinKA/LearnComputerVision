import cv2 as cv


# rescale. works for video, img, live video
def rescaleFrame(frame, scale=0.75):
    height = int( frame.shape[0]*scale)
    width = int( frame.shape[1] * scale )

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


#change resolution for live video
def changeResolution_liveVideo(width, height):
    capture = cv.VideoCapture(0)

    capture.set(3, width)
    capture.set(4, height)


# reading video
def read_video():
    capture = cv.VideoCapture('videos/Digimon Xros Wars Opening 1.mp4')

    while True:
        isTrue, frame = capture.read()  # frame by frame

        frame_resized = rescaleFrame(frame)  # resize the frame

        cv.imshow('Digimon video', frame)
        cv.imshow('Digimon resized video', frame_resized)

        if cv.waitKey(10) & 0xFF == ord('d'):
            break  # when d is hit, break

    capture.release()
    cv.destroyAllWindows()


read_video()


