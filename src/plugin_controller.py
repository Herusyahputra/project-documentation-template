import shutil
import os
from pathlib import Path
from PyQt5 import QtWidgets, QtGui, QtCore
from moilutils.moilutils import MoilUtils
from plugin_collection import PluginCollection


class PluginController(object):
    def __init__(self, main_controller):
        super(PluginController, self).__init__()
        self.main_controller = main_controller
        self.plugin_win = None
        self.index = None
        # path_file = os.path.dirname(os.path.realpath(__file__))
        self.plugins = PluginCollection("plugins")
        self.init_plugin_win()
        self.main_controller.comboBox.addItems(self.plugins.name_application)

        # action from menubar menu apps
        self.main_controller.actionAdd_Apps.triggered.connect(self.add_application)
        self.main_controller.actionDelete_Apps.triggered.connect(self.action_delete_apps)
        self.main_controller.actionOpen_Apps.triggered.connect(self.action_open_apps)
        self.main_controller.btn_add_apps.clicked.connect(self.add_application)
        self.main_controller.btn_open_app.clicked.connect(self.btn_open_apps)
        self.main_controller.btn_delete_app.clicked.connect(self.btn_delete_apps)

    def init_plugin_win(self):
        self.plugin_win = []
        for i in range(len(self.plugins.name_application)):
            self.plugin_win.append(QtWidgets.QMainWindow())

    def btn_open_apps(self):
        index = self.main_controller.comboBox.currentIndex()
        self.open_application(index)

    def action_open_apps(self):
        self.dialog_apps()
        if self.index is not None:
            self.open_application(self.index)

    def open_application(self, index):
        """
        Open application depend on selected application available on comboBox.

        Returns:
            Will hide the main apps window and show the selection application.
        """
        self.main_controller.open_plugin = True
        self.init_plugin_win()
        if index == -1:
            QtWidgets.QMessageBox.warning(None, "Warning", " No Installation Plugin, please add first !!")
        else:
            self.plugins.application(self.plugin_win[index], index)

    def btn_delete_apps(self):
        index = self.main_controller.comboBox.currentIndex()
        self.delete_apps(index)

    def action_delete_apps(self):
        self.dialog_apps()
        if self.index is not None:
            self.delete_apps(self.index)

    def dialog_apps(self):
        """
        Select the camera type prompt.

        """
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.setWindowTitle("Select Plugin")
        self.Dialog.resize(240, 120)
        buttonBox = QtWidgets.QDialogButtonBox(self.Dialog)
        buttonBox.setGeometry(QtCore.QRect(20, 80, 200, 32))
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        self.combobox_plugins = QtWidgets.QComboBox(self.Dialog)
        self.combobox_plugins.setGeometry(QtCore.QRect(20, 40, 200, 30))
        self.combobox_plugins.setObjectName("comboBox")
        self.combobox_plugins.addItems(self.plugins.name_application)
        label = QtWidgets.QLabel(self.Dialog)
        label.setGeometry(QtCore.QRect(10, 10, 220, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(13)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        label.setText("A Plugin wants to open!!")

        buttonBox.accepted.connect(self.dialog_accept)
        buttonBox.rejected.connect(self.dialog_reject)
        self.Dialog.exec_()

    def dialog_accept(self):
        self.index = self.combobox_plugins.currentIndex()
        self.Dialog.close()

    def dialog_reject(self):
        self.index = None
        self.Dialog.close()

    def delete_apps(self, index):
        """
        Delete selected application from the list.

        Returns:
            None.
        """

        if index == -1:
            QtWidgets.QMessageBox.warning(None, "Warning", " No Installation Plugin Application!!")
        else:
            name = self.plugins.name_application[index]
            path = self.plugins.path_folder[index]
            path = path.split(".")[1]
            path = "./plugins/" + path
            reply = QtWidgets.QMessageBox.question(
                self.main_controller.parent,
                'Message',
                "Are you sure want to delete \n" +
                name +
                " application ?\n",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                shutil.rmtree(path, ignore_errors=True)
                self.plugins.reload_plugins()
                newList = self.plugins.name_application
                self.main_controller.comboBox.clear()
                self.main_controller.comboBox.addItems(newList)
                self.init_plugin_win()
                QtWidgets.QMessageBox.information(None, "Information", "Plugins was successfully deleted !!")

    def add_application(self):
        """
        Add application plugin collection.

        Returns:
            None.
        """
        options = QtWidgets.QFileDialog.DontUseNativeDialog
        dir_plugin = QtWidgets.QFileDialog.getExistingDirectory(
            self.main_controller.parent, 'Select Application Folder', "../plugin_store", options)
        if dir_plugin:
            original = dir_plugin
            name_plug = os.path.basename(os.path.normpath(original))
            target = 'plugins/'
            name_exist = Path(target + name_plug)
            if name_exist.exists():
                QtWidgets.QMessageBox.warning(None, "Warning !!", "Plugins already exist!!")
            else:
                listApp = self.plugins.name_application
                MoilUtils.copyDirectory(original, target)
                self.plugins.reload_plugins()
                newList = self.plugins.name_application
                name = [item for item in newList if item not in listApp]
                index = newList.index(self.listToString(name))
                self.main_controller.comboBox.clear()
                self.main_controller.comboBox.addItems(newList)
                self.main_controller.comboBox.setCurrentIndex(index)
                self.init_plugin_win()
                QtWidgets.QMessageBox.information(None, "Information", "Plugins was successfully added!!")

    @classmethod
    def listToString(cls, listIn):
        """
        Initialize an empty string
        Args:
            listIn (): List input

        Returns:

        """
        str1 = " "
        return str1.join(listIn)
