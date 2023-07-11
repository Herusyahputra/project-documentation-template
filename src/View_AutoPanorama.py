import cv2
# from libs.CenterDetector import FindCenter
from ShowResult import ShowImageResult


class AutoPanorama:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        # self.detector = FindCenter()
        self.parent.ui.checkBox_CenterLumen.clicked.connect(self.centerLumen)
        self.parent.ui.checkPanoramaAuto.clicked.connect(self.autoMode)

    def frameAuto(self):
        self.parent.ui.labelRecenter.show()
        self.parent.ui.labelImagerecenter.show()
        self.parent.ui.checkBox_ShowRecenterImage_2.setChecked(False)
        self.parent.ui.label_31.show()
        self.parent.ui.label_32.show()

    def hideAutoframe(self):
        self.parent.ui.label_31.hide()
        self.parent.ui.label_32.hide()
        self.parent.ui.labelRecenter.clear()
        self.parent.ui.labelRecenter.hide()
        self.parent.ui.labelImagerecenter.hide()

    def centerLumen(self):
        image = self.parent.image.copy()
        if self.parent.ui.checkBox_CenterLumen.isChecked():
            self.parent.ui.checkPanoramaAuto.setChecked(False)
            self.frameAuto()
            self.annot_image = self.parent.image.copy()
            coordinate = self.detector.center_coordinate(self.annot_image)
            x = coordinate[0]

            if type(x) is int:
                delta_x = round(coordinate[0] - self.parent.imageWidth * 0.5)
                delta_y = round(- (coordinate[1] - self.parent.imageHeight * 0.5))
                self.alpha, self.beta = self.parent.config.get_alpha_beta(0, delta_x, delta_y)
                # print("Alpha: " + str(self.alpha), "Beta: " + str(self.beta))
                # cv2.putText(self.annot_image, "center = " + str(coordinate),
                #             (15, 55), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 1)
                cv2.circle(self.annot_image, coordinate, 25, (0, 255, 0), -1)
                self.show.showInRecenterLabel(self.annot_image)
                self.show.showResult(self.annot_image)
                coordinate = str(coordinate)
                center_p = self.parent.ui.label_32
                center_p.setText(coordinate)

            else:
                # cv2.putText(self.annot_image, "Not detected",
                #             (15, 15), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
                self.show.showInRecenterLabel(self.annot_image)
                self.show.showResult(self.annot_image)
                center_p = self.parent.ui.label_32
                center_p.setText("Not Detected")

        else:
            self.hideAutoframe()
            self.show.showOriginalImage(image)
            self.show.showResult(image)

    def autoMode(self):
        image = self.parent.image.copy()
        if self.parent.ui.checkPanoramaAuto.isChecked():
            self.parent.ui.checkBox_CenterLumen.setChecked(False)
            self.parent.ui.statusMessage.setText("Debug still on development")
            # self.annot_image = self.parent.image.copy()
            # self.frameAuto()
            # coordinate = self.detector.center_coordinate(self.annot_image)
            # x = coordinate[0]
            #
            # if type(x) is int:
            #     delta_x = round(coordinate[0] - self.parent.imageWidth * 0.5)
            #     delta_y = round(- (coordinate[1] - self.parent.imageHeight * 0.5))
            #     self.alpha, self.beta = self.parent.config.get_alpha_beta(0, delta_x, delta_y)
            #     # print("Alpha: " + str(self.alpha), "Beta: " + str(self.beta))
            #     # cv2.putText(self.annot_image, "center = " + str(coordinate),
            #     #             (15, 55), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 25, 5), 1)
            #     cv2.circle(self.annot_image, coordinate, 25, (255, 255, 255), -1)
            #
            #     self.show.showInRecenterLabel(self.annot_image)
            #     self.max = float(self.parent.ui.lineEdit_Max.text())
            #     self.min = float(self.parent.ui.lineEdit_Min.text())
            #     self.parent.revImage = self.parent.recenter.reverseImage(self.parent.image, self.parent.res,
            #                                                              self.parent.alpha,
            #                                                              self.parent.beta)
            #     self.parent.moildev.PanoramaX(self.parent.mapX, self.parent.mapY, self.parent.imageWidth,
            #                                   self.parent.imageHeight,
            #                                   self.parent.m_ratio, self.max, self.min)
            #     self.show.showInRecenterLabel(self.parent.revImage)
            #     self.show.showPanoAnyImage(self.parent.angle)
            #     coordinate = str(coordinate)
            #     center_p = self.parent.ui.label_32
            #     center_p.setText(coordinate)
            #
            # else:
            #     cv2.putText(self.annot_image, "Not detected",
            #                 (15, 15), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
            #     self.parent.revImage = image
            #
            #     self.show.showInRecenterLabel(self.parent.revImage)
            #     self.show.showPanoAnyImage(self.parent.angle)
            #     center_p = self.parent.ui.label_32
            #     center_p.setText("Not Detected")

        else:
            self.parent.ui.statusMessage.setText(self.parent.ui.comboBox.currentText())
            self.hideAutoframe()
            # self.show.showOriginalImage(image)
            # self.show.showResult(image)
