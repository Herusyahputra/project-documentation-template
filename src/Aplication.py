from DefaultView import DefaultView
from Apps_CarsafetySystem import Car_Safety
from Apps_Surveillance import Surveillance
from Apps_TubeInspection import TubeInspection
from Apps_Colonoscopy import Colonoscopy
from Apps_ObjectDetection import Object_detection
from Apps_FaceDetection import FaceDetect
from Apps_Measurment import Measurement
from Apps_Reconstruction import Reconstruction
from Apps_VisualOdometry import Visual_Odometry
from Apps_SetupCenterCamera import SetupCenterCamera


class Application:
    def __init__(self, Mainwindow):
        self.parent = Mainwindow
        self.default = DefaultView(self.parent)
        self.car_apps = Car_Safety(self.parent)
        self.surveillance = Surveillance(self.parent)
        self.tube = TubeInspection(self.parent)
        self.colonoscopy = Colonoscopy(self.parent)
        self.objectDetect = Object_detection(self.parent)
        self.faceDetect = FaceDetect(self.parent)
        self.measure = Measurement(self.parent)
        self.reconstruction_image = Reconstruction(self.parent)
        self.visualOdometry = Visual_Odometry(self.parent)
        self.setupCameraCenter = SetupCenterCamera(self.parent)

        self.setupCameraCenter.initRadiusCircle()
        self.init_frame_hide()
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.comboBox.activated.connect(self.applicationMoildevs)
        self.parent.ui.checkDebugMode.clicked.connect(self.debug_Apps)

    def init_frame_hide(self):
        self.parent.ui.checkPanorama.setChecked(False)
        self.parent.ui.checkAnypoint.setChecked(False)
        self.parent.ui.checkDebugMode.setChecked(False)
        self.parent.ui.frame_7.hide()
        self.parent.ui.labelRecenter.hide()
        self.parent.ui.labelImagerecenter.hide()
        self.parent.ui.label_31.hide()
        self.parent.ui.label_32.hide()
        self.parent.ui.windowResult.show()
        self.parent.ui.PlussIcon.show()
        self.parent.ui.gridFrame.hide()
        self.parent.ui.frame3D.hide()
        self.parent.ui.frame_2.hide()
        self.parent.ui.frame_7.hide()
        self.parent.ui.frame_8.hide()
        self.parent.ui.checkBox_CenterLumen.hide()
        self.parent.ui.showFovCam.hide()
        self.parent.ui.spinBoxFoVCaamera.hide()
        self.parent.ui.frame_setcenter.hide()
        self.parent.ui.frameSaveImage.hide()
        self.parent.ui.radioAnypointM1.setChecked(True)
        self.parent.ui.frame_4.setDisabled(True)
        self.parent.ui.frame_5.setDisabled(True)
        self.parent.ui.frame_2.setDisabled(True)
        self.parent.ui.frame_7.setDisabled(True)
        self.parent.ui.gridFrame_surveillance.hide()

    def frameOriginalHide(self):
        self.parent.ui.windowOri.hide()
        self.parent.ui.videoPlay.hide()
        self.parent.ui.videoStop.hide()
        self.parent.ui.videoSkip.hide()
        self.parent.ui.videoBack.hide()
        self.parent.ui.recordBtn.hide()
        self.parent.ui.sliderVideotime.hide()
        self.parent.ui.label_4.hide()
        self.parent.ui.label_3.hide()
        self.parent.ui.frame3D.show()
        self.parent.ui.windowResult.hide()
        self.parent.ui.PlussIcon.hide()
        self.parent.ui.windowOri.clear()
        self.parent.ui.windowResult.clear()
        self.parent.ui.PlussIcon.clear()
        self.parent.image = None

    def frameOriginalShow(self):
        self.parent.ui.windowOri.show()
        self.parent.ui.videoPlay.show()
        self.parent.ui.videoStop.show()
        self.parent.ui.videoSkip.show()
        self.parent.ui.videoBack.show()
        self.parent.ui.recordBtn.show()
        self.parent.ui.sliderVideotime.show()
        self.parent.ui.label_4.show()
        self.parent.ui.label_3.show()
        self.parent.ui.frame3D.hide()
        self.parent.ui.label3Dimage1.clear()
        self.parent.ui.label3Dimage2.clear()
        self.parent.image_1 = None
        self.parent.image_2 = None
        self.parent.ui.windowResult.show()
        self.parent.ui.PlussIcon.show()

    def applicationMoildevs(self):
        self.debug_Apps()
        if self.parent.ui.comboBox.currentIndex() == 0:
            '''
            << select here >> // Default showing
            '''
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkBox_ShowRecenterImage_2.hide()
            self.parent.ui.checkPanoramaAuto.hide()
            self.parent.ui.checkPanorama.show()
            self.parent.ui.checkAnypoint.show()
            self.parent.ui.frame_5.show()
            self.parent.ui.frame_4.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.parent.ui.radioAnypointM1.show()
            self.parent.ui.radioAnypointM2.show()
            self.parent.ui.checkDebugMode.hide()
            self.frameOriginalShow()
            self.default.defaultView()

        elif self.parent.ui.comboBox.currentIndex() == 1:
            """
            Car safety system Application
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkPanorama.hide()
            self.parent.ui.checkAnypoint.show()
            self.parent.ui.frame_5.hide()
            self.parent.ui.frame_4.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.parent.ui.radioAnypointM1.hide()
            self.parent.ui.radioAnypointM2.hide()
            self.parent.ui.radioAnypointM1.setChecked(False)
            self.parent.ui.radioAnypointM2.setChecked(True)
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalShow()
            self.car_apps.carAplication()

        elif self.parent.ui.comboBox.currentIndex() == 2:
            """
            Surveillance system Application
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkPanorama.hide()
            self.parent.ui.checkAnypoint.show()
            self.parent.ui.frame_5.hide()
            self.parent.ui.frame_4.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.parent.ui.radioAnypointM1.show()
            self.parent.ui.radioAnypointM2.show()
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalShow()
            self.surveillance.surveillance()

        elif self.parent.ui.comboBox.currentIndex() == 3:
            """
            Tube inspection system Application
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkPanorama.show()
            self.parent.ui.checkAnypoint.show()
            self.parent.ui.frame_4.show()
            self.parent.ui.frame_5.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.parent.ui.radioAnypointM1.hide()
            self.parent.ui.radioAnypointM2.hide()
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalShow()
            self.tube.tubeInspection()

        elif self.parent.ui.comboBox.currentIndex() == 4:
            """
            Colonoscopy system Application
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkPanorama.show()
            self.parent.ui.checkAnypoint.hide()
            self.parent.ui.frame_4.hide()
            self.parent.ui.frame_5.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.parent.ui.radioAnypointM1.hide()
            self.parent.ui.radioAnypointM2.hide()
            self.parent.ui.checkDebugMode.show()
            self.parent.ui.checkBox_CenterLumen.show()
            self.parent.ui.checkBox_ShowRecenterImage_2.show()
            self.parent.ui.checkPanoramaAuto.show()
            self.frameOriginalShow()
            self.colonoscopy.colonoscopy()

        elif self.parent.ui.comboBox.currentIndex() == 5:
            """
            Object detection system Application
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkBox_ShowRecenterImage_2.hide()
            self.parent.ui.checkPanoramaAuto.hide()
            self.parent.ui.checkPanorama.show()
            self.parent.ui.checkAnypoint.show()
            self.parent.ui.frame_5.show()
            self.parent.ui.frame_4.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.radioAnypointM1.show()
            self.parent.ui.radioAnypointM2.show()
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalShow()
            self.parent.ui.frame_8.show()
            self.parent.ui.frame_8.setDisabled(True)
            self.objectDetect.detectObject()

        elif self.parent.ui.comboBox.currentIndex() == 6:
            """
            Face Recognition detection system Application
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkBox_ShowRecenterImage_2.hide()
            self.parent.ui.checkPanoramaAuto.hide()
            self.parent.ui.checkPanorama.show()
            self.parent.ui.checkAnypoint.show()
            self.parent.ui.frame_5.show()
            self.parent.ui.frame_4.show()
            self.parent.ui.frame_7.hide()
            self.parent.ui.radioAnypointM1.show()
            self.parent.ui.radioAnypointM2.show()
            self.parent.ui.checkDebugMode.show()
            self.parent.ui.frame_8.hide()
            self.frameOriginalShow()
            self.faceDetect.faceRecognition()

        elif self.parent.ui.comboBox.currentIndex() == 7:
            """
            3D measurement Application
            """
            self.parent.ui.windowResult.hide()
            self.parent.ui.PlussIcon.hide()
            self.parent.ui.gridFrame.hide()
            self.parent.ui.frame3D.show()
            self.parent.ui.checkPanorama.hide()
            self.parent.ui.checkAnypoint.hide()
            self.parent.ui.frame_5.hide()
            self.parent.ui.frame_4.hide()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.parent.ui.frame_2.show()
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalHide()
            if self.parent.cap:
                self.parent.cap.release()
            self.measure.corner_detection()

        elif self.parent.ui.comboBox.currentIndex() == 8:
            """
            3D Reconstruction
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.frameOriginalShow()
            self.reconstruction_image.reconstructionImage()

        elif self.parent.ui.comboBox.currentIndex() == 9:
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalShow()
            self.parent.ui.frame_7.hide()
            self.parent.ui.frame_8.hide()
            self.visualOdometry.visualOdometry()

        elif self.parent.ui.comboBox.currentIndex() == 10:
            """
            Setup camera center
            """
            self.parent.ui.frame_2.hide()
            self.parent.ui.frame_2.setDisabled(True)
            self.parent.ui.checkPanorama.setChecked(False)
            self.parent.ui.checkAnypoint.setChecked(False)
            self.parent.ui.frame_5.hide()
            self.parent.ui.frame_4.hide()
            self.parent.ui.frame_7.show()
            self.parent.ui.frame_8.hide()
            self.parent.ui.checkPanorama.hide()
            self.parent.ui.checkAnypoint.hide()
            self.parent.ui.checkDebugMode.show()
            self.frameOriginalShow()
            self.setupCameraCenter.find_center()

        else:
            pass

    def debug_Apps(self):
        if self.parent.ui.comboBox.currentIndex() == 0:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText("Default Apps")

        elif self.parent.ui.comboBox.currentIndex() == 1:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 2:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 3:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())
        elif self.parent.ui.comboBox.currentIndex() == 4:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 5:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 6:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 7:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 8:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")

            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 9:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())

        elif self.parent.ui.comboBox.currentIndex() == 10:
            if self.parent.ui.checkDebugMode.isChecked():
                self.parent.ui.statusMessage.setText("Debug still on development")
            else:
                self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())
        else:
            pass
