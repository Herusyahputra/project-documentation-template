import Utils
from ShowResult import ShowImageResult


class Panorama:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.max = float(110)
        self.min = float(10)
        self.parent.ui.lineEdit_Max.setText(str(self.max))
        self.parent.ui.lineEdit_Min.setText(str(self.min))
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.checkPanorama.clicked.connect(self.panorama_view)
        self.parent.ui.pushButtonPanorama.clicked.connect(self.set_pano)

    def set_pano(self):
        self.max = float(self.parent.ui.lineEdit_Max.text())
        self.min = float(self.parent.ui.lineEdit_Min.text())
        self.panorama_view()

    def panorama_view(self):
        if self.parent.image is None:
            pass
        else:
            image = self.parent.image.copy()
            if self.parent.ui.checkPanorama.isChecked():
                self.parent.ui.checkAnypoint.setChecked(False)
                self.parent.ui.frame_4.setDisabled(True)
                self.parent.ui.frame_5.setDisabled(False)
                self.parent.ui.lineEdit_Max.setText(str(self.max))
                self.parent.ui.lineEdit_Min.setText(str(self.min))
                self.parent.mapX, self.parent.mapY = self.parent.moildev.getPanoramaMaps(self.min, self.max)
                # self.parent.moildev.PanoramaX(self.parent.mapX, self.parent.mapY, self.parent.imageWidth, self.parent.imageHeight, self.parent.m_ratio,
                #                               self.max, self.min)

                self.showOriginalPanorama()
                self.show.showPanoAnyImage()

            else:
                self.parent.ui.frame_4.setDisabled(True)
                self.parent.ui.frame_5.setDisabled(True)
                self.show.showOriginalImage(image)
                self.show.showResult(image)

    def showOriginalPanorama(self):
        image = self.parent.image.copy()
        if self.parent.anypoint_Image is not None:
            self.parent.coor = self.parent.center
            oriImage = Utils.drawPoint(image, self.parent.imageHeight, self.parent.coor)
        else:
            if self.parent.coor:
                oriImage = Utils.drawPoint(image, self.parent.imageHeight, self.parent.coor)
            else:
                oriImage = Utils.drawPoint(image, self.parent.imageHeight, self.parent.center)
        self.show.showOriginalImage(oriImage)
