from ShowResult import ShowImageResult


class Visual_Odometry:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)

    def visualOdometry(self):
        if self.parent.image is None:
            pass
        else:
            self.show.showOriginalImage(self.parent.image)
            self.show.show_development()
