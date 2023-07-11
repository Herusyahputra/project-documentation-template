import numpy as np
from PyQt5 import QtCore, QtGui
import cv2
import RatioImage
import Apps_FaceDetection
from ShowResult import ShowImageResult


class MultipleView:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.pushButton_2.clicked.connect(self.multipleView)
        self.parent.ui.threeView.clicked.connect(self.controlVIew)
        self.parent.ui.sixView.clicked.connect(self.controlVIew)
        self.parent.ui.nineView.clicked.connect(self.controlVIew)

        # self.parent.ui.window_LT.mousePressEvent = self.onclickWindow_LT
        # self.parent.ui.window_T.mousePressEvent = self.onclickWindow_T
        # self.parent.ui.window_RT.mousePressEvent = self.onclickWindow_RT
        # self.parent.ui.window_L.mousePressEvent = self.onclickWindow_L
        # self.parent.ui.window_Center.mousePressEvent = self.onclickWindow_Center
        # self.parent.ui.window_R.mousePressEvent = self.onclickWindow_R
        # self.parent.ui.window_LB.mousePressEvent = self.onclickWindow_LB
        # self.parent.ui.window_B.mousePressEvent = self.onclickWindow_B
        # self.parent.ui.window_RB.mousePressEvent = self.onclickWindow_RB

    def initMapMulti(self, image):
        imageHeight, imageWidth = image.shape[:2]
        mapX = np.zeros((imageHeight, imageWidth), dtype=np.float32)
        mapY = np.zeros((imageHeight, imageWidth), dtype=np.float32)
        return mapX, mapY

    # def calculateMap(self):
    #     if self.ui.radioAnypointM1.isChecked():
    #         self.moildev.AnyPointM(self.mapX_1, self.mapY_1, self.imageWidth, self.imageHeight, self.alpha,
    #                                self.beta, self.zoom, self.m_ratio)
    #         print(">>>>>>>> map X <<<<<<<<<<")
    #         print(self.mapX)
    #
    #     elif self.ui.radioAnypointM2.isChecked():
    #         self.moildev.AnyPointM2(self.mapX_1, self.mapY_1, self.imageWidth, self.imageHeight, self.alpha,
    #                                 self.beta, self.zoom, self.m_ratio)

    def multipleView(self):
        if self.parent.multiView:
            self.controlFrameHide()
            self.parent.ui.pushButton_2.setStyleSheet('background-color: rgb(238, 238, 236);')
            self.parent.ui.pushButton_2.setText("Multiple View")
            self.parent.multiView = False

        else:
            if self.parent.ui.comboBox.currentIndex() == 2:
                self.controlFrameShow()
                self.parent.ui.gridFrame.hide()
                self.parent.ui.gridFrame_surveillance.show()
            else:
                self.controlFrameShow()
                self.parent.ui.gridFrame_surveillance.hide()
                self.parent.ui.gridFrame.show()

            self.parent.ui.pushButton_2.setStyleSheet("background-color: rgb(115, 210, 22);")
            self.parent.ui.pushButton_2.setText("Single View")
            self.parent.multiView = True

    def controlFrameShow(self):
        self.parent.ui.windowResult.hide()
        self.parent.ui.PlussIcon.hide()
        self.parent.ui.scrollArea_3.setMaximumSize(QtCore.QSize(16777215, 16777215))

    def controlFrameHide(self):
        self.parent.ui.windowResult.show()
        self.parent.ui.PlussIcon.show()
        self.parent.ui.scrollArea_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.parent.ui.gridFrame.hide()
        self.parent.ui.gridFrame_surveillance.hide()

    def controlVIew(self):
        if self.parent.ui.threeView.isChecked():
            self.parent.ui.frame_LT.hide()
            self.parent.ui.frame_T.hide()
            self.parent.ui.frame_RT.hide()
            self.parent.ui.frame_L.show()
            self.parent.ui.frame_C.show()
            self.parent.ui.frame_R.show()
            self.parent.ui.frame_LB.hide()
            self.parent.ui.frame_B.hide()
            self.parent.ui.frame_RB.hide()
        elif self.parent.ui.sixView.isChecked():
            self.parent.ui.frame_LT.hide()
            self.parent.ui.frame_T.hide()
            self.parent.ui.frame_RT.hide()
            self.parent.ui.frame_L.show()
            self.parent.ui.frame_C.show()
            self.parent.ui.frame_R.show()
            self.parent.ui.frame_LB.show()
            self.parent.ui.frame_B.show()
            self.parent.ui.frame_RB.show()
        elif self.parent.ui.nineView.isChecked():
            self.parent.ui.frame_LT.show()
            self.parent.ui.frame_T.show()
            self.parent.ui.frame_RT.show()
            self.parent.ui.frame_L.show()
            self.parent.ui.frame_C.show()
            self.parent.ui.frame_R.show()
            self.parent.ui.frame_LB.show()
            self.parent.ui.frame_B.show()
            self.parent.ui.frame_RB.show()

    def multiView(self, image, with_img):
        self.ui.frame_LT.hide()
        self.ui.frame_T.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()
        # display_LT(self, image, with_img)
        # display_T(self, image, with_img)
        # display_RT(self, image, with_img)
        display_L(self, image, with_img)
        display_center(self, image, with_img)
        display_R(self, image, with_img)
        # display_LB(self, image, with_img)
        # display_B(self, image, with_img)
        # display_RB(self, image, with_img)

    def display_LT(self, image, width_img):
        print(self.camera)
        mapX = np.load('MapsImage/mapX_LT.npy')
        mapY = np.load('MapsImage/mapY_LT.npy')
        self.ui.window_LT.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_12.setMinimumSize(QtCore.QSize(width_img, 0))
        image_LT = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        image_LT = RatioImage.ratioResult(self, image_LT, width_img)
        normal_image = QtGui.QImage(image_LT.data, image_LT.shape[1],
                                    image_LT.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_LT.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_LT_Maxi(self, image, width_img):
        display_LT(self, image, width_img)
        self.ui.frame_LT.show()
        self.ui.frame_T.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_LT_Mini(self, image, width_img):
        display_LT(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.show()
        self.ui.frame_B.show()
        self.ui.frame_RB.show()

    def display_T(self, image, width_img):
        mapX = np.load('MapsImage/mapX_T.npy')
        mapY = np.load('MapsImage/mapY_T.npy')
        self.ui.window_T.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_21.setMinimumSize(QtCore.QSize(width_img, 0))
        image_T = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        image_T = RatioImage.ratioResult(self, image_T, width_img)
        normal_image = QtGui.QImage(image_T.data, image_T.shape[1],
                                    image_T.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_T.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_T_Maxi(self, image, width_img):
        display_T(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_T_Mini(self, image, width_img):
        display_T(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_LT.show()
        self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.show()
        self.ui.frame_B.show()
        self.ui.frame_RB.show()

    def display_RT(self, image, width_img):
        mapX = np.load('MapsImage/mapX_RT.npy')
        mapY = np.load('MapsImage/mapY_RT.npy')
        self.ui.window_RT.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_33.setMinimumSize(QtCore.QSize(width_img, 0))
        image_RT = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        image_RT = RatioImage.ratioResult(self, image_RT, width_img)
        normal_image = QtGui.QImage(image_RT.data, image_RT.shape[1],
                                    image_RT.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_RT.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_RT_Maxi(self, image, width_img):
        display_RT(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.show()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_RT_Mini(self, image, width_img):
        display_RT(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_LT.show()
        self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.show()
        self.ui.frame_B.show()
        self.ui.frame_RB.show()

    def display_L(self, image, width_img):
        if self.camera == "axis":
            mapX = np.load('MapsImage/axis/mapX_L.npy')
            mapY = np.load('MapsImage/axis/mapY_L.npy')
        else:
            mapX = np.load('MapsImage/mapX_L.npy')
            mapY = np.load('MapsImage/mapY_L.npy')
        self.ui.window_L.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_34.setMinimumSize(QtCore.QSize(width_img, 0))
        image_L = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        if self.ui.CheckFaceDetect.isChecked():
            image_L = Apps_FaceDetection.faceDetect(image_L)
        else:
            image_L = image_L
        # print(self.ui.CheckFaceDetect.isChecked())
        image_L = RatioImage.ratioResult(self, image_L, width_img)
        normal_image = QtGui.QImage(image_L.data, image_L.shape[1],
                                    image_L.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_L.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_L_Maxi(self, image, width_img):
        display_L(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.show()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_L_Mini(self, image, width_img):
        display_L(self, image, width_img)
        # self.ui.frame_T.show()
        # self.ui.frame_LT.show()
        # self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        # self.ui.frame_LB.show()
        # self.ui.frame_B.show()
        # self.ui.frame_RB.show()

    def display_center(self, image, width_img):
        if self.camera == "axis":
            mapX = np.load('MapsImage/axis/mapX_c.npy')
            mapY = np.load('MapsImage/axis/mapY_c.npy')
        else:
            mapX = np.load('MapsImage/mapX_center.npy')
            mapY = np.load('MapsImage/mapY_center.npy')
        self.ui.window_Center.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_35.setMinimumSize(QtCore.QSize(width_img, 0))
        image_center = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        if self.ui.CheckFaceDetect.isChecked():
            image_center = Apps_FaceDetection.faceDetect(image_center)
        else:
            image_center = image_center
        image_center = RatioImage.ratioResult(self, image_center, width_img)
        normal_image = QtGui.QImage(image_center.data, image_center.shape[1],
                                    image_center.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_Center.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_center_Maxi(self, image, width_img):
        display_center(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.show()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_center_Mini(self, image, width_img):
        display_center(self, image, width_img)
        # self.ui.frame_T.show()
        # self.ui.frame_LT.show()
        # self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        # self.ui.frame_LB.show()
        # self.ui.frame_B.show()
        # self.ui.frame_RB.show()

    def display_R(self, image, width_img):
        if self.camera == "axis":
            mapX = np.load('MapsImage/axis/mapX_R.npy')
            mapY = np.load('MapsImage/axis/mapY_R.npy')
        else:
            mapX = np.load('MapsImage/mapX_R.npy')
            mapY = np.load('MapsImage/mapY_R.npy')
        self.ui.window_R.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_36.setMinimumSize(QtCore.QSize(width_img, 0))
        image_R = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        if self.ui.CheckFaceDetect.isChecked():
            image_R = Apps_FaceDetection.faceDetect(image_R)
        else:
            image_R = image_R
        image_R = RatioImage.ratioResult(self, image_R, width_img)
        normal_image = QtGui.QImage(image_R.data, image_R.shape[1],
                                    image_R.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_R.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_R_Maxi(self, image, width_img):
        display_R(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.show()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_R_Mini(self, image, width_img):
        display_R(self, image, width_img)
        # self.ui.frame_T.show()
        # self.ui.frame_LT.show()
        # self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        # self.ui.frame_LB.show()
        # self.ui.frame_B.show()
        # self.ui.frame_RB.show()

    def display_LB(self, image, width_img):
        mapX = np.load('MapsImage/mapX_LB.npy')
        mapY = np.load('MapsImage/mapY_LB.npy')
        self.ui.window_LB.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_53.setMinimumSize(QtCore.QSize(width_img, 0))
        image_LB = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        image_LB = RatioImage.ratioResult(self, image_LB, width_img)
        normal_image = QtGui.QImage(image_LB.data, image_LB.shape[1],
                                    image_LB.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_LB.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_LB_Maxi(self, image, width_img):
        display_LB(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.show()
        self.ui.frame_B.hide()
        self.ui.frame_RB.hide()

    def Window_LB_Mini(self, image, width_img):
        display_LB(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_LT.show()
        self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.show()
        self.ui.frame_B.show()
        self.ui.frame_RB.show()

    def display_B(self, image, width_img):
        mapX = np.load('MapsImage/mapX_B.npy')
        mapY = np.load('MapsImage/mapY_B.npy')
        self.ui.window_B.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_52.setMinimumSize(QtCore.QSize(width_img, 0))
        image_B = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        image_B = RatioImage.ratioResult(self, image_B, width_img)
        normal_image = QtGui.QImage(image_B.data, image_B.shape[1],
                                    image_B.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_B.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_B_Maxi(self, image, width_img):
        display_B(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.show()
        self.ui.frame_RB.hide()

    def Window_B_Mini(self, image, width_img):
        display_B(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_LT.show()
        self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.show()
        self.ui.frame_B.show()
        self.ui.frame_RB.show()

    def display_RB(self, image, width_img):
        mapX = np.load('MapsImage/mapX_RB.npy')
        mapY = np.load('MapsImage/mapY_RB.npy')
        self.ui.window_RB.setMinimumSize(QtCore.QSize(width_img, 0))
        self.ui.label_47.setMinimumSize(QtCore.QSize(width_img, 0))
        image_RB = cv2.remap(image, mapX, mapY, cv2.INTER_CUBIC)
        image_RB = RatioImage.ratioResult(self, image_RB, width_img)
        normal_image = QtGui.QImage(image_RB.data, image_RB.shape[1],
                                    image_RB.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.window_RB.setPixmap(QtGui.QPixmap.fromImage(normal_image))

    def Window_RB_Maxi(self, image, width_img):
        display_RB(self, image, width_img)
        self.ui.frame_T.hide()
        self.ui.frame_LT.hide()
        self.ui.frame_RT.hide()
        self.ui.frame_L.hide()
        self.ui.frame_C.hide()
        self.ui.frame_R.hide()
        self.ui.frame_LB.hide()
        self.ui.frame_B.hide()
        self.ui.frame_RB.show()

    def Window_RB_Mini(self, image, width_img):
        display_RB(self, image, width_img)
        self.ui.frame_T.show()
        self.ui.frame_LT.show()
        self.ui.frame_RT.show()
        self.ui.frame_L.show()
        self.ui.frame_C.show()
        self.ui.frame_R.show()
        self.ui.frame_LB.show()
        self.ui.frame_B.show()
        self.ui.frame_RB.show()


    def onclickWindow_LT(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_LT_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_LT_Mini(self, self.image, 640)
                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_LT_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_LT_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 1

    def onclickWindow_T(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_T_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_T_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_T_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_T_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 2

    def onclickWindow_RT(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_RT_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_RT_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_RT_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_RT_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 3

    def onclickWindow_L(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_L_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_L_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_L_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_L_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 4

    def onclickWindow_Center(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_center_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_center_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_center_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_center_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 5

    def onclickWindow_R(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_R_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_R_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_R_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_R_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 6

    def onclickWindow_LB(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_LB_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_LB_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_LB_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_LB_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 7

    def onclickWindow_B(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_B_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_B_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_B_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_B_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 8

    def onclickWindow_RB(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            if self.maxi:
                if self.maximizedMultiWindow:
                    MutipleView.Window_RB_Maxi(self, self.image, 1800)
                    self.maximizedMultiWindow = False
                else:
                    MutipleView.Window_RB_Mini(self, self.image, 640)

                    self.maximizedMultiWindow = True
            else:
                if self.maximizedMultiWindow is False:
                    MutipleView.Window_RB_Maxi(self, self.image, 1300)
                    self.maximizedMultiWindow = True
                else:
                    MutipleView.Window_RB_Mini(self, self.image, 400)
                    self.maximizedMultiWindow = False
        self.displayW = 9
