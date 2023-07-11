from ShowResult import ShowImageResult


class Rotate:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.pushButton_21.clicked.connect(self.rotate_left)
        self.parent.ui.pushButton_22.clicked.connect(self.rotate_right)

    def rotate_left(self):
        if self.parent.angle == 180:
            pass
        else:
            self.parent.angle += 10
        self.show.showPanoAnyImage(self.parent.angle)

    def rotate_right(self):
        if self.parent.angle == 180:
            pass
        else:
            self.parent.angle -= 10
        self.show.showPanoAnyImage(self.parent.angle)
