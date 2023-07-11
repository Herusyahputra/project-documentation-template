import sys
import cv2
import os
import numpy as np
import datetime
from MoildevUi.MoildevAppsUi import *
from Utils import read_image, saveImage, select_file
from InitMoildev import Config
from Moildev import Moildev
from VideoControler import Video_Controler
from View_Anypoint import AnyPoint
from View_Panorama import Panorama
from Ui_FastView import FastView
from Aplication import Application
from Ui_MutipleView import MultipleView
from View_Window import ViewWindow
from View_AutoPanorama import AutoPanorama
from View_RecenterImage import RecenterImage
from VIew_Rotate import Rotate
from Help import Win_Help
from PyQt5 import QtWidgets
from OpenCamera import OpenCameras


class Controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Controller, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_event()
        self.image = None
        self.OriginalimageAnypoint = None
        self.anypoint_Image = None
        self.panorama_Image = None
        self.image_1 = None
        self.image_2 = None
        self.img_file_path_l = None
        self.img_file_path_r = None
        self.img_result_1 = None
        self.img_result_2 = None
        self.angle = 0
        self.alpha = 0
        self.beta = 0
        self.zoom = 4
        self.multiView = False
        self.annot_image = None
        self.revImage = None

        self.img_result = None
        self.width_img = 1400
        self.anypointState = 0
        self.ratio = 0
        self.oriImage = None
        self.resultImage = None
        self.morphImage = None
        self.cam = False
        self.coor = None
        self.cap = None

        self.displayW = None

        self.maximizedMultiWindow = False
        self.record = False
        self.maxi = False

        self.videoControl = Video_Controler(self)
        self.videoControl.videoButtonDisable()

        self.application = Application(self)
        self.application.applicationMoildevs()

        self.autoPano = AutoPanorama(self)
        self.recenter = RecenterImage(self)

        self.panorama = Panorama(self)

        self.fast = FastView(self)
        self.multi = MultipleView(self)
        self.view = ViewWindow(self)
        self.rotate = Rotate(self)

        self.anypoint = AnyPoint(self)

        self.dialogHelp = QtWidgets.QDialog()
        self.winHelp = Win_Help(self, self.dialogHelp)

        self.dialogOpenCam = QtWidgets.QDialog()
        self.winOpenCam = OpenCameras(self, self.dialogOpenCam)

    def connect_event(self):
        """
        connect the signal from the activity to function will execute.
        """
        self.ui.actionLoad_video.triggered.connect(self.open_video_file)
        self.ui.actionLoad_Image.triggered.connect(self.openImage)
        self.ui.actionOpen_Cam.triggered.connect(self.onclick_open_camera)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionAbout_Us.triggered.connect(self.aboutUs)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionSave_Image.triggered.connect(self.saveImage)
        self.ui.windowOri.mousePressEvent = self.mouse_event
        self.ui.windowOri.mouseMoveEvent = self.mouseMovedOriImage
        self.ui.windowOri.mouseReleaseEvent = self.mouse_ori_release_event
        self.ui.PlussIcon.mouseReleaseEvent = self.mouse_result_release_event
        self.ui.PlussIcon.mouseDoubleClickEvent = self.mouseDoubleclic_event
        self.ui.PlussIcon.wheelEvent = self.wheelEvent_result
        self.ui.gridFrame.mouseReleaseEvent = self.releaseMouseEvent
        # self.ui.windowOri.mouseReleaseEvent = self.mouse_release_event

        # self.ui.window_LT.mousePressEvent = self.onclickWindow_LT
        # self.ui.window_T.mousePressEvent = self.onclickWindow_T
        # self.ui.window_RT.mousePressEvent = self.onclickWindow_RT
        # self.ui.window_L.mousePressEvent = self.onclickWindow_L
        # self.ui.window_Center.mousePressEvent = self.onclickWindow_Center
        # self.ui.window_R.mousePressEvent = self.onclickWindow_R
        # self.ui.window_LB.mousePressEvent = self.onclickWindow_LB
        # self.ui.window_B.mousePressEvent = self.onclickWindow_B
        # self.ui.window_RB.mousePressEvent = self.onclickWindow_RB

        # self.ui.pushButtonPanorama.clicked.connect(self.set_pano)


        # self.ui.checkBox_ShowRecenterImage_2.clicked.connect(self.showRecenter)
        # self.ui.checkPanoramaAuto.clicked.connect(self.autoMode)

        # self.ui.spinBox_zoom.valueChanged.connect(self.zoomValue)

        # self.ui.checkBox_CenterLumen.clicked.connect(self.centerLumen)
        # self.ui.CheckFaceDetect.clicked.connect(self.onclickFaceDetect)

        self.ui.pushButton.clicked.connect(self.reset)
        # self.ui.actionCar_Safety_system.triggered.connect(self.appsCarsafety)
        # self.ui.actiontube_inspection.triggered.connect(self.appsTubeInspection)
        self.ui.recordBtn.clicked.connect(self.recordVideo)
        # self.ui.actionMaximized.triggered.connect(self.show_Maximized)
        # self.ui.actionMinimized.triggered.connect(self.show_Minimized)
        # self.ui.pushButton_2.clicked.connect(self.multipleView)

    def init_parameter(self):
        """
        create initial parameter
        """
        self.camera = self.config.get_cameraName()
        self.sensor_width = self.config.get_sensorWidth()
        self.sensor_height = self.config.get_sensor_height()
        self.Icx = self.config.get_Icx()
        self.Icy = self.config.get_Icy()
        self.ratio = self.config.get_ratio()
        self.imageWidth = self.config.get_imageWidth()
        self.imageHeight = self.config.get_imageHeight()
        self.calibrationRatio = self.config.get_calibrationRatio()
        self.parameter0 = self.config.get_parameter0()
        self.parameter1 = self.config.get_parameter1()
        self.parameter2 = self.config.get_parameter2()
        self.parameter3 = self.config.get_parameter3()
        self.parameter4 = self.config.get_parameter4()
        self.parameter5 = self.config.get_parameter5()
        self.coorX = self.Icx
        self.coorY = self.Icy

    def init_Map(self):
        self.ui.lineEdit_Icx.setText(str(self.Icx))
        self.ui.lineEdit_Icy.setText(str(self.Icy))
        self.cx = int(self.ui.lineEdit_Icx.text())
        self.cy = int(self.ui.lineEdit_Icy.text())
        self.m_ratio = self.ratio
        self.mapX = np.zeros((self.imageHeight, self.imageWidth), dtype=np.float32)
        self.mapY = np.zeros((self.imageHeight, self.imageWidth), dtype=np.float32)
        size = self.imageHeight, self.imageWidth, 3
        self.res = np.zeros(size, dtype=np.uint8)

    def importMoildev(self):
        """
        import moildev library
        """
        self.init_parameter()
        self.moildev = Moildev(self.camera, self.sensor_width, self.sensor_height, self.Icx, self.Icy, self.ratio,
                               self.imageWidth, self.imageHeight, self.parameter0, self.parameter1, self.parameter2,
                               self.parameter3, self.parameter4, self.parameter5, self.calibrationRatio)
        # self.ui.camera_name.setText(str(self.camera))

    # open source media
    def openImage(self):
        """
        thi function for open image will use for the apps
        """
        if self.ui.comboBox.currentIndex() == 7:
            # this image will open and select two image for 3D measuement
            QtWidgets.QMessageBox.information(self, "Information", "Select Source Image\nL -> R")
            # self.ui.status_label.setText("select the image !!")
            self.img_file_path_l = select_file("Select Image", "../SourceImage", "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
            # self.ui.status_label.setText("Find the corner on the object !!")
            if self.img_file_path_l:
                self.ui.statusMessage.setText("Corner Detection Process !!")
                self.img_file_path_r = select_file("Select Image", "../SourceImage", "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
                if self.img_file_path_r:
                    self.image_1 = read_image(self.img_file_path_l)
                    # self.h, self.w = self.image_1.shape[:2]
                    self.image_2 = read_image(self.img_file_path_r)
                    self.img_result_1, self.img_result_2 = self.ratio3D_Measurement(self.image_1, self.image_2)
                    self.application.applicationMoildevs()
                    QtWidgets.QMessageBox.information(self, "Information", "Ready to go !!")

        else:
            QtWidgets.QMessageBox.information(self, "Information", "Select Source Image then select\nThe parameter of "
                                                                   "the image")
            self.filename = select_file("Select Image", "../SourceImage", "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
            if self.filename:
                file_name = select_file("Select Parameter", "../Moil_Parameter", "Parameter Files (*.json)")
                if file_name:
                    # print(file_name)
                    self.videoControl.stop_camera()
                    self.ui.checkAnypoint.setChecked(False)
                    self.ui.checkPanorama.setChecked(False)
                    if self.multiView:
                        self.multipleView()
                    self.config = Config(file_name)
                    self.moildev = Moildev(file_name)
                    # self.importMoildev()
                    self.image = read_image(self.filename)
                    self.h, self.w = self.image.shape[:2]
                    self.imageWidth, self.imageHeight = self.w, self.h
                    self.videoControl.videoButtonDisable()
                    # self.init_Map()
                    self.application.applicationMoildevs()
                    self.ratio_x, self.ratio_y, self.center = self.init_ori_ratio(self.image)
                    self.cam = False
                    self.anypoint.resetAlphaBeta()

    def open_video_file(self):
        """ load video frame """
        QtWidgets.QMessageBox.information(self, "Information", "Select Source Video then select\nThe parameter of "
                                                               "the image")
        videoFile = select_file("Select Image", "../Source_Video", "Image Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if videoFile:
            paramName = select_file("Select Parameter", "../Moil_Parameter", "Parameter Files (*.json)")
            if paramName:
                if self.multiView:
                    self.multipleView()
                self.anypoint.resetAlphaBeta()
                self.videoControl.videoButtonEnable()
                self.coor = None
                self.config = Config(paramName)
                self.importMoildev()
                self.init_Map()
                if self.cap:
                    self.cap = cv2.VideoCapture(videoFile)
                    self.fps = self.cap.get(cv2.CAP_PROP_FPS)
                    self.cam = True
                    self.next_frame_slot()
                else:
                    self.cap = cv2.VideoCapture(videoFile)
                    self.fps = self.cap.get(cv2.CAP_PROP_FPS)
                    self.cam = True
                    self.next_frame_slot()

    def onclick_open_camera(self):
        self.dialogOpenCam.show()

    def cameraOpen(self):
        self.videoStreamURL = self.winOpenCam.vidUrl()
        if self.videoStreamURL is None:
            pass
        else:
            self.cap = cv2.VideoCapture(self.videoStreamURL)
            self.coor = None
            if self.cap.isOpened is False:
                QtWidgets.QMessageBox.information(self, "Information", "No server camera founded")
            else:
                QtWidgets.QMessageBox.information(self, "Information", "Select Parameter Camera !!")
                file_name = select_file("Select Left Parameter", "../Moil_Parameter", "Parameter Files (*.json)")
                if file_name == "":
                    self.cap = None
                else:
                    if self.multiView:
                        self.multipleView()
                    self.config = Config(file_name)
                    self.importMoildev()
                    self.videoControl.videoButtonCamera()
                    self.ret, self.image = self.cap.read()
                    if self.image is None:
                        QtWidgets.QMessageBox.information(self, "Information", "No server camera founded")
                    else:
                        self.init_Map()
                        self.application.setupCameraCenter.set_center()
                        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
                        self.cam = True
                        self.next_frame_slot()

    def next_frame_slot(self):
        self.ret, self.image = self.cap.read()
        if self.image is None:
            pass
        else:
            self.oriImage = self.image.copy()
            self.h, self.w = self.image.shape[:2]
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.pos_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.pos_msec = self.cap.get(cv2.CAP_PROP_POS_MSEC)
            self.frame_count = float(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration_sec = int(self.frame_count / self.fps)
            self.minutes = duration_sec // 60
            duration_sec %= 60
            self.seconds = duration_sec
            sec_pos = int(self.pos_frame / self.fps)
            self.minute = int(sec_pos // 60)
            sec_pos %= 60
            self.sec = sec_pos
            self.videoControl.controler()
            self.ratio_x, self.ratio_y, self.center = self.init_ori_ratio(self.image)
            self.application.applicationMoildevs()
            # if self.ui.checkAnypoint.isChecked():
            #     if self.multiView:
            #         if self.maxi:
            #             if self.maximizedMultiWindow:
            #                 if self.displayW == 1:
            #                     MutipleView.Window_LT_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 2:
            #                     MutipleView.Window_T_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 3:
            #                     MutipleView.Window_RT_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 4:
            #                     MutipleView.Window_L_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 5:
            #                     MutipleView.Window_center_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 6:
            #                     MutipleView.Window_R_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 7:
            #                     MutipleView.Window_LB_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 8:
            #                     MutipleView.Window_B_Maxi(self, self.image, 1800)
            #                 elif self.displayW == 9:
            #                     MutipleView.Window_RB_Maxi(self, self.image, 1800)
            #                 else:
            #                     pass
            #             else:
            #                 MutipleView.multiView(self, self.image, 640)
            #         else:
            #             if self.maximizedMultiWindow:
            #                 if self.displayW == 1:
            #                     MutipleView.Window_LT_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 2:
            #                     MutipleView.Window_T_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 3:
            #                     MutipleView.Window_RT_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 4:
            #                     MutipleView.Window_L_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 5:
            #                     MutipleView.Window_center_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 6:
            #                     MutipleView.Window_R_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 7:
            #                     MutipleView.Window_LB_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 8:
            #                     MutipleView.Window_B_Maxi(self, self.image, 1300)
            #                 elif self.displayW == 9:
            #                     MutipleView.Window_RB_Maxi(self, self.image, 1300)
            #                 else:
            #                     pass
            #             else:
            #                 MutipleView.multiView(self, self.image, 400)
            #     else:
            #         self.ui.PlussIcon.show()
            #         self.oriImage = View_Anypoint.drawPolygon(self.oriImage, self.mapX, self.mapY)
            #         self.showResult.showFrame(self.image)
            #
            # elif self.ui.checkBox_CenterLumen.isChecked():
            #     self.centerLumen()
            # elif self.ui.checkPanoramaAuto.isChecked():
            #     self.autoMode()
            # # elif self.ui.checkBox_ObjectDetection.isChecked():
            # #     self.morp_image()
            # elif self.ui.CheckFaceDetect.isChecked():
            #     self.onclickFaceDetect()
            # else:
            #     self.oriImage = self.oriImage
            #     self.showResult.showFrame(self.image)
                # if self.record:
                #     self.video_writer.write(self.oriImage)

    def mouse_event(self, e):
        if self.image is None:
            pass
        else:
            if e.button() == QtCore.Qt.LeftButton:
                # print(self.oriImage.shape[:2])
                self.currPos = e.pos()
                self.pos_x = round(e.x())
                self.pos_y = round(e.y())
                delta_x = round(self.pos_x * self.ratio_x - self.imageWidth * 0.5)
                delta_y = round(- (self.pos_y * self.ratio_y - self.imageHeight * 0.5))
                # print(self.pos_x, self.pos_y)
                # print(self.ratio_x, self.ratio_y)
                self.coor = (round(self.pos_x * self.ratio_x), round(self.pos_y * self.ratio_y))
                self.coorX = round(self.pos_x * self.ratio_x)
                self.coorY = round(self.pos_y * self.ratio_y)
                if self.ui.checkAnypoint.isChecked():
                    self.alpha, self.beta = self.config.get_alpha_beta(self.anypointState, delta_x, delta_y)
                    # print(self.alpha, self.beta)
                    self.anypoint.anypoint_view()
                elif self.ui.checkBox_ShowRecenterImage_2.isChecked():
                    self.alpha, self.beta = self.config.get_alpha_beta(0, delta_x, delta_y)
                    self.recenter.recenterImage()
                else:
                    print("coming soon")

    def mouseDoubleclic_event(self, e):
        self.anypoint.resetAlphaBeta()
        if self.ui.checkAnypoint.isChecked():
            self.anypoint.anypoint_view()
        elif self.ui.checkPanorama.isChecked():
            self.panorama.panorama_view()
        else:
            pass

    def wheelEvent_result(self, e):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ControlModifier:
            wheelcounter = e.angleDelta()
            if wheelcounter.y() / 120 == -1:
                if self.width_img == 1100:
                    pass
                else:
                    self.width_img -= 100
                self.application.applicationMoildevs()
            if wheelcounter.y() / 120 == 1:
                if self.width_img == 4000:
                    pass
                else:
                    self.width_img += 100
                self.application.applicationMoildevs()

    def releaseMouseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            pass
        else:
            menu = QtWidgets.QMenu()
            maxi = menu.addAction("Fullscreen")
            maxi.triggered.connect(self.show_Maximized)
            mini = menu.addAction("Minimized")
            mini.triggered.connect(self.show_Minimized)
            menu.exec_(e.globalPos())

    def mouseMovedOriImage(self, e):
        self.currPos = e.pos()
        self.pos_x = round(e.x())
        self.pos_y = round(e.y())
        delta_x = round(self.pos_x * self.ratio_x - self.imageWidth * 0.5)
        delta_y = round(- (self.pos_y * self.ratio_y - self.imageHeight * 0.5))
        self.coor = (round(self.pos_x * self.ratio_x), round(self.pos_y * self.ratio_y))
        self.coorX = round(self.pos_x * self.ratio_x)
        self.coorY = round(self.pos_y * self.ratio_y)
        if self.ui.checkAnypoint.isChecked():
            self.alpha, self.beta = self.config.get_alpha_beta(self.anypointState, delta_x, delta_y)
            self.anypoint.anypoint_view()

    def mouse_ori_release_event(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            pass
        else:
            if self.image is None:
                pass
            else:
                self.menuMouseEvent(e)

    def mouse_result_release_event(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            pass
        else:
            if self.image is None:
                pass
            else:
                self.menuMouseEvent(e)

    def menuMouseEvent(self, e):
        menu = QtWidgets.QMenu()
        maxi = menu.addAction("Show Maximized")
        maxi.triggered.connect(self.view.show_Maximized)
        mini = menu.addAction("Show Minimized")
        mini.triggered.connect(self.view.show_Minimized)
        save = menu.addAction("Save Image")
        info = menu.addAction("Show Info")
        save.triggered.connect(self.saveImage)
        info.triggered.connect(self.info)
        menu.exec_(e.globalPos())

    def info(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n\nContact: "
            "M07158031@0365.mcut.edu.tw")
        msgbox.setIconPixmap(QtGui.QPixmap('./assets/chess.jpg'))
        msgbox.exec()

    def saveImage(self):
        """
        save image, please write the name image on string
        """
        if self.image is None:
            pass
        else:
            self.ui.frameSaveImage.show()
            name_image = "Original"
            image = self.image
            if self.ui.checkPanorama.isChecked() or self.ui.checkAnypoint.isChecked():
                name_image = "result"
                image = self.resultImage

            self.snapshot_label = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
            image_ = self.ratioImage(image, 240)
            imagePixmap = QtGui.QImage(image_.data, image_.shape[1], image_.shape[0],
                                       QtGui.QImage.Format_RGB888).rgbSwapped()
            self.snapshot_label.setPixmap(QtGui.QPixmap.fromImage(imagePixmap))
            self.addWidget()
            saveImage(name_image, image)

    def addWidget(self):
        """ take snapshot"""
        self.snapshot_label.setStyleSheet("border-width:1px;\n"
                                          "border: 1px solid black;")
        self.snapshot_label.setFixedSize(240, 180)
        self.ui.verticalLayout_7.addWidget(self.snapshot_label)

    def ratioImage(self, imageOri, widthSize):
        h, w = imageOri.shape[:2]
        r = widthSize / float(w)
        hi = round(h * r)
        img_ori = cv2.resize(imageOri, (widthSize, hi), interpolation=cv2.INTER_AREA)
        return img_ori

    ##################################################
    # video controller
    ##################################################
    def recordVideo(self):
        if self.record is False:
            self.ui.recordBtn.setIcon(QtGui.QIcon("assets/rec.jpg"))
            self.ui.recordBtn.setIconSize(QtCore.QSize(30, 20))
            print("record")
            ss = datetime.datetime.now().strftime("%H_%M_%S")
            frame_width = int(self.cap.get(3))
            frame_height = int(self.cap.get(4))
            filename = "Original"
            if self.ui.checkPanorama.isChecked() or self.ui.checkAnypoint.isChecked():
                filename = "result"
            self.name = "../result/Video/" + filename + "_" + str(ss) + ".avi"
            self.timer.stop()
            QtWidgets.QMessageBox.information(self, "Information", " Start Record Video !!")
            self.timer.start()
            self.video_writer = cv2.VideoWriter(self.name, cv2.VideoWriter_fourcc(*'XVID'), 30,
                                                (frame_width, frame_height))
            os.makedirs(os.path.dirname(self.name), exist_ok=True)
            self.record = True
        #
        else:
            self.ui.recordBtn.setIcon(QtGui.QIcon("assets/rec.png"))
            self.ui.recordBtn.setIconSize(QtCore.QSize(20, 18))
            print("finish record")
            self.video_writer.release()
            self.timer.stop()
            QtWidgets.QMessageBox.information(self, "Information", "Video saved !!")
            self.timer.start()
            self.record = False

    def reset(self):
        self.anypoint.resetAlphaBeta()
        if self.ui.checkAnypoint.isChecked():
            self.anypoint.anypoint_view()
        else:
            pass

    # def multipleView(self):
    #     if self.multiView:
    #         MutipleView.controlFrameHide(self)
    #         self.ui.pushButton_2.setStyleSheet('background-color: rgb(238, 238, 236);')
    #         self.ui.pushButton_2.setText("Multiple View")
    #         self.ui.PlussIcon.show()
    #         ShowResult.showFrame(self)
    #         self.multiView = False
    #         # print("multi")
    #     else:
    #         MutipleView.controlFrameShow(self)
    #         MutipleView.multiView(self, self.image, 400)
    #         self.ui.pushButton_2.setStyleSheet("background-color: rgb(115, 210, 22);")
    #         self.ui.pushButton_2.setText("Single View")
    #         self.multiView = True
    #         # print("single")

    def ratio3D_Measurement(self, image_1, image_2, width=600):
        h, w = image_1.shape[:2]
        r = width / float(w)
        hi = round(h * r)
        self.ui.label3Dimage1.setMaximumSize(QtCore.QSize(width, hi))
        self.ui.label3Dimage2.setMaximumSize(QtCore.QSize(width, hi))
        img_result_1 = cv2.resize(image_1, (width, hi), interpolation=cv2.INTER_AREA)
        img_result_2 = cv2.resize(image_2, (width, hi), interpolation=cv2.INTER_AREA)
        return img_result_1, img_result_2

    def init_ori_ratio(self, image):
        """
        calculate the ratio of original Image
        """
        h = self.ui.windowOri.height()
        w = self.ui.windowOri.width()
        height, width = image.shape[:2]
        ratio_x = width / w
        ratio_y = height / h
        center = (round((w / 2) * ratio_x), round((h / 2) * ratio_y))
        return ratio_x, ratio_y, center

    def aboutUs(self):
        """
        About us information
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n\nContact: "
            "M07158031@0365.mcut.edu.tw")
        msgbox.setIconPixmap(QtGui.QPixmap('./assets/chess.jpg'))
        msgbox.exec()

    def help(self):
        self.dialogHelp.show()

    def exit(self):
        if self.cam:
            self.videoControl.stop_camera()
        self.close()
