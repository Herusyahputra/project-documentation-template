# from Moildev import Moildev
# import cv2
#
# image = cv2.imread("../SourceImage/image.jpg")
# camera_type = "Raspi"
#
# moil = Moildev("cam_params/camera_parameters.json", camera_type)
# mapx, mapy = moil.getAnypointMaps(0, 50, 4, 2)
# image = cv2.remap(image, mapx, mapy, cv2.INTER_CUBIC)
# result = cv2.resize(image, (800, 600), interpolation=cv2.INTER_AREA)
#
# cv2.imshow("Result", result)
# cv2.waitKey()
import numpy as np
import cv2

# im = cv2.imread('../../SourceImage/image.jpg')
# row, col = im.shape[:2]
# bottom = im[row-2:row, 0:col]
# mean = cv2.mean(bottom)[0]
#
# bordersize = 10
# border = cv2.copyMakeBorder(
#     im,
#     top=bordersize,
#     bottom=bordersize,
#     left=bordersize,
#     right=bordersize,
#     borderType=cv2.BORDER_CONSTANT,
#     value=[mean, mean, mean]
# )
#
# cv2.imshow('image', im)
# cv2.imshow('bottom', bottom)
# cv2.imshow('border', border)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
cap = cv2.VideoCapture("http://192.168.0.69:8000/stream.mjpg")

# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()