from PyQt5 import QtCore, QtGui
import cv2


class Set_RatioImage:
    def __init__(self, MainWindow):
        self.parent = MainWindow

    def init_ori_ratio(self):
        """
        calculate the ratio of original Image
        """
        h = self.parent.ui.windowOri.height()
        w = self.parent.ui.windowOri.width()
        height, width = self.parent.image.shape[:2]
        ratio_x = width / w
        ratio_y = height / h
        center = (round((w / 2) * ratio_x), round((h / 2) * ratio_y))
        return ratio_x, ratio_y, center

    def ratioORi(self, imageOri):
        h, w = imageOri.shape[:2]
        r = 400 / float(w)
        hi = round(h * r)
        self.parent.ui.windowOri.setMinimumSize(QtCore.QSize(400, hi))
        self.parent.ui.labelImagerecenter.setMinimumSize(QtCore.QSize(400, hi))
        img_ori = cv2.resize(imageOri, (400, hi), interpolation=cv2.INTER_AREA)
        return img_ori

    # def ratio3D_Measurement(self, image_1, image_2, width=600):
    #     h, w = image_1.shape[:2]
    #     r = width / float(w)
    #     hi = round(h * r)
    #     self.parent.ui.label3Dimage1.setMaximumSize(QtCore.QSize(width, hi))
    #     self.parent.ui.label3Dimage2.setMaximumSize(QtCore.QSize(width, hi))
    #     img_result_1 = cv2.resize(image_1, (width, hi), interpolation=cv2.INTER_AREA)
    #     img_result_2 = cv2.resize(image_2, (width, hi), interpolation=cv2.INTER_AREA)
    #
    #     return img_result_1, img_result_2

    def ratioImage(self, imageOri, widthSize):
        h, w = imageOri.shape[:2]
        r = widthSize / float(w)
        hi = round(h * r)
        img_ori = cv2.resize(imageOri, (widthSize, hi), interpolation=cv2.INTER_AREA)
        return img_ori

    def ratioResult(self, imageResult, widthSize):
        h, w = imageResult.shape[:2]
        r = widthSize / float(w)
        hi2 = round(h * r)

        self.parent.ui.windowResult.setGeometry(QtCore.QRect(10, 0, widthSize, hi2))
        self.parent.ui.PlussIcon.setGeometry(QtCore.QRect(10, 10, widthSize, hi2))
        blue = QtGui.QPixmap(widthSize, hi2)
        blue.fill(QtCore.Qt.transparent)
        p = QtGui.QPainter(blue)
        pen = QtGui.QPen(QtGui.QBrush(QtGui.QColor(0, 255, 0)), 3)
        p.setPen(pen)
        p.drawLine(round((widthSize / 2) - 10), round(hi2 / 2), round((widthSize / 2) + 10), round(hi2 / 2))
        p.drawLine(round(widthSize / 2), round((hi2 / 2) - 10), round(widthSize / 2), round((hi2 / 2) + 10))
        p.end()
        self.parent.ui.PlussIcon.setPixmap(blue)
        img_result = cv2.resize(imageResult, (widthSize, hi2), interpolation=cv2.INTER_AREA)
        return img_result
