# """A simple example of capturing and displaying an image
# """
# import EasyPySpin
# import cv2
#
#
# def main():
#     cap = EasyPySpin.VideoCapture(0)
#     writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'XVID'), 15, (4000, 3000))
#     # fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
#     # # video_writer = cv2.VideoWriter("output.avi", fourcc, 25, (w, h))
#
#     if not cap.isOpened():
#         print("Camera can't open\nexit")
#         return -1
#
#     cap.set(cv2.CAP_PROP_EXPOSURE, 7500)  # -1 sets exposure_time to auto
#     cap.set(cv2.CAP_PROP_GAIN, -1)  # -1 sets gain to auto
#
#     while True:
#         ret, frame = cap.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BayerBG2BGR)  # for RGB camera demosaicing
#         # cv2.imwrite("test3.jpg", frame)
#         # writer.write(frame)
#         img_show = cv2.resize(frame, None, fx=0.25, fy=0.25)
#         cv2.imshow("press q to quit", img_show)
#         key = cv2.waitKey(30)
#         if key == ord("q"):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     main()

try:
    import keras
    print('\nModule was installed')
except ImportError:
    print('\nThere was no such module installed')