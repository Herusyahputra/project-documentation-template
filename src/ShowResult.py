import cv2
from PyQt5 import QtGui, QtCore
from RatioImage import Set_RatioImage


def Rotate(src, angle, center=None, scale=1.0):
    """Turn an image in a clockwise or counterclockwise direction.

    Args:
        src: original image
        angle: the value angle for turn the image
        center: determine the specific coordinate to rotate image
        scale: scale image

    Returns:
        dst image: rotated image

    """
    h, w = src.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(src, M, (w, h))
    return rotated


class ShowImageResult:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.ratio = Set_RatioImage(self.parent)

    def showInRecenterLabel(self, image):
        annotate_image = self.ratio.ratioORi(image)
        my_label3 = self.parent.ui.labelImagerecenter
        annotate_image = QtGui.QImage(annotate_image.data, annotate_image.shape[1], annotate_image.shape[0],
                                      QtGui.QImage.Format_RGB888).rgbSwapped()
        my_label3.setPixmap(QtGui.QPixmap.fromImage(annotate_image))

    def showOriginalImage(self, imageOri):
        """
        showing the original image
        """
        imageOriginal = self.ratio.ratioORi(imageOri)
        image = QtGui.QImage(imageOriginal.data, imageOriginal.shape[1], imageOriginal.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        image = QtGui.QPixmap.fromImage(image)
        self.parent.ui.windowOri.setPixmap(image)

    def showPanoAnyImage(self, angle=0):
        """
        This function is to select the ratio of image before display on the main window user interface
        """
        self.parent.ui.windowResult.setMinimumSize(QtCore.QSize(self.parent.width_img, 0))
        self.parent.anypoint_Image = self.parent.image.copy()
        self.parent.panorama_Image = self.parent.image.copy()
        # if self.parent.ui.comboBox.currentIndex() == 0:
        if self.parent.ui.checkPanorama.isChecked():
            if self.parent.ui.checkBox_ShowRecenterImage_2.isChecked() or self.parent.ui.checkPanoramaAuto.isChecked():
                self.resultImage = cv2.remap(self.parent.revImage, self.parent.mapX, self.parent.mapY,
                                             cv2.INTER_CUBIC)
            else:
                self.resultImage = cv2.remap(self.parent.panorama_Image, self.parent.mapX, self.parent.mapY,
                                             cv2.INTER_CUBIC)
            # print(self.parent.mapX)
            # print(self.parent.ratio)

            self.resultImage_view = self.ratio.ratioResult(self.resultImage, self.parent.width_img)

        elif self.parent.ui.checkAnypoint.isChecked():
            self.resultImage = cv2.remap(self.parent.anypoint_Image, self.parent.mapX, self.parent.mapY,
                                         cv2.INTER_CUBIC)

            self.resultImage = Rotate(self.resultImage, angle)
            self.resultImage_view = self.ratio.ratioResult(self.resultImage, self.parent.width_img)

        else:
            self.resultImage_view = self.ratio.ratioResult(self.parent.image, self.parent.width_img)

        image = QtGui.QImage(self.resultImage_view.data, self.resultImage_view.shape[1], self.resultImage_view.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        image = QtGui.QPixmap.fromImage(image)
        self.parent.ui.windowResult.setPixmap(image)

    def showResult(self, image):
        """
        this is for showing result on demo moildev library application
        """
        self.parent.ui.windowResult.setMinimumSize(QtCore.QSize(self.parent.width_img, 0))
        resultImage = self.ratio.ratioResult(image, self.parent.width_img)
        # self.view_result(self.resultImage_view)
        image = QtGui.QImage(resultImage.data, resultImage.shape[1], resultImage.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        image = QtGui.QPixmap.fromImage(image)
        self.parent.ui.windowResult.setPixmap(image)

    def display_3D(self, image_1, image_2):
        lab_image_1 = self.parent.ui.label3Dimage1
        image_1 = QtGui.QImage(image_1.data, image_1.shape[1], image_1.shape[0],
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        image_1 = QtGui.QPixmap.fromImage(image_1)
        lab_image_1.setPixmap(image_1)

        lab_image_2 = self.parent.ui.label3Dimage2
        image_2 = QtGui.QImage(image_2.data, image_2.shape[1], image_2.shape[0],
                               QtGui.QImage.Format_RGB888).rgbSwapped()
        image_2 = QtGui.QPixmap.fromImage(image_2)
        lab_image_2.setPixmap(image_2)

    def show_development(self):
        self.parent.ui.PlussIcon.hide()
        font = QtGui.QFont()
        font.setPointSize(20)
        self.parent.ui.windowResult.setFont(font)
        self.parent.ui.windowResult.setAlignment(QtCore.Qt.AlignCenter)
        if self.parent.ui.comboBox.currentIndex() == 8:
            self.parent.ui.windowResult.setText(" 3D Reconstruction Application Still in Development")

        elif self.parent.ui.comboBox.currentIndex() == 9:
            self.parent.ui.windowResult.setText(" Visual Odometry Application Still in Development")

        else:
            self.parent.ui.windowResult.setText("Application Still in Development")
