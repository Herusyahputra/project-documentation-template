from ShowResult import ShowImageResult

class FastView:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.pushButton_43.clicked.connect(self.upLeft)
        self.parent.ui.pushButton_41.clicked.connect(self.left)
        self.parent.ui.pushButton_42.clicked.connect(self.lefDown)
        self.parent.ui.pushButton_23.clicked.connect(self.up)
        self.parent.ui.pushButton_24.clicked.connect(self.down)
        self.parent.ui.pushButton_19.clicked.connect(self.right)
        self.parent.ui.pushButton_20.clicked.connect(self.rightDown)
        self.parent.ui.pushButton_25.clicked.connect(self.center)
        self.parent.ui.pushButton_26.clicked.connect(self.upRight)

    def upLeft(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 75
            self.parent.beta = -45
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 45
            self.parent.beta = -45
        self.parent.anypoint.anypoint_view()

    def up(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 75
            self.parent.beta = 0
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 50
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()

    def upRight(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 45
            self.parent.beta = 75
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 45
            self.parent.beta = 45
        self.parent.anypoint.anypoint_view()

    def left(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = -90
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 0
            self.parent.beta = -75
        self.parent.anypoint.anypoint_view()

    def center(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 0
            self.parent.beta = 0
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 0
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()

    def right(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 90
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 0
            self.parent.beta = 65
        self.parent.anypoint.anypoint_view()

    def lefDown(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 225
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = -45
            self.parent.beta = -45
        self.parent.anypoint.anypoint_view()

    def down(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 180
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = -65
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()

    def rightDown(self):
        self.parent.coor = self.parent.center
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 135
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = -45
            self.parent.beta = 45
        self.parent.anypoint.anypoint_view()
