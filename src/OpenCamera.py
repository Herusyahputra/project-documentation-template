from MoildevUi.OpenCam import Ui_Dialog
import cv2
from PyQt5 import QtWidgets


class OpenCameras(Ui_Dialog):
    def __init__(self, MainWindow, recentWindow):
        super().__init__(MainWindow)
        '''
         >> Main window is the the inheritance from the main UI this program
         >> Recent window is the UI for this window. 
         this make it possible to communication between this two UI
        '''
        self.parent_win = MainWindow
        self.parent_dialog = recentWindow
        self.setupUi(self.parent_dialog)
        self.videoStreamURL = None
        self.lineEdit_14.setText('http://192.168.100.226:8000/stream.mjpg')

        self.handleActivatedCombobox()
        self.connectToButton()

    def connectToButton(self):
        self.comboBox.activated.connect(self.handleActivatedCombobox)
        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.exit)
        self.detectPort.clicked.connect(self.checkPortCamera)

    def handleActivatedCombobox(self):
        if self.comboBox.currentText() == 'USB Camera':
            self.label_59.hide()
            self.lineEdit_14.hide()
            self.framePortUsb.show()
            # self.parent_win.stop_camera()

        else:
            # self.frame_2.show()
            self.label_59.show()
            self.lineEdit_14.show()
            self.framePortUsb.hide()
            # self.parent_win.stop_camera()

    def checkPortCamera(self):
        all_camera_idx_available = []
        for camera_idx in range(5):
            cap = cv2.VideoCapture(camera_idx)
            if cap.isOpened():
                all_camera_idx_available.append(camera_idx)
                cap.release()

        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Camera Port Available")
        msgbox.setText(
            "Select the port camera from the number in list !! \n"
            "Available Port = " + str(all_camera_idx_available))
        msgbox.exec()

    def vidUrl(self):
        if self.comboBox.currentText() == 'USB Camera':
            self.videoStreamURL = int(self.portCamera.currentText())
        else:
            self.videoStreamURL = self.lineEdit_14.text()
        if self.videoStreamURL is None:
            return None
        else:
            return self.videoStreamURL

    def ok(self):
        self.parent_win.cameraOpen()
        self.parent_dialog.close()

    def exit(self):
        self.parent_dialog.close()
