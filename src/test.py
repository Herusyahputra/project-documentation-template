# import cv2
#
# # define a video capture object
# vid = cv2.VideoCapture("rtsp://192.168.103.56/axis-media/media.amp")
#
# while (True):
#
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

import cv2

img = cv2.imread('../SourceImage/enthaniya.png', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)
width = int(img.shape[1] * 75 / 100)
height = int(img.shape[0] * 75 / 100)

print(round(1295 * (75 / 100)))
print(round(972 * (75 / 100)))
print(round(4.05 * (75 / 100)))

# dsize
dsize = (width, height)

# resize image
resized = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
cv2.imwrite("../SourceImage/test_resize.jpg", resized)

print('Resized Dimensions : ', resized.shape)
