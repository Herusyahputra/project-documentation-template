import webbrowser
from PyQt5 import QtWidgets, QtGui
from .Help import Win_Help
import os


class Help():
    def __init__(self):
        super(Help, self).__init__()
        self.dialogHelp = QtWidgets.QDialog()
        self.winHelp = Win_Help(self.dialogHelp)

    def open_user_guide_moildev(self):
        # file = os.path.realpath('./plugins/Thread_inspection/help/index.html')
        # print(file)
        # webbrowser.open('file://' + file)
        # webbrowser.open('https://www.youtube.com/watch?v=irpWmNmgAz4')
        self.dialogHelp.show()

    @classmethod
    def about_us(cls):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_create_plugin(cls):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Create Plugin")
        msgbox.setText(
            "Comming soon !!!!!!!!\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_plugin(cls):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help Plugin")
        msgbox.setText(
            "Comming soon !!!!!!!!\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev2.png'))
        msgbox.exec()

    @classmethod
    def help_moilApp(cls):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help !!")
        msgbox.setText(
            "Moildev-Apps\n\n"
            "Moildev-Apps is software to process fisheye "
            "image with the result panorama widget_controller and Anypoint"
            " widget_controller. \n\nThe panoramic widget_controller may present a horizontal"
            "widget_controller in a specific immersed environment to meet the"
            "common human visual perception, while the Anypoint"
            "widget_controller is an image that has been undistorted in a certain"
            "area according to the input coordinates."
            "\n\nMore reference about Moildev, contact us\n\n")
        msgbox.setIconPixmap(QtGui.QPixmap('images/moildev.png'))
        msgbox.exec()
