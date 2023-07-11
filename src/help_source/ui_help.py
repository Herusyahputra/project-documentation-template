# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moilApp_release.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(1053, 700)
        Help.setMinimumSize(QtCore.QSize(1050, 700))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Help)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(Help)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                   "background-color: #71D1BA;\n"
                                   "border-radius: 10px;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea.setMinimumSize(QtCore.QSize(700, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 680))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                 "background-color: #71D1BA;\n"
                                 "border-radius: 10px;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setSearchPaths([])
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "MoilApp Help"))
        self.label_2.setText(_translate("Help", "Index"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Help", "MoilApp"))
        item = self.listWidget.item(1)
        item.setText(_translate("Help", "AnyPoint"))
        item = self.listWidget.item(2)
        item.setText(_translate("Help", "Panorama"))
        item = self.listWidget.item(3)
        item.setText(_translate("Help", "Plugins/Add-ons"))
        # item = self.listWidget.item(4)
        # item.setText(_translate("Help", "Recenter Image"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Help", "MoilApp Assistant"))
        self.textBrowser.setHtml(_translate("Help",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">MoilApp</span></p>\n"
                                            "<hr width=\"90%\"/>\n"
                                            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">MoilApp is a fisheye image processing software developed by MOIL-Lab. This application is an implementation of Moildev SDK as a sophisticated method of processing fisheye images. The commonly used is to process fisheye image with the result panorama view and Anypoint view. This sophisticated methodology for image processing is very useful in a variety of applications that require high image quality and wide-angle FoV (Field of View). For more details about MoilDev SDK you can click this <a href=\"https://github.com/MoilOrg/moildev\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub link</span></a> or <a href=\"https://pypi.org/project/Moildev/\"><span style=\" text-decoration: underline; color:#0000ff;\">PyPi link</span></a> to implement it in python programs.</p>\n"
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
                                            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:24px;\">The values of image center x and image center y will be calculated to be the center position of the image. the modified image will be displayed in this window.</p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Help = QtWidgets.QWidget()
    ui = Ui_Help()
    ui.setupUi(Help)
    Help.show()
    sys.exit(app.exec_())
