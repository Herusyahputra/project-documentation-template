from ShowResult import ShowImageResult
import cv2
from PyQt5 import QtCore, QtGui
from Utils import corner_detect, get_corner_list, draw_corners, distance


class Measurement:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.clicked_time_l = 0
        self.clicked_time_r = 0
        self.coor_1 = None
        self.coor_2 = None
        self.connectToButtonUi()

    def connectToButtonUi(self):
        self.parent.ui.checkBox_2.clicked.connect(self.show_corner_detection)
        self.parent.ui.label3Dimage1.mousePressEvent = self.mousePressEvent_image_1
        self.parent.ui.label3Dimage2.mousePressEvent = self.mousePressEvent_image_2
        self.parent.ui.ClearBtn.clicked.connect(self.clear)
        self.parent.ui.CalculateBtn.clicked.connect(self.calculate)

    def corner_detection(self, sigma=3, threshold=0.01):
        """
        this function is for find the corner for each box on the image
        """
        if self.parent.image_1 is None:
            pass
        else:
            self.parent.ui.frame_2.setDisabled(False)
            self.img_result_1 = self.parent.img_result_1.copy()
            self.h, self.w = self.parent.image_1.shape[:2]
            self.img_result_2 = self.parent.img_result_2.copy()
            # convert rgb image to gray for image 1
            self.gray_1 = cv2.cvtColor(self.parent.img_result_1, cv2.COLOR_BGR2GRAY)
            corner = corner_detect(self.gray_1, sigma, threshold)
            self.coor_1 = get_corner_list(corner)

            # convert rgb image to gray for image 2
            self.gray_2 = cv2.cvtColor(self.img_result_2, cv2.COLOR_BGR2GRAY)
            corner = corner_detect(self.gray_2, sigma, threshold)
            self.coor_2 = get_corner_list(corner)
            self.ratioLabel()
            self.show.display_3D(self.img_result_1, self.parent.img_result_2)

    def show_corner_detection(self):
        if self.parent.ui.checkBox_2.isChecked():
            self.img_result_1 = draw_corners(self.coor_1, self.parent.img_result_1.copy())
            self.img_result_2 = draw_corners(self.coor_2, self.parent.img_result_2.copy())
        else:
            self.img_result_1 = self.parent.img_result_1.copy()
            self.img_result_2 = self.parent.img_result_2.copy()
        self.show.display_3D(self.img_result_1, self.img_result_2)

    def clear(self):
        self.img_result_1 = self.parent.img_result_1.copy()
        self.img_result_2 = self.parent.img_result_2.copy()
        self.show.display_3D(self.img_result_1, self.img_result_2)

    def calculate(self):
        self.parent.ui.statusMessage.setText("Function still on Development")

    def ratioLabel(self):
        label_w_1 = self.parent.ui.label3Dimage1.width()
        label_h_1 = self.parent.ui.label3Dimage1.height()
        self.ratio_x_1 = self.w / label_w_1
        self.ratio_y_1 = self.h / label_h_1
        label_w_2 = self.parent.ui.label3Dimage2.width()
        label_h_2 = self.parent.ui.label3Dimage2.height()
        self.ratio_x_2 = self.w / label_w_2
        self.ratio_y_2 = self.h / label_h_2

    def mousePressEvent_image_1(self, e):
        """ Get the position coordinate from mouse event"""
        if e.button() == QtCore.Qt.LeftButton:
            if self.clicked_time_l == 0:
                self.currPos = e.pos()
                self.pos_x = round(e.x())
                self.pos_y = round(e.y())
                pos = '{},{}'.format(self.pos_y, self.pos_x)
                pos = tuple(map(int, pos.split(',')))
                nearest = min(self.coor_1, key=lambda x: distance(x, pos))
                self.point_l_1 = (list(nearest)[1], list(nearest)[0])
                cv2.circle(self.img_result_1, self.point_l_1, 3, (0, 0, 255), -1)
                coor_y = list(nearest)[0] * self.ratio_y_1
                coor_x = list(nearest)[1] * self.ratio_x_1
                point = (round(coor_y), round(coor_x))
                self.parent.ui.label_22.setText(str(point))
                self.show.display_3D(self.img_result_1, self.img_result_2)
                self.clicked_time_l = 1

            elif self.clicked_time_l == 1:
                self.currPos = e.pos()
                self.pos_x = round(e.x())
                self.pos_y = round(e.y())
                pos = '{},{}'.format(self.pos_y, self.pos_x)
                pos = tuple(map(int, pos.split(',')))
                nearest = min(self.coor_1, key=lambda x: distance(x, pos))
                self.point_l_2 = (list(nearest)[1], list(nearest)[0])
                cv2.circle(self.img_result_1, self.point_l_2, 3, (0, 0, 255), -1)
                cv2.line(self.img_result_1, self.point_l_1, self.point_l_2, (0, 0, 255), 1)
                coor_y = list(nearest)[0] * self.ratio_y_1
                coor_x = list(nearest)[1] * self.ratio_x_1
                point = (round(coor_y), round(coor_x))
                self.parent.ui.label_6.setText(str(point))
                self.show.display_3D(self.img_result_1, self.img_result_2)
                self.clicked_time_l = 0

            else:
                print("No Left Image !!!")

    def mousePressEvent_image_2(self, e):
        """ Get the position coordinate from mouse event"""
        if e.button() == QtCore.Qt.LeftButton:
            if self.clicked_time_r == 0:
                print("11111111111111")
                self.currPos = e.pos()
                self.pos_x = round(e.x())
                self.pos_y = round(e.y())
                pos = '{},{}'.format(self.pos_y, self.pos_x)
                print(pos)
                pos = tuple(map(int, pos.split(',')))
                nearest = min(self.coor_2, key=lambda x: distance(x, pos))
                self.point_r_1 = (list(nearest)[1], list(nearest)[0])
                cv2.circle(self.img_result_2, self.point_r_1, 3, (0, 0, 255), -1)
                coor_y = list(nearest)[0] * self.ratio_y_2
                coor_x = list(nearest)[1] * self.ratio_x_2
                point = (round(coor_y), round(coor_x))
                self.parent.ui.label_23.setText(str(point))
                self.show.display_3D(self.img_result_1, self.img_result_2)

                self.clicked_time_r = 1

            elif self.clicked_time_r == 1:
                self.currPos = e.pos()
                self.pos_x = round(e.x())
                self.pos_y = round(e.y())
                pos = '{},{}'.format(self.pos_y, self.pos_x)
                pos = tuple(map(int, pos.split(',')))
                print(pos)
                nearest = min(self.coor_2, key=lambda x: distance(x, pos))
                self.point_r_2 = (list(nearest)[1], list(nearest)[0])
                cv2.circle(self.img_result_2, self.point_r_2, 3, (0, 0, 255), -1)
                cv2.line(self.img_result_2, self.point_r_1, self.point_r_2, (0, 0, 255), 1)
                coor_y = list(nearest)[0] * self.ratio_y_2
                coor_x = list(nearest)[1] * self.ratio_x_2
                point = (round(coor_y), round(coor_x))
                self.parent.ui.label_7.setText(str(point))
                self.show.display_3D(self.img_result_1, self.img_result_2)

                self.clicked_time_r = 0

            else:
                print("No Left Image !!!")

    # def loadImage_R(self):
    #     if self.parent.img_file_path_r:
    #         self.pixmap_r = QtGui.QPixmap(self.parent.img_file_path_r)
