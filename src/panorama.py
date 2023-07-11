import numpy as np
from moilutils.moilutils import MoilUtils
from PyQt5 import QtWidgets


class Panorama(object):
    def __init__(self, Parent):
        """
        Panorama widget_controller controller
        Args:
            Parent (): The main class
        """
        self.parent = Parent
        self.rho = None
        self.moildev = None
        self.__pano_alpha_min = 10
        self.__pano_alpha_max = None

    def process_to_panorama(self):
        """
        Process to the panorama widget_controller.

        """
        if self.parent.image is not None:
            self.parent.anypoint.resetAlphaBeta()
            self.parent.buttonRecenter.setChecked(False)
            self.parent.buttonRecenter.setStyleSheet(
                "QPushButton{\n"
                "  border-color: #71D1BA;\n"
                "  border-width: 2px;        \n"
                "  border-style: solid;\n"
                "  border-radius: 5px;\n"
                "  background-color : rgb(238, 238, 236); }\n")
            if self.parent.type_camera:
                self.moildev = MoilUtils.connectToMoildev(self.parent.type_camera)
                self.__pano_alpha_max = self.moildev.camera_fov()/2
                self.parent.max_pano.setMaximum(self.__pano_alpha_max)
                self.__panorama()
                self.parent.show_percentage()
                self.parent.status_alpha.setText("Alpha: 0")
                self.parent.status_beta.setText("Beta: 0")
            else:
                QtWidgets.QMessageBox.information(self.parent.parent,
                                                  "Warning", "This image not support for this application. \n "
                                                             "Please contact developer!!")

    def __panorama(self):
        """
        Panorama function.

        """
        self.parent.normal_view = False
        self.parent.anypoint_view = False
        self.parent.panorama_view = True
        self.parent.angle = 0
        self.rho = self.moildev.get_rho_from_alpha(self.__pano_alpha_min)
        self.parent.frame_navigator.hide()
        self.parent.frame_panorama.show()
        mapX, mapY, = self.moildev.maps_panorama(
            self.__pano_alpha_min, self.__pano_alpha_max)
        np.save("./maps_pano/mapX.npy", mapX)
        np.save("./maps_pano/mapY.npy", mapY)
        self.parent.max_pano.setValue(self.__pano_alpha_max)
        self.parent.min_pano.setValue(self.__pano_alpha_min)
        self.parent.showToWindow()

    def change_panorama_fov(self):
        """
        Change the panorama widget_controller with change the field of widget_controller.

        """
        self.__pano_alpha_min = self.parent.min_pano.value()
        self.__pano_alpha_max = self.parent.max_pano.value()
        self.__panorama()
