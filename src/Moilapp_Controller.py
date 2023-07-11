#########################################################################
#   MoilApp (Applications for sophisticated fisheye image processing)   #
#   Written by Haryanto (haryanto@o3635.mcut.edu.tw)                    #
#   Based on Moil-Lab (Ming Chi University of Technology)               #
#########################################################################
import os
import cv2
import datetime
import webbrowser
import numpy as np
from help import Help
from moilutils import ResourceIcon
from functools import partial
from PyQt5 import QtWidgets, QtGui, QtCore
from moilutils import MoilUtils
from plugin_controller import PluginController
from Ui_Moilapp import Ui_MainWindow
from panorama import Panorama
from anypoint import Anypoint
from reCenter import RecenterImage
from control_view import ManipulateView
from event_controller import MouseEvent
from moilutils import VideoController


class Controller(Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self, parent):
        """

        Args:
            parent ():
        """
        super().__init__(parent)
        self.comboBox_cam_type = None
        self.parent = parent
        self.setupUi(self.parent)
        self.rs = ResourceIcon()
        self.open_plugin = False
        self.image = None
        self.cap = None
        self.cam = False
        self.record = False
        self.video_writer = None
        self.videoDir = None
        self.moildev = None
        self.recImage = None
        self.normal_view = True
        self.panorama_view = False
        self.anypoint_view = False
        self.axis_controller = False
        self.dir_save = None
        self.posVid = []
        self.mapX = None
        self.mapY = None
        self.mapX_pano = None
        self.mapY_pano = None
        self.zoom_area = False
        self.type_camera = None
        self.num = 0
        self.pos_x = 0
        self.w = 0
        self.h = 0
        self.point = None
        self.result_image = None
        self.easySpin = False
        self.width_original_image = 300
        self.width_result_image = 1080
        self.angle = 0

        self.dialogHelp = QtWidgets.QDialog()
        self.winHelp = Help(self, self.dialogHelp)

        self.video_controller = VideoController(self)
        self.panorama = Panorama(self)
        self.anypoint = Anypoint(self)
        self.recenter = RecenterImage(self)
        self.control_mouse = MouseEvent(self)
        self.manipulate = ManipulateView(self)

        self.frameVideoController.hide()
        self.frame_panorama.hide()
        self.frame_navigator.hide()
        self.buttonBack.hide()
        self.buttonRecenter.hide()
        self.labelrecenterTitle.hide()
        self.frameRecenter.hide()
        self.control_plugin = PluginController(self)
        self.connect_event()

    def connect_event(self):
        """
        Connect every event on user interface like button event, mouse event
        and etc to the function processing.

        """
        self.parent.closeEvent = self.closeEvent
        self.parent.resizeEvent = self.resizeEvent

        # action from menubar menu file
        self.actionLoad_Image.triggered.connect(self.open_image)
        self.actionLoad_Video.triggered.connect(self.onclick_load_video)
        self.actionOpen_Cam.triggered.connect(self.open_camera)
        self.actionCamera_Parameters.triggered.connect(MoilUtils.parametersForm)
        self.actionRecord_video.triggered.connect(self.actionRecordVideo)
        self.actionSave_Image.triggered.connect(self.save_image)
        self.actionExit.triggered.connect(self.onclick_exit)

        # action from menubar menu view
        self.actionRotateLeft.triggered.connect(self.manipulate.rotate_left)
        self.actionRotateRight.triggered.connect(self.manipulate.rotate_right)
        self.actionZoomIn.triggered.connect(self.manipulate.zoom_in)
        self.actionZoomOut.triggered.connect(self.manipulate.zoom_out)

        # action from menubar menu Window
        self.actionMaximize.triggered.connect(self.maximize_view)
        self.actionMinimize.triggered.connect(self.minimize_view)

        # action from menubar menu apps
        self.actionHelpPlugins.triggered.connect(self.winHelp.help_plugin)

        # action from menubar menu help
        self.actionAbout_Apps.triggered.connect(self.onclick_help_moil)
        self.actionAbout_Us.triggered.connect(self.winHelp.about_us)
        self.action_accessibility.triggered.connect(self.onclick_accessibility)
        self.actionReleaseNote.triggered.connect(self.onclickReleaseNote)
        self.actionCheckUpdate.triggered.connect(self.checkUpdate)

        # ++++++ Normal view ++++++
        self.btn_normal.clicked.connect(self.onclick_view_normal)

        # +++++ anypoint View +++++
        self.btn_anypoint.clicked.connect(self.anypoint.process_to_anypoint)
        self.btn_Up_View.clicked.connect(self.anypoint.up)
        self.btn_Right_view.clicked.connect(self.anypoint.right)
        self.btn_left_view.clicked.connect(self.anypoint.left)
        self.btn_center_view.clicked.connect(self.anypoint.center)
        self.btn_Down_view.clicked.connect(self.anypoint.down)
        self.radio_btn_mode_1.clicked.connect(self.anypoint.anypoint_mode_1)
        self.radio_btn_mode_2.clicked.connect(self.anypoint.anypoint_mode_2)
        self.lineedit_alpha_2.editingFinished.connect(self.anypoint.set_param_any)
        self.lineedit_beta_2.editingFinished.connect(self.anypoint.set_param_any)
        self.anypoint_zoom_2.editingFinished.connect(self.anypoint.set_param_any)

        # +++++ panorama View +++++
        self.btn_panorama.clicked.connect(self.panorama.process_to_panorama)
        self.max_pano.valueChanged.connect(self.panorama.change_panorama_fov)
        self.min_pano.valueChanged.connect(self.panorama.change_panorama_fov)

        # +++ recenter view ++++
        self.buttonRecenter.clicked.connect(self.onclickRecenter)
        self.setIcx.valueChanged.connect(self.recenter.positionCoorX)
        self.setIcy.valueChanged.connect(self.recenter.positionCoorY)

        # connect button to function
        self.btn_Open_Image.clicked.connect(self.open_image)
        self.btn_Open_Video.clicked.connect(self.onclick_load_video)
        self.btn_Open_Cam.clicked.connect(self.open_camera)
        self.btn_Save_Image.clicked.connect(self.save_image)

        # media player controller
        self.btn_Record_video.clicked.connect(self.buttonRecordVideo)
        self.btn_play_pouse.clicked.connect(partial(self.video_controller.playPauseVideo, self.btn_play_pouse))
        self.btn_stop_video.clicked.connect(self.video_controller.stopVideo)
        self.btn_prev_video.clicked.connect(self.video_controller.rewindVideo)
        self.btn_skip_video.clicked.connect(self.video_controller.forwardVideo)
        self.slider_Video.valueChanged.connect(self.video_controller.sliderController)

        # control view
        self.btn_Rotate_Left.clicked.connect(self.manipulate.rotate_left)
        self.btn_Rotate_Right.clicked.connect(self.manipulate.rotate_right)
        self.btn_Zoom_in.clicked.connect(self.manipulate.zoom_in)
        self.btn_Zoom_out.clicked.connect(self.manipulate.zoom_out)

        # mouse event controller
        self.label_Original_Image.mouseDoubleClickEvent = self.control_mouse.mouseDoubleclick_event
        self.label_Result_Image.mouseDoubleClickEvent = self.control_mouse.mouseDoubleclick_event
        self.label_Original_Image.mousePressEvent = self.control_mouse.mouse_event
        self.label_Result_Image.mousePressEvent = self.control_mouse.mouse_result_press
        self.label_Original_Image.wheelEvent = self.control_mouse.mouse_wheelEvent_ori_label
        self.label_Result_Image.wheelEvent = self.control_mouse.mouse_wheelEvent
        self.label_Result_Image.mouseReleaseEvent = self.control_mouse.mouse_release_event
        self.label_Original_Image.mouseMoveEvent = self.control_mouse.mouseMovedOriImage
        self.label_Result_Image.mouseMoveEvent = self.control_mouse.mouseMoveEvent

        # others
        self.btnAboutUs.clicked.connect(self.winHelp.about_us)
        self.btnHelpMoil.clicked.connect(self.onclick_help_moil)
        self.btn_clear.clicked.connect(self.onclick_clear)
        self.listWidget.currentItemChanged.connect(self.saved_image_activated)
        self.comboBox_zoom.activated.connect(self.combo_percentage_zoom)
        self.button_menu.clicked.connect(self.control_frame_view_button)
        self.buttonBack.clicked.connect(self.showToWindow)

    def onclick_clear(self):
        if self.cam:
            self.video_controller.stopVideo()
            self.cap.release()
            self.frameVideoController.hide()
        self.label_Result_Image.clear()
        self.label_Result_Image.setMaximumSize(QtCore.QSize(1080, 810))
        self.label_Result_Image.setMinimumSize(QtCore.QSize(1080, 810))
        self.label_Original_Image.setMinimumSize(QtCore.QSize(266, 200))
        self.label_Original_Image.clear()
        self.reset_mode_view()
        self.comboBox_zoom.removeItem(8)
        self.comboBox_zoom.setCurrentIndex(0)
        self.label_Application.setText("MoilApp")
        self.parent.setWindowTitle("MoilApp")
        self.buttonBack.hide()
        self.frameRecenter.hide()
        self.buttonRecenter.hide()
        self.image = None
        self.recImage = None

    def open_image(self):
        """
        Open Dialog to search the file image from directory. This function also will read the comment from
        metadata image.

        """
        filename = MoilUtils.selectFile(self.parent, "Image Files",
                                        "../SourceImage", "(*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            self.reset_mode_view()
            if self.cam:
                self.video_controller.stopVideo()
                self.cap.release()
                self.frameVideoController.hide()
            typeCam = MoilUtils.read_camera_type(filename)
            if typeCam == "" or typeCam == None:
                self.type_camera = MoilUtils.selectCameraType()
                MoilUtils.write_camera_type(filename, self.type_camera)
            else:
                self.type_camera = typeCam

            if self.type_camera is not None:
                self.updateLabel(filename)
                self.image = MoilUtils.readImage(filename)
                self.h, self.w = self.image.shape[:2]
                self.moildev = MoilUtils.connectToMoildev(self.type_camera)

                self.buttonRecenter.setChecked(False)
                self.buttonRecenter.setStyleSheet(
                    "QPushButton{\n"
                    "  border-color: #71D1BA;\n"
                    "  border-width: 2px;        \n"
                    "  border-style: solid;\n"
                    "  border-radius: 5px;\n"
                    "  background-color : rgb(238, 238, 236); }\n")
                self.showToWindow()
                self.cam = False

    def onclick_load_video(self):
        """
        Open Dialog to search video file from Directory. after you select the video file, it will show the prompt
        to select the type of camera.

        """
        video_source = MoilUtils.selectFile(self.parent,
                                            "Select Video Files",
                                            "../",
                                            "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            self.reset_mode_view()
            self.type_camera = MoilUtils.selectCameraType()
            self.easySpin = False
            if self.type_camera is not None:
                self.updateLabel(video_source)
                self.running_video(video_source)

    def open_camera(self):
        """
        open the camera from the available source in the system,
        this function provide 2 source namely USB cam and Streaming cam from Raspberry pi.
        """
        self.reset_mode_view()
        camera_source = MoilUtils.selectCameraSource()
        if camera_source is not None:
            self.type_camera = MoilUtils.selectCameraType()
            if self.type_camera is not None:
                self.updateLabel()
                if self.type_camera == "narl_fisheye":
                    self.easySpin = True
                    self.running_video(camera_source, True)
                else:
                    self.running_video(camera_source)
                    self.easySpin = False

    def running_video(self, video_source, easySpin = False):
        """
        Open Video following the source given.

        Args:
            video_source (): the source of media, can be camera and video file.

        """
        self.frameVideoController.show()
        if easySpin:
            try:
                import EasyPySpin
                self.cap = EasyPySpin.VideoCapture(video_source)
                self.cap.set(cv2.CAP_PROP_EXPOSURE, -1)  # -1 sets exposure_time to auto
                self.cap.set(cv2.CAP_PROP_GAIN, -1)  # -1 sets gain to auto
                print('\nModule was installed')
            except ImportError:
                print('\nThere was no such module installed')
                QtWidgets.QMessageBox.warning(None, "Warning !!", "The Module was not Installed. \n\n"
                                                                  "Please install the library following \n"
                                                                  "the document provided.")
        else:
            self.cap = cv2.VideoCapture(video_source)
            if self.type_camera == "leo_fisheye":
                self.cap.set(3, 1920)
                self.cap.set(4, 1080)

        success, self.image = self.cap.read()
        if success:
            self.h, self.w = self.image.shape[:2]
            self.moildev = MoilUtils.connectToMoildev(self.type_camera)
            self.cam = True
            self.buttonRecenter.setChecked(False)
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(238, 238, 236); }\n")
            self.video_controller.nextFrame()
        else:
            QtWidgets.QMessageBox.information(self.parent, "Information", "No source camera founded !!!")

    def onclick_view_normal(self):
        """
        Showing the original image into Label frame in UI.

        """
        if self.image is not None:
            self.buttonRecenter.setChecked(False)
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(238, 238, 236); }\n")
            self.reset_mode_view()
            self.normal_view = True
            self.panorama_view = False
            self.anypoint_view = False
            self.angle = 0
            self.showToWindow()
            self.frame_navigator.hide()
            self.frame_panorama.hide()
            self.show_percentage()
            self.status_alpha.setText("Alpha: 0")
            self.status_beta.setText("Beta: 0")

    def showToWindow(self):
        """
        Showing the processing result image into the frame UI.

        """
        # _, img = self.cap.read()
        # if not _:
        #     QtWidgets.QMessageBox.information(None, "Test", "Finishhhh")
        self.zoom_area = False
        self.buttonBack.hide()
        radius = 6 if self.h < 800 else 10
        if self.normal_view:
            self.frameRecenter.hide()
            self.labelrecenterTitle.hide()
            self.buttonRecenter.show()
            if self.buttonRecenter.isChecked():
                self.labelMin.hide()
                self.labelMax.hide()
                self.min_pano.hide()
                self.max_pano.hide()
                self.labelIcx.show()
                self.labelIcy.show()
                self.setIcx.show()
                self.setIcy.show()
                self.recImage = self.recenter.returnImage()
                resImage = self.recImage
                self.frame_panorama.setGeometry(QtCore.QRect(5, 50, 180, 80))
            else:
                resImage = self.image
                self.point = (round(self.moildev.icx()), round(self.moildev.icy()))
                self.frame_panorama.hide()
            image = MoilUtils.drawPoint(self.image.copy(), self.point, radius)
            MoilUtils.showImageToLabel(self.label_Original_Image,
                                       image,
                                       self.width_original_image)
            MoilUtils.showImageToLabel(self.label_Result_Image,
                                       resImage,
                                       self.width_result_image, self.angle, plusIcon=True)

        elif self.panorama_view:
            self.buttonRecenter.show()
            mapX = np.load(
                    './maps_pano/mapX.npy')
            mapY = np.load(
                    './maps_pano/mapY.npy')
            # rho = self.panorama.rho
            if self.buttonRecenter.isChecked():
                self.frameRecenter.show()
                self.labelrecenterTitle.show()
                self.labelIcx.show()
                self.labelIcy.show()
                self.setIcx.show()
                self.setIcy.show()
                self.labelMin.show()
                self.labelMax.show()
                self.min_pano.show()
                self.max_pano.show()
                self.frame_panorama.setGeometry(QtCore.QRect(5, 50, 180, 145))
                self.recImage = self.recenter.returnImage()
                resImage = self.recImage
                # res = MoilUtils.drawPolygon(resImage.copy(), mapX, mapY)
                MoilUtils.showImageToLabel(self.labelRecenter,
                                           resImage,
                                           self.width_original_image, plusIcon=True)
                image = MoilUtils.drawPoint(self.image.copy(), self.point, radius)
                MoilUtils.showImageToLabel(self.label_Original_Image,
                                           image,
                                           self.width_original_image)
            else:
                self.frameRecenter.hide()
                self.labelrecenterTitle.hide()
                self.labelIcx.hide()
                self.labelIcy.hide()
                self.setIcx.hide()
                self.setIcy.hide()
                self.labelMin.show()
                self.labelMax.show()
                self.min_pano.show()
                self.max_pano.show()
                self.frame_panorama.setGeometry(QtCore.QRect(5, 50, 180, 80))
                resImage = self.image.copy()
                self.point = (round(self.moildev.icx()), round(self.moildev.icy()))

                # self.result_image = self.result_image[round(rho):self.h, 0:self.w]
                # print(self.result_image)
                # image = MoilUtils.drawPolygon(self.image.copy(), mapX, mapY)
                image = MoilUtils.drawPoint(self.image.copy(), self.point, radius)
                MoilUtils.showImageToLabel(self.label_Original_Image,
                                           image,
                                           self.width_original_image)
            self.result_image = MoilUtils.remap(resImage, mapX, mapY)
            MoilUtils.showImageToLabel(self.label_Result_Image,
                                       self.result_image,
                                       self.width_result_image, self.angle)

        else:
            self.buttonRecenter.hide()
            self.frameRecenter.hide()
            self.labelrecenterTitle.hide()
            image = MoilUtils.drawPolygon(self.image.copy(), self.mapX, self.mapY)
            image = MoilUtils.drawPoint(image, self.point, radius)
            self.result_image = MoilUtils.remap(self.image, self.mapX, self.mapY)
            result = MoilUtils.drawLine(self.result_image.copy())
            MoilUtils.showImageToLabel(self.label_Result_Image,
                                       result,
                                       self.width_result_image, self.angle, plusIcon=True)
            MoilUtils.showImageToLabel(self.label_Original_Image,
                                       image,
                                       self.width_original_image)
        self.show_percentage()

    def save_image(self):
        """
        Save image into local directory, it can save original image or
        result image from panorama or anypoint processing.

        """
        if self.image is not None:
            image = self.image if self.normal_view else self.result_image
            if self.dir_save is None or self.dir_save == "":
                self.video_controller.pauseVideo()
                self.dir_save = MoilUtils.selectDirectory(self)
            if self.dir_save:
                self.name_saved = MoilUtils.saveImage(image, self.dir_save, self.type_camera)
                self.addWidget(image)
                QtWidgets.QMessageBox.information(
                    self.parent, "Information", "Image saved !!\n\nLoc @: " + self.dir_save)

    def addWidget(self, image):
        """
        Add the image widget in the list widget_controller of saved image. it can be reopen when you select.
        Args:
            image (): the image saved.

        """
        height = MoilUtils.calculateHeight(self.image, 140)
        self.listWidget.setIconSize(QtCore.QSize(140, height))
        new_widget = QtWidgets.QListWidgetItem()

        image_ = MoilUtils.resizeImage(image, 140)
        imagePixmap = QtGui.QImage(
            image_.data,
            image_.shape[1],
            image_.shape[0],
            QtGui.QImage.Format_RGB888).rgbSwapped()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagePixmap))
        new_widget.setIcon(icon)
        new_widget.setText(str(self.name_saved) + ".png")
        self.listWidget.addItem(new_widget)
        self.posVid.append(self.video_controller.pos_frame)

    def saved_image_activated(self):
        """
        Function that for connect with the event in list widget to reopen the image.

        """
        filename = self.dir_save + "/" + self.listWidget.currentItem().text()
        posFrame = self.posVid[self.listWidget.currentRow()]
        self.type_camera = MoilUtils.read_camera_type(filename)
        if self.cam:
            self.video_controller.pauseVideo()
            self.reset_mode_view()
            self.image = MoilUtils.readImage(filename)
            self.h, self.w = self.image.shape[:2]
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, posFrame)
            self.video_controller.nextFrame()
            if self.listWidget.count() == 1:
                self.listWidget.selectionModel().reset()

    def cropImage(self, rect):
        image = self.convertCv2ToQimage(self.image.copy()) if self.result_image is None \
            else self.convertCv2ToQimage(self.result_image.copy())
        height = MoilUtils.calculateHeight(self.image, self.width_result_image)
        ratio_x = self.w / self.width_result_image
        ratio_y = self.h / height
        x = rect.x() * ratio_x
        y = rect.y() * ratio_y
        width = rect.width() * ratio_x
        height = rect.height() * ratio_y
        rect = QtCore.QRect(x, y, width, height)
        croppedImage = image.copy(rect)
        point_1 = (round(x), round(y))
        point_2 = (round(x + width), round(y + height))
        ori_image = self.image.copy() if self.normal_view else self.result_image.copy()
        image = MoilUtils.drawRectangle(ori_image, point_1, point_2)
        return image, self.convertQImageToMat(croppedImage)

    @classmethod
    def convertCv2ToQimage(cls, im):
        qim = QtGui.QImage()
        if im is None:
            return qim
        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_Indexed8)
                qim.setColorTable([QtGui.qRgb(i, i, i) for i in range(256)])
            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_RGB888)
                elif im.shape[2] == 4:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_ARGB32)
        return qim

    @classmethod
    def convertQImageToMat(cls, incomingImage):
        """  Converts a QImage into an opencv MAT format  """
        incomingImage = incomingImage.convertToFormat(4)
        width = incomingImage.width()
        height = incomingImage.height()
        ptr = incomingImage.bits()
        ptr.setsize(incomingImage.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
        return cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)

    def show_percentage(self):
        count = self.comboBox_zoom.count()
        if count == 8:
            self.comboBox_zoom.addItem("")
        self.comboBox_zoom.setCurrentIndex(8)
        size = round((self.width_result_image / self.w) * 100)
        self.comboBox_zoom.setItemText(8, (str(size) + "%"))

    def combo_percentage_zoom(self):
        if self.image is not None:
            self.comboBox_zoom.removeItem(8)
            percent = self.comboBox_zoom.currentText()
            percent = int(percent.replace("%", ""))
            self.width_result_image = round((self.w * percent) / 100)
            self.showToWindow()

    def reset_mode_view(self):
        """
        Update the properties' widget_controller when you reset.

        """
        self.result_image = None
        self.width_result_image = 1080
        self.normal_view = True
        self.anypoint.resetAlphaBeta()
        self.btn_Record_video.setChecked(False)
        self.frame_navigator.hide()
        self.frame_panorama.hide()

    def control_frame_view_button(self):
        """
        control the button in anypoint and panorama mode.

        """
        # print(self.button_menu.isChecked())
        if self.button_menu.isChecked():
            if self.anypoint_view:
                self.frame_navigator.hide()
                # self.label_34.hide()
            elif self.panorama_view:
                self.frame_panorama.hide()
                # self.label_34.hide()
            else:
                print("coming soon")
        else:
            if self.anypoint_view:
                self.frame_navigator.show()
                # self.label_34.show()
            elif self.panorama_view:
                self.frame_panorama.show()
            else:
                print("coming soon")

    def maximize_view(self):
        """
        Control the widget on user interface to make possible in maximum size.

        """
        self.label_saved_image.hide()
        self.listWidget.hide()
        self.frame_original_image.hide()
        self.frame_help.hide()
        self.frame_feature.hide()
        self.frame_2.hide()
        self.frame_Open_Source.hide()
        self.frame_rotate.hide()
        self.frame_zoom.hide()
        self.frame_save.hide()
        self.label_Application.hide()
        self.frame_13.hide()
        self.frame_16.hide()
        self.frame_17.hide()
        self.frame_18.hide()
        self.labelOrginalTitle.hide()
        self.label_time_recent.hide()
        self.slider_Video.hide()
        self.label_time_end.hide()
        self.frame_apps.hide()
        self.frame_clear.hide()
        self.labelrecenterTitle.hide()
        self.frameRecenter.hide()
        self.statusbar.hide()

    def minimize_view(self):
        """
        Control the widget on user interface to make possible in minimum size.

        """
        self.labelOrginalTitle.show()
        self.label_saved_image.show()
        self.listWidget.show()
        self.frame_original_image.show()
        self.frame_help.show()
        self.frame_feature.show()
        self.frame_2.show()
        self.frame_Open_Source.show()
        self.frame_rotate.show()
        self.frame_zoom.show()
        self.frame_save.show()
        self.label_Application.show()
        self.frame_13.show()
        self.frame_16.show()
        self.frame_17.show()
        self.frame_18.show()
        self.label_time_recent.show()
        self.slider_Video.show()
        self.label_time_end.show()
        self.frame_apps.show()
        self.frame_clear.show()
        self.statusbar.show()
        self.labelOrginalTitle.show()
        if self.buttonRecenter.isChecked():
            if self.panorama_view:
                self.labelrecenterTitle.show()
                self.frameRecenter.show()

    def actionRecordVideo(self):
        """
        Create video writer to save video.

        """
        if self.image is None:
            self.actionRecord_video.setChecked(False)
        else:
            if self.cam:
                if self.actionRecord_video.isChecked():
                    if self.video_controller.play:
                        self.video_controller.pauseVideo()
                    if self.videoDir is None or self.videoDir == "":
                        self.videoDir = MoilUtils.selectDirectory()
                    if self.videoDir:
                        ss = datetime.datetime.now().strftime("%m%d%H_%M%S")
                        frame_width = int(self.cap.get(3))
                        frame_height = int(self.cap.get(4))
                        filename = "Recorded"  # if self.parent.normal_view else "result"

                        name = self.videoDir + "/" + filename + "_" + str(ss) + ".avi"
                        answer = QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            " Start Record Video !!",
                            QtWidgets.QMessageBox.Yes,
                            QtWidgets.QMessageBox.No)

                        if answer == QtWidgets.QMessageBox.Yes:
                            self.video_controller.playVideo()
                            self.video_writer = cv2.VideoWriter(
                                name, cv2.VideoWriter_fourcc(
                                    *'XVID'), self.video_controller.fps, (frame_width, frame_height))
                            os.makedirs(os.path.dirname(name), exist_ok=True)
                            self.btn_Record_video.setChecked(True)
                            self.btn_Record_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.actionRecord_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.record = True
                        if answer == QtWidgets.QMessageBox.No:
                            self.actionRecord_video.setChecked(False)
                            self.record = False
                    else:
                        self.videoDir = None
                        self.actionRecord_video.setChecked(False)

                else:
                    if self.videoDir:
                        self.video_controller.timer.stop()
                        self.btn_play_pouse.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
                        QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            "Video saved !!\n\nLoc: " +
                            self.videoDir)
                        self.video_writer = None
                        self.video_controller.play = False
                        self.record = False
                        self.actionRecord_video.setChecked(False)
                        self.btn_Record_video.setChecked(False)
                        self.btn_Record_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))
                        self.actionRecord_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))

    def buttonRecordVideo(self):
        """
        Create video writer to save video.

        """
        if self.image is None:
            self.btn_Record_video.setChecked(False)
        else:
            if self.cam:
                if self.btn_Record_video.isChecked():
                    if self.video_controller.play:
                        self.video_controller.pauseVideo()
                    if self.videoDir is None or self.videoDir == "":
                        self.videoDir = MoilUtils.selectDirectory()
                    if self.videoDir:
                        ss = datetime.datetime.now().strftime("%m%d%H_%M%S")
                        frame_width = int(self.cap.get(3))
                        frame_height = int(self.cap.get(4))
                        filename = "Recorded"  # if self.parent.normal_view else "result"

                        name = self.videoDir + "/" + filename + "_" + str(ss) + ".avi"
                        answer = QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            " Start Record Video !!",
                            QtWidgets.QMessageBox.Yes,
                            QtWidgets.QMessageBox.No)

                        if answer == QtWidgets.QMessageBox.Yes:
                            self.video_controller.playVideo()
                            self.video_writer = cv2.VideoWriter(
                                name, cv2.VideoWriter_fourcc(
                                    *'XVID'), self.video_controller.fps, (frame_width, frame_height))
                            os.makedirs(os.path.dirname(name), exist_ok=True)
                            self.actionRecord_video.setChecked(True)
                            self.btn_Record_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.actionRecord_video.setIcon(
                                QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecording())))
                            self.record = True
                        if answer == QtWidgets.QMessageBox.No:
                            self.btn_Record_video.setChecked(False)
                            self.record = False
                    else:
                        self.videoDir = None
                        self.btn_Record_video.setChecked(False)

                else:
                    if self.videoDir:
                        self.video_controller.timer.stop()
                        self.btn_play_pouse.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconPlay())))
                        QtWidgets.QMessageBox.information(
                            self.parent,
                            "Information",
                            "Video saved !!\n\nLoc: " +
                            self.videoDir)
                        self.video_writer = None
                        self.video_controller.play = False
                        self.record = False
                        self.actionRecord_video.setChecked(False)
                        self.btn_Record_video.setChecked(False)
                        self.btn_Record_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))
                        self.actionRecord_video.setIcon(
                            QtGui.QIcon(QtGui.QPixmap.fromImage(self.rs.iconRecord())))

    def onclickRecenter(self):
        if self.buttonRecenter.isChecked():
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : #81AED1; }\n")
            self.recenter.onclickRecenter()
            self.frame_panorama.show()
            # self.checkAuto.show()
        else:
            self.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(238, 238, 236); }\n")
            self.showToWindow()
            self.recImage = None

    def onclickReleaseNote(self):
        """
        Showing the message box to show help information obout this application.

        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Release Note")
        msgbox.setText(
            "New features MoilApp Version 3.2*\n\n"
            "There are many updates in this version, "
            "which can improve the results of processing fisheye camera images, including: \n\n"
            "1. Shortcuts for every process and button work well, show on accessibility in menu help\n"
            "2. Added redo function during zoom area\n"
            "3. Added Menubar View for manipulate view image\n"
            "4. Fix bug in zoom area\n"
            "5. Record video using action or button\n"
            "\nMore Documentation about MoilApp, visit: \nhttps://oil-mcut.educationhost.cloud/moilapp/\n")
        msgbox.exec()

    @classmethod
    def checkUpdate(cls):
        webbrowser.open('https://github.com/MoilOrg/MoilApp')

    def onclick_accessibility(self):
        """
        Open prompt for accessibility MoilApp
        Returns:

        """
        QtWidgets.QMessageBox.information(
            self.parent, "Accessibility", "MoilApp Accessibility\n\n"
                                          "Information !!\n"
                                          "Crtl + I\t: Open Image\n"
                                          "Ctrl + V\t: Open Video\n"
                                          "Ctrl + C\t: Open cam\n"
                                          "Ctrl + P\t: Open Camera parameters form\n"
                                          "Ctrl + R\t: Record Video\n"
                                          "Ctrl + S\t: Save image\n"
                                          "Ctrl + Q\t: Exit apps\n"
                                          "+ \t: Zoom In\n"
                                          "- \t: Zoom Out\n"
                                          "F11 \t: Maximized window\n"
                                          "Esc \t: Minimized window\n"
                                          "Ctrl + Left\t: Backward video in 5 seconds\n"
                                          "Space\t: play/pause video\n"
                                          "0 \t: Stop video\n"
                                          "Ctrl + Right\t: Forward video in 5 seconds\n"
                                          "Up\t: Up View\n"
                                          "Right\t: Right view\n"
                                          "Left\t: Left view\n"
                                          "Down\t: Down View\n"
                                          "Ctrl + Shift + /\t:show help\n"
                                          "Alt + Shift + A\t:Show Accessibility\n\n")

    def onclick_help(self):
        """
        Showing the message box to show help information obout this application.

        """
        self.winHelp.help_moilApp()

    def onclick_help_moil(self):
        self.dialogHelp.show()

    def updateLabel(self, filename=None):
        if filename is None:
            self.parent.setWindowTitle("MoilApp - " + self.type_camera)
        else:
            self.parent.setWindowTitle("MoilApp - " + filename)
            self.label_Application.setText("Camera: " + self.type_camera)

    def onclick_exit(self):
        """

        Returns:

        """
        self.parent.close()

    def closeEvent(self, event):
        """
        Control the close event by ask yes or no.
        Args:
            event ():

        Returns:

        """
        if self.cam:
            self.video_controller.pauseVideo()
        reply = QtWidgets.QMessageBox.question(
            self.parent,
            'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            if self.open_plugin:
                for i in range(len(self.control_plugin.plugins.name_application)):
                    self.control_plugin.plugin_win[i].close()
            if self.cam:
                self.cap.release()
            event.accept()
        else:
            event.ignore()
