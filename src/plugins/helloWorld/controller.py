from .user_interface.ui_mainwindow import Ui_MainWindow


class UiController(Ui_MainWindow):
    def __init__(self, mainWindow):
        super(UiController, self).__init__()
        self.parent = mainWindow
        self.setupUi(self.parent)
