from ShowResult import ShowImageResult


class Surveillance:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)

    def surveillance(self):
        if self.parent.image is None:
            pass
        else:
            image = self.parent.image.copy()
            self.show.showOriginalImage(image)
            if self.parent.ui.checkAnypoint.isChecked():
                self.parent.anypoint.showPolygon()
                self.show.showPanoAnyImage(self.parent.angle)
            elif self.parent.ui.checkPanorama.isChecked():
                self.parent.panorama.showOriginalPanorama()
                self.show.showPanoAnyImage()
            else:
                self.show.showResult(image)
