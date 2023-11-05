import cv2 as cv


# rescale
def rescale_frame(frame, scale = 0.5):

    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def read_rescaled_img():
    img = cv.imread('photos/alicia.jpg')

    rescaled_img = rescale_frame(img)

    cv.imshow('Alicia comel', rescaled_img)

    cv.waitKey(0)


# call the function
read_rescaled_img()

