from moilutils.moilutils import MoilUtils
from PyQt5 import QtWidgets


class Anypoint(object):
    def __init__(self, Parent):
        """
        The class for anypoint process.

        Args:
            Parent (): The Main class of this application
        """
        self.parent = Parent
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.anypoint_mode = 1
        self.moildev = None
        self.parent.radio_btn_mode_1.setChecked(True)

    def set_param_any(self):
        self.alpha = float(self.parent.lineedit_alpha_2.text())
        self.beta = float(self.parent.lineedit_beta_2.text())
        self.zoom_any = float(self.parent.anypoint_zoom_2.text())
        self.anyPo()

    def writeAlphaBeta(self):
        self.parent.lineedit_alpha_2.setValue(self.alpha)
        self.parent.lineedit_beta_2.setValue(self.beta)
        self.parent.anypoint_zoom_2.setValue(self.zoom_any)

    def process_to_anypoint(self):
        """
        This function is to process the image and show on anypoint mode.

        """
        if self.parent.image is not None:
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
                self.parent.point = (round(self.moildev.icx()), round(self.moildev.icy()))
                self.resetAlphaBeta()
                self.anypoint()
                self.parent.status_alpha.setText("Alpha: %.1f" % self.parent.anypoint.alpha)
                self.parent.status_beta.setText("Beta: %.1f" % self.parent.anypoint.beta)
                self.parent.show_percentage()
            else:
                QtWidgets.QMessageBox.information(self.parent.parent,
                                                  "Warning", "This image not support for this application. \n "
                                                             "Please contact developer!!")

    def anypoint(self):
        """
        Anypoint widget_controller algorithm.

        """
        self.parent.normal_view = False
        self.parent.panorama_view = False
        self.parent.anypoint_view = True
        self.parent.angle = 0
        self.parent.frame_navigator.show()
        self.parent.frame_panorama.hide()
        self.parent.mapX, self.parent.mapY, = self.moildev.maps_anypoint(
            self.alpha, self.beta, self.zoom_any, self.anypoint_mode)
        self.parent.showToWindow()
        self.writeAlphaBeta()

    def anyPo(self):
        self.parent.mapX, self.parent.mapY, = self.parent.moildev.maps_anypoint(
            round(self.alpha, 2), round(self.beta, 2), self.zoom_any, self.anypoint_mode)
        self.parent.showToWindow()
        self.writeAlphaBeta()

    def anypoint_mode_1(self):
        """
        Execute the anypoint process mode 1.

        Returns:
            None.
        """
        self.anypoint_mode = 1
        self.resetAlphaBeta()
        self.process_to_anypoint()

    def anypoint_mode_2(self):
        """
        Execute the anypoint process mode 2.

        Returns:
            None.
        """
        self.anypoint_mode = 2
        self.resetAlphaBeta()
        self.process_to_anypoint()

    def resetAlphaBeta(self):
        """
        The method for reset alpha, beta, zoom, and angle.

        Returns:
            None.
        """
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.writeAlphaBeta()
        if self.parent.moildev is not None:
            self.parent.point = (round(self.parent.moildev.icx()), round(self.parent.moildev.icy()))

    def up(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 75
            self.beta = 0
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 50
            self.beta = 0
        self.anypoint()

    def left(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = -90
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = -75
        self.anypoint()

    def center(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = (round(self.parent.moildev.getIcx()), round(self.parent.moildev.getIcy()))
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 0
            self.beta = 0
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 0
        self.anypoint()

    def right(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 90
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 65
        self.anypoint()

    def down(self):
        """
        The method showing anypoint widget_controller in specific area.
        """
        self.parent.point = None
        if self.parent.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 180
        elif self.parent.radio_btn_mode_2.isChecked():
            self.alpha = -65
            self.beta = 0
        self.anypoint()
