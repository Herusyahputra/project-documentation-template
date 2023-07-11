import math
import cv2
from ShowResult import ShowImageResult


class SetupCenterCamera:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButtonUi()

    def connectToButtonUi(self):
        self.parent.ui.pushButtonFindCenter.clicked.connect(self.set_center)
        self.parent.ui.pushButtonRaidusCircle.clicked.connect(self.onclick_set_radius)

    def set_center(self):
        self.cx = int(self.parent.ui.lineEdit_Icx.text())
        self.cy = int(self.parent.ui.lineEdit_Icy.text())

    def onclick_set_radius(self):
        self.r1 = int(self.parent.ui.lineEdit_radiusCircle1.text())
        self.r2 = int(self.parent.ui.lineEdit_radiusCircle2.text())
        self.r3 = int(self.parent.ui.lineEdit_radiusCircle3.text())
        self.r4 = int(self.parent.ui.lineEdit_radiusCircle4.text())
        self.r5 = int(self.parent.ui.lineEdit_radiusCircle5.text())

    def initRadiusCircle(self):
        """
        initial for setup the center
        """
        self.r1 = int(self.parent.ui.lineEdit_radiusCircle1.text())
        self.r2 = int(self.parent.ui.lineEdit_radiusCircle2.text())
        self.r3 = int(self.parent.ui.lineEdit_radiusCircle3.text())
        self.r4 = int(self.parent.ui.lineEdit_radiusCircle4.text())
        self.r5 = int(self.parent.ui.lineEdit_radiusCircle5.text())

    def find_center(self):
        """
        this function is for setting the center of the camera
        """
        if self.parent.image is None:
            pass
        else:
            self.parent.ui.frame_7.setDisabled(False)
            image = self.parent.image.copy()
            h, w = image.shape[:2]
            b = self.cy
            a = round(b / math.sin(45))
            cv2.circle(image, (self.cx, self.cy), self.r1, (255, 0, 4), 4, -1)
            cv2.circle(image, (self.cx, self.cy), self.r2, (255, 0, 4), 4, -1)
            cv2.circle(image, (self.cx, self.cy), self.r3, (255, 0, 4), 4, -1)
            cv2.circle(image, (self.cx, self.cy), self.r4, (255, 0, 4), 4, -1)
            cv2.circle(image, (self.cx, self.cy), self.r5, (255, 0, 4), 4, -1)
            cv2.line(image, (0, self.cy), (self.cx, self.cy), (255, 0, 4), 3)
            cv2.line(image, (self.cx, self.cy), (w, self.cy), (255, 0, 4), 3)
            cv2.line(image, (self.cx, 0), (self.cx, self.cy), (255, 0, 4), 3)
            cv2.line(image, (self.cx, self.cy), (self.cx, h), (255, 0, 4), 3)
            # line 45 degree
            cv2.line(image, (self.cx + a, 0), (self.cx, self.cy), (255, 0, 4), 3)
            cv2.line(image, (self.cx, self.cy), (self.cx - a, h), (255, 0, 4), 3)
            cv2.line(image, (self.cx - a, 0), (self.cx, self.cy), (255, 0, 4), 3)
            cv2.line(image, (self.cx, self.cy), (self.cx + a, h), (255, 0, 4), 3)

            # show the original image and result image to the frame
            self.show.showOriginalImage(self.parent.image)
            self.show.showResult(image)
