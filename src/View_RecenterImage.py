import cv2
from ShowResult import ShowImageResult


class RecenterImage:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.parent.ui.spinBox_coorX.valueChanged.connect(self.positionCoorX)
        self.parent.ui.spinBox_coorY.valueChanged.connect(self.positionCoorY)
        self.parent.ui.checkBox_ShowRecenterImage_2.clicked.connect(self.recenterImage)

    def recenterImage(self):
        if self.parent.ui.checkBox_ShowRecenterImage_2.isChecked():
            self.parent.ui.frame_setcenter.show()
            self.frameRecenter()
            self.parent.ui.frame_setcenter.show()
            self.max = float(self.parent.ui.lineEdit_Max.text())
            self.min = float(self.parent.ui.lineEdit_Min.text())
            self.parent.revImage = self.reverseImage(self.parent.image, self.parent.res, self.parent.alpha, self.parent.beta)
            self.parent.moildev.PanoramaX(self.parent.mapX, self.parent.mapY, self.parent.imageWidth, self.parent.imageHeight,
                                   self.parent.m_ratio, self.max, self.min)
            self.show.showInRecenterLabel(self.parent.revImage)
            self.show.showPanoAnyImage(self.parent.angle)
            self.updatePossCenter()

        else:
            self.parent.ui.labelRecenter.hide()
            self.parent.ui.labelImagerecenter.hide()
            self.parent.ui.frame_setcenter.hide()

    def frameRecenter(self):
        self.parent.ui.checkPanoramaAuto.setChecked(False)
        self.parent.ui.checkBox_ShowRecenterImage_2.setChecked(True)
        self.parent.ui.labelRecenter.show()
        self.parent.ui.labelImagerecenter.show()
        self.parent.ui.label_31.hide()
        self.parent.ui.label_32.hide()

    def updatePossCenter(self):
        self.parent.ui.spinBox_coorX.setValue(self.parent.coorX)
        self.parent.ui.spinBox_coorY.setValue(self.parent.coorY)

    def setCoorCenterObject(self):
        delta_x = round(self.parent.coorX - self.parent.imageWidth * 0.5)
        delta_y = round(- (self.parent.coorY - self.parent.imageHeight * 0.5))
        self.parent.alpha, self.parent.beta = self.parent.config.get_alpha_beta(0, delta_x, delta_y)

    def positionCoorX(self):
        if self.parent.image is None:
            pass
        else:
            self.parent.coorX = self.parent.ui.spinBox_coorX.value()
            self.setCoorCenterObject()
            self.recenterImage()

    def positionCoorY(self):
        if self.parent.image is None:
            pass
        else:
            self.parent.coorY = self.parent.ui.spinBox_coorY.value()
            self.setCoorCenterObject()
            self.recenterImage()

    def reverseImage(self, dst, src, alpha, beta):
        self.parent.moildev.PanoramaM_Rt(self.parent.mapX, self.parent.mapY, self.parent.imageWidth,
                                         self.parent.imageHeight, self.parent.m_ratio, 110, alpha, beta)
        panoImage = cv2.remap(dst, self.parent.mapX, self.parent.mapY, cv2.INTER_CUBIC)
        self.parent.moildev.revPanorama(panoImage, src, self.parent.imageWidth, self.parent.imageHeight, 110, beta)
        return src
