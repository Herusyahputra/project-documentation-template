from ShowResult import ShowImageResult
from PyQt5 import QtCore


class ViewWindow:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.actionMaximized.triggered.connect(self.show_Maximized)
        self.parent.ui.actionMinimized.triggered.connect(self.show_Minimized)
        self.parent.ui.actionsave_Image_box.triggered.connect(self.hideImageBox)
        self.parent.ui.actionToolbar.triggered.connect(self.hideToolbar)

    def show_Maximized(self):
        if self.parent.image is None:
            pass
        else:
            self.parent.ui.scrollArea_2.hide()
            self.parent.ui.frameSaveImage.hide()
            self.parent.width_img = 2000
            self.parent.ui.scrollArea_3.setMaximumSize(QtCore.QSize(self.parent.width_img, 16777215))
            self.parent.application.applicationMoildevs()
            self.maxi = True

    def show_Minimized(self):
        if self.parent.image is None:
            pass
        else:
            self.parent.ui.scrollArea_2.show()
            self.parent.ui.frameSaveImage.show()
            self.parent.width_img = 1400
            self.parent.ui.scrollArea_3.setMaximumSize(QtCore.QSize(self.parent.width_img, 16777215))
            self.parent.application.applicationMoildevs()
            self.maxi = False

    def hideImageBox(self):
        if self.parent.ui.actionsave_Image_box.isChecked():
            self.parent.ui.frameSaveImage.show()
        else:
            self.parent.ui.frameSaveImage.hide()

    def hideToolbar(self):
        if self.parent.ui.actionToolbar.isChecked():
            self.parent.ui.toolBar.hide()
        else:
            self.parent.ui.toolBar.show()
