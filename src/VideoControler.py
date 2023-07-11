from PyQt5 import QtCore, QtGui
import cv2


class Video_Controler:
    def __init__(self, Mainwindow):
        self.parent = Mainwindow
        self.play = False
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.actionClose_Cam.triggered.connect(self.stop_camera)
        self.parent.ui.videoPlay.clicked.connect(self.videoPlayPouse)
        self.parent.ui.videoStop.clicked.connect(self.stop_video)
        self.parent.ui.videoSkip.clicked.connect(self.skip_video)
        self.parent.ui.videoBack.clicked.connect(self.prev_video)
        self.parent.ui.sliderVideotime.valueChanged.connect(self.changeValue)

    def videoButtonDisable(self):
        self.parent.ui.videoPlay.setDisabled(True)
        self.parent.ui.videoStop.setDisabled(True)
        self.parent.ui.videoSkip.setDisabled(True)
        self.parent.ui.videoBack.setDisabled(True)
        self.parent.ui.recordBtn.setDisabled(True)
        self.parent.ui.sliderVideotime.setDisabled(True)
        self.parent.ui.label_4.setDisabled(True)
        self.parent.ui.label_3.setDisabled(True)

    def videoButtonEnable(self):
        self.parent.ui.videoPlay.setDisabled(False)
        self.parent.ui.videoStop.setDisabled(False)
        self.parent.ui.videoSkip.setDisabled(False)
        self.parent.ui.videoBack.setDisabled(False)
        self.parent.ui.recordBtn.setDisabled(False)
        self.parent.ui.sliderVideotime.setDisabled(False)
        self.parent.ui.label_4.setDisabled(False)
        self.parent.ui.label_3.setDisabled(False)

    def videoButtonCamera(self):
        self.parent.ui.videoPlay.setDisabled(False)
        self.parent.ui.videoStop.setDisabled(False)
        self.parent.ui.videoSkip.setDisabled(False)
        self.parent.ui.videoBack.setDisabled(False)
        self.parent.ui.recordBtn.setDisabled(False)
        self.parent.ui.sliderVideotime.setDisabled(True)
        self.parent.ui.label_4.setDisabled(True)
        self.parent.ui.label_3.setDisabled(True)

    def reset_time(self):
        current = self.parent.ui.label_3
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00:00")

        current_1 = self.parent.ui.label_4
        current_1.setAlignment(QtCore.Qt.AlignCenter)
        current_1.setText("00:00")

    def videoPlayPouse(self):
        if self.play:
            self.timer.stop()
            self.parent.ui.videoPlay.setIcon(QtGui.QIcon("assets/control.png"))
            self.pause_video()
            self.play = False

        else:
            self.parent.ui.videoPlay.setIcon(QtGui.QIcon("assets/control-pause.png"))
            self.play_video()
            self.play = True

    def play_video(self):
        """ Video Controller"""
        if self.parent.cap.isOpened():
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.parent.next_frame_slot)
            self.timer.start(1000. / self.parent.fps)
        else:
            pass

    def pause_video(self):
        self.timer.stop()

    def stop_video(self):
        self.play = False
        self.parent.ui.videoPlay.setIcon(QtGui.QIcon("assets/control.png"))
        if self.parent.cap.isOpened():
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.parent.next_frame_slot()
            self.pause_video()
            self.reset_time()
            self.parent.application.applicationMoildevs()
            self.parent.image = None
        else:
            pass

    def stop_camera(self):
        if self.parent.cam:
            self.timer.stop()
            self.parent.cap.release()
            self.parent.ui.windowOri.clear()
            self.parent.ui.windowResult.clear()
        else:
            pass

    def prev_video(self):
        """ show 5 second previous frame"""
        if self.parent.cap.isOpened():
            position = self.parent.pos_frame - 5 * self.parent.fps
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.parent.next_frame_slot()
        else:
            pass

    def skip_video(self):
        """ show 5 second previous frame"""
        if self.parent.cap.isOpened():
            position = self.parent.pos_frame + 5 * self.parent.fps
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.parent.next_frame_slot()
        else:
            pass

    def changeValue(self, value):
        if self.parent.cap.isOpened():
            dst_frame = self.parent.frame_count * value / self.parent.ui.sliderVideotime.maximum() + 1
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, dst_frame)
            self.parent.next_frame_slot()
            self.timer.stop()
        else:
            pass

    def controler(self):
        dst_value = self.parent.pos_frame * (self.parent.ui.sliderVideotime.maximum() + 1) / self.parent.frame_count
        self.parent.ui.sliderVideotime.blockSignals(True)
        self.parent.ui.sliderVideotime.setValue(dst_value)
        self.parent.ui.sliderVideotime.blockSignals(False)

        current = self.parent.ui.label_3
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("%02d : %02d" % (self.parent.minute, self.parent.sec))

        if self.parent.minute > 1000:
            my_label3 = self.parent.ui.label_4
            my_label3.setAlignment(QtCore.Qt.AlignCenter)
            my_label3.setText("00:00")

        else:
            my_label3 = self.parent.ui.label_4
            my_label3.setAlignment(QtCore.Qt.AlignCenter)
            my_label3.setText("%02d : %02d" % (self.parent.minutes, self.parent.seconds))
