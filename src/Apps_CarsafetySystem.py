from ShowResult import ShowImageResult


class Car_Safety:
    def __init__(self, Mainwindow):
        self.parent = Mainwindow
        self.show = ShowImageResult(self.parent)

    def carAplication(self):
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
