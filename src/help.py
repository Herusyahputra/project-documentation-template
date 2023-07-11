from help_source.ui_help import Ui_Help
from help_source import MoilApp_help
import webbrowser
from PyQt5 import QtWidgets, QtGui
from moilutils import ResourceIcon


class Help(Ui_Help):
    def __init__(self, MainWindow, recentWindow):
        """
         >> Main window is the the inheritance from the main UI this program
         >> Recent window is the UI for this window.
         this make it possible to communication between this two UI
        """

        self.parent_win = MainWindow
        self.parent_dialog = recentWindow
        self.rs = ResourceIcon()

        self.setupUi(self.parent_dialog)
        self.eventButton()
        self.listWidget.setCurrentRow(0)
        self.selectItem()

    @classmethod
    def open_user_guide_moildev(cls):
        # file = os.path.realpath('./plugins/Thread_inspection/help/index.html')
        # print(file)
        # webbrowser.open('file://' + file)
        webbrowser.open('https://www.youtube.com/watch?v=irpWmNmgAz4')
        # self.dialogHelp.show()

    def about_us(self):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n")
        msgbox.setIconPixmap(QtGui.QPixmap.fromImage(self.rs.iconChessBox()))
        msgbox.exec()

    def help_create_plugin(self):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Create Plugin")
        msgbox.setText(
            "Comming soon !!!!!!!!\n")
        msgbox.setIconPixmap(QtGui.QPixmap.fromImage(self.rs.iconChessBox()))
        msgbox.exec()

    def help_plugin(self):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help Plugin")
        msgbox.setText(
            "Comming soon !!!!!!!!\n")
        msgbox.setIconPixmap(QtGui.QPixmap.fromImage(self.rs.iconChessBox()))
        msgbox.exec()

    def help_moilApp(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About MoilApps")
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
        msgbox.setIconPixmap(QtGui.QPixmap.fromImage(self.rs.iconChessBox()))
        msgbox.exec()

    def eventButton(self):
        self.listWidget.itemSelectionChanged.connect(self.selectItem)

    def selectItem(self):
        apps = self.listWidget.currentItem().text()
        if apps == 'MoilApp':
            self.moilapp()
        elif apps == "AnyPoint":
            self.anypoint()
        elif apps == "Panorama":
            self.panorama()
        elif apps == "Plugins/Add-ons":
            self.add_ons()
        elif apps == "Recenter Image":
            self.recenter_image()
        else:
            self.another()

    def moilapp(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">MoilApp</span></p>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">MoilApp is a fisheye image processing software developed by MOIL-Lab. This application is an implementation of Moildev SDK as a sophisticated method of processing fisheye images. The commonly used is to process fisheye image with the result panorama view and Anypoint view. This sophisticated methodology for image processing is very useful in a variety of applications that require high image quality and wide-angle FoV (Field of View).</p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The following picture is an explanation of the User Interface in the MoilApp Application.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/moilapp_release.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User Interface of MoilApp</p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600; text-decoration: underline;\">Explanation</span><span style=\" text-decoration: underline;\">:</span></p>\n"
            "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">MenuBar</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This is container stores various button</p>\n"
            "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">File</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\">File contains Load image, Load video, Open cam, Cam Parameter, Record Video, Save Image, and Exit    </p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">View</li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\">Rotate Left, rotate right, Zoom In and Zoom Out</p>\n"
            "<li style=\" font-weight:600;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Window<span style=\" font-weight:400;\">    </span></li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\">Window contains  Maximize and Minimize    </p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Apps</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\">Apps contains <span style=\" font-weight:600;\"> </span>Add, Open, Delete, Create and Help for Plugins</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Help</span></li></ul>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\">Help contains<span style=\" font-weight:600;\">  </span>About Apps, About Us, Accesibility, Release Note and Check for Update</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\"><br /></p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Name of Application</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This part will give information about app name </p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Source of Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The source button has three buttons, first and second to load Image and load Video from directory. The third button is to open the camera in real-time which can choose USB Cam or WebCam. </p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Rotate Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Rotate your image right and left 10 degree</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Zoom Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Zoom in or Zoom out your image and provide information of zoom ratio percentage </p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Saving Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Save Image and Record Video</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">PlugIns/ Add-Ons</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Plugins or Add-Ons will provide information, install, remove and open Add-Ons application</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Application Name/ Information  of Camera</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This part will first show the name of the MoilApp application but when open the image it will change to camera information on the image used</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">View Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">There are 3 view buttons, the first is Normal View which corresponds to the original image, Anypoint which point can see all sides of the image and Panorama which makes the image a panorama</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Help Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Help button will givr information about MoilApp and Moil-lab</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Clear Button</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Clear all process of observation image</p>\n"
            "<li style=\" font-weight:600;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Exstra Button</li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This button will show other tools that help in processing anypoint and panoramic images</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Result window / result frame</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Showing the resulting image after processing, this is the main image viewer </p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Image saved window / saved frame</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This will contain the image frame saved and allow to show it again in the result image viewer</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Video Controller</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This will contain some important tools for the video controller such as the previous button, play/pause button, skip button, stop button, slider time, and recent time viewer of the video</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Original Image window / original frame</span></li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Showing the original image frame and keep it to show the difference before and after processing</p>\n"
            "<li style=\" font-weight:600;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Alpha Beta Value</li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Showing value of alpha and beta degree for anypoint view</p>\n"
            "<li style=\" font-weight:600;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Back Button</li>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The back button will appear when using the zoom area by selecting the area you want to observaion</p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/back_button.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Back Button When Zoom Area</p>\n"
            "<li style=\" font-weight:600;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Recenter Button</li>\n"
            "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Recenter is useful for determining the center point of the image by changing the value of Image center X and image center Y. This button will appear when in normal view and panoramic view.</p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/recenter_image_bu.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Recenter Image</p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Recenter Image Result</span></li></ol>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The values of image center x and image center y will be calculated to be the center position of the image. the modified image will be displayed in this window. This window only show in panorama view</p></body></html>")

    def anypoint(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Anypoint View</span></p>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0x; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">This method converts the image plane coordinate to hemispherical coordinates, moves the optical axis to the specified zenithal (alpha) and azimuthal (beta) angle based on the coordinate given. the Anypoint view is an image that has been undistorted in a certain area according to the input coordinates.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/Hemisphere.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hemisphere coordinate system</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/zenital_azimut_com.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Left: Zenithal Angle (beta), Right: Azimuthal Angle (beta)</p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The image below is an anypoint mode. On the original frame, there is a square box with a curved line with the top color red and the left blue with the other side green. The result frame also has a similar line color, red, blue, and green. This line is intended to make it easier to understand the position of the image and will not affect the image.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/anypoint_com.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Anypoint View (Center)</p>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Below is an overview of the extra button in Anypoint view mode.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/axis_any.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Exstra Buttons For Anypoint</p>\n"
            "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:12px;\"><span style=\" font-weight:600;\">Fast View</span></li>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">MoilApp provides a feature to operate anypoint view with the fast view feature. You can directly choose which side of the image you want to observe. Some of the button options provided include:</p>\n"
            "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Center View</li>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Right View</li>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Left View</li>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Upper View</li>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bellow View</li></ul>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">In addition to using fast view you can also directly click on the frame on the original frame image so that the image in the result image frame will change based on the alpha and beta angles on the original frame.</p>\n"
            "<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Mode</span></li>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Anypoint view has 2 modes, where mode 1 is the result rotation from betaOffset degree rotation around the Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). Below is the example of anypoint result mode 1.</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/mode1_com.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Anypoint View Mode 1</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Whereas, for mode -2 the result rotation is theta Y degree rotation around the Y- axis(yaw) after thetaX degree rotation around the X-axis(pitch). With the results of the image of this process can be seen in the following image.</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/mode2_com.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Anypoint View Mode 2</p>\n"
            "<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Zoom</span></li></ol>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The zoom factor is useful in increasing the size of the image area to be observed. by default the zoom value is 4. the larger the zoom value, the smaller the FoV or closer to the object. the smaller the zoom value the FoV will be wider or will move away from the object.</p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The image below it will be clearer about what zoom is and how it affects the observation process. please pay attention to the picture of the box with red blue and green lines on the original image frame and the picture on the result image frame</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/any_zoom3.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zoom Value 3</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/anypoint/any_zoom14.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zoom Value 14</p></body></html>")

    def panorama(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Panorama View</span></p>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The panoramic view may present a horizontal view in a specific immersed environment to meet the common human visual perception. A panoramic view is like unfold the hemisphere image. </p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/pano/panorama.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pixel Mapping Diagram Panorama View</p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Left: Fisheye Image, Right: Panorama Plane</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Here, Figure above shows the fisheye image model, and shows the panoramic view\'s mapping plane. The horizontal axis in the panorama plane is the longitude and the vertical axis is the latitude of spherical coordinate. The maximum radius of longitude angle also called beta (β) is 360 degree and the latitude or alpha (α) is a half of Field of View (FoV) camera where in this study camera lens have FoV 220 degree. We set the alpha and beta is 0 then we calculate with our method formula then the fisheye image can be expanded to the desired panorama image.</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/pano/Exstra_button_pano.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Exstra Button For Panorama </p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The support button is useful for limiting the Fov you want to see. Fov values that can be changed are 10 degrees for the minimum and 110 degrees for the maximum. If you change this value then the panoramic image will be cropped automatically. For Recenter Image button will be explained in another topic. The picture below is an example of an image on the original image into a panoramic view.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/pano/pano_ori_com.png\" /></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Original View</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/pano/pano_release_com.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Panorama View</p></body></html>")

    def add_ons(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Plugins/Add-Ons</span></p>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Because the applications are very diverse, we implement a plugin framework so that users can select apps according to their needs. A plugin is a software component that adds a specific feature to an existing computer program. When a program supports plug-ins, it enables customization. A plugin architecture consists of two components: a core system and plug-in modules. </p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The main key design here is to allow adding additional features that are called plugins modules to our core system, providing extensibility, flexibility, and isolation to our application features. This will provide us with the ability to add, remove, and change the behavior of the application with little or no effect on the core system or other plug-in modules making our code very modular and extensible.</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/plug_architecture.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plugin Architecure</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The MoilApp application is designed to be able to implement this concept plugin, there is a special menu bar  named Apps and button container to control the plug-in application as shown below.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/plugin_release.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plugins Controller</p>\n"
            "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-weight:600;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add Plugins Application</li>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">You can add the application plugin that you have created by pressing the (+) button or menubar apps then select add application. System will open a file explorer dialog to select a plugin folder and please to select the folder of plugins program. If your application matches the format and was successfully added, then the plugin application will be available in the combobox like shown on figure below. </p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/plugin_add_release.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Add Plugin Application</p>\n"
            "<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Open Plugins Application</span></li>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">You can open a plugin that you have added by selecting it in the combo box and pressing the open plugins button. The example below is a multiple view plugin application for ADAS application.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/plugin_open_release.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Open Plugin Application</p>\n"
            "<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Delete Plugins Application</span></li></ol>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">If you want to delete the application plugins, you can do it by pressing the “delete” button in plugin controller container. This will open a dialog to confirm that you are sure to remove this app. If the application is deleted, then the application is no longer available in the application combo box list.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/plugin_delete_release.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Delete Plugin Application</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p></body></html>")

    def recenter_image(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Recenter Image</span></p>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Recenter image was for making the center point exactly at the position of the image you want to monitor. Usually, to get the middle value we do it manually with hardware, whereas now we only need to adjust it digitally. recenter image only exists in normal view and also in panoramic view. </p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The picture below is the recenter image in normal view. Recenter values obtained are X = 1298 and Y = 966. For a more detailed explanation to make it easier to understand, see the example in the panoramic view.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/recenter/reventer_normal.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Original Image on Normal View</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><br /></p>\n"
            "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Normal Panorama</span></li>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">In Normal Panorama, the values for center X and center Y are by default based on the observed image. the value of center X is 1298 and center Y = 966. It looks like an irregularity or hollowness on the horizontal axis. that way, to get a good panorama is to change the value of center x and center y.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/recenter/recenter_pano_normal.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Normal Panorma</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X = 1298, Y = 966</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:2; text-indent:0px;\"><br /></p>\n"
            "<li align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Recenter Image Panorama</span></li></ol>\n"
            "<hr width=\"90%\"/>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Previously in normal panorama, the value of center X was 1298 and center Y = 966. Then we changed it to X = 1299 and Y = 973. with a change in the center value, the resulting panoramic image will also be different and it can be seen that the results are better because the hollow at the top is no longer there.</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/recenter/recenter_pano_after.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Panorama Recenter Image</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X = 1299, Y = 973</p></body></html>")

    def multiple_view(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Multiple View</span></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Multiple View</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Multiple views will process images into 6 views at once so that it can facilitate the observation process and several other things such as the ADAS project.</p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Original View Image</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Original view will only display the image according to the original image as shown below</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/multiori.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Original View Image</p>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Six View Image</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Six view will provide a view at the same time that includes:</p>\n"
            "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Left View</li>\n"
            "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Center View</li>\n"
            "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Right View</li>\n"
            "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Left BottomView</li>\n"
            "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Bottom View</li>\n"
            "<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Right Bottom View</li></ol>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">You can also select the view directly by selecting the number or clicking the image in the window</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/multipleview2.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Six AnyPoint View</p></body></html>")

    def axis_controller(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Axis Controller</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">Axis controller is a tool controller plugin that is useful in moving the camera that will take pictures or videos. </p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">User Interface</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">User interface and functions are explained bellow:</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/axis.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User Interface of Axis Controller</p>\n"
            "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Connect</li>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Connect your application to device</p>\n"
            "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Disconnect</li>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Disconnect application with device</p>\n"
            "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Help</li>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Give information about Axis Controller Add-Ons</p>\n"
            "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reset All</li>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Reset position become 0 and speed becamo 500 RPM</p>\n"
            "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Backward</li>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Backward 20 mm</p>\n"
            "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Forward</li>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Forward 20 mm</p>\n"
            "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Absolute Move</li></ul>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Window contains  Maximize and Minimize</p>\n"
            "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\"><span style=\" font-weight:600;\">Device</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The devices used are also specifically as in the following picture. These devices are prepared by MOIL-Lab. In this device consists of a specimen, a camera controlled by a raspberry pi, a power supply and a usb connected to the user labtop</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/axis.jpg\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Device to Capture Image</p></body></html>")

    def object_measurement(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Object Measurement</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">These add-ons allow us to <span style=\" font-weight:600;\">measure</span> an object size from images. It takes two cameras or two images to be able to use this feature. By determining the <span style=\" font-weight:600;\">points</span> to be measured from the two images, we can determine the size of the object. The user interface of this application is as shown in the following picture:</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Moilapp/Webp.net-resizeimage.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Measuring Object</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

    def another(self):
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Waree\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Moil-Lab</span></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Omnidirectional Imaging &amp; Surveillance Lab</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ming Chi University of Technology</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">|</p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if you have any questions please contact us</p></body></html>")
