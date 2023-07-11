from Utils import drawPoint
from ShowResult import ShowImageResult
import numpy as np
import cv2


class AnyPoint:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButton()

    def connectToButton(self):
        self.parent.ui.pushButtonAnypoint.clicked.connect(self.set_anypoint)
        self.parent.ui.checkAnypoint.clicked.connect(self.onclickAnypoint)
        self.parent.ui.radioAnypointM1.clicked.connect(self.anypoint_mode_1)
        self.parent.ui.radioAnypointM2.clicked.connect(self.anypoint_mode_2)
        self.parent.ui.spinBox_zoom.valueChanged.connect(self.zoomValue)

    def zoomValue(self):
        self.parent.zoom = self.parent.ui.spinBox_zoom.value()
        self.anypoint_view()

    def resetAlphaBeta(self):
        self.parent.alpha = 0
        self.parent.beta = 0
        self.parent.zoom = 4
        self.parent.angle = 0
        if self.parent.image is None:
            self.parent.coor = None
        else:
            self.parent.coor = self.parent.center

    def onclickAnypoint(self):
        if self.parent.ui.radioAnypointM1.isChecked():
            self.anypoint_mode_1()
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.anypoint_mode_2()

    def anypoint_view(self):
        if self.parent.image is None:
            pass
        else:
            image = self.parent.image.copy()
            if self.parent.ui.checkAnypoint.isChecked():
                self.parent.ui.checkPanorama.setChecked(False)
                self.parent.ui.frame_4.setDisabled(False)
                self.parent.ui.frame_5.setDisabled(True)
                self.alpha = self.parent.alpha
                self.beta = self.parent.beta
                self.zoom = self.parent.zoom

                if self.parent.ui.radioAnypointM1.isChecked():
                    self.parent.mapX, self.parent.mapY = self.parent.moildev.getAnypointMaps(self.alpha, self.beta, self.zoom)

                elif self.parent.ui.radioAnypointM2.isChecked():
                    self.parent.mapX, self.parent.mapY = self.parent.moildev.getAnypointMaps(self.alpha, self.beta,
                                                                                             self.zoom, 2)

                self.showPolygon()
                self.show.showPanoAnyImage(self.parent.angle)
                self.updateParamAnypoint()

            else:
                self.parent.ui.frame_4.setDisabled(True)
                self.parent.ui.frame_5.setDisabled(True)
                self.show.showOriginalImage(image)
                self.show.showResult(image)

    def showPolygon(self):
        image = self.parent.image.copy()
        image = self.drawPolygon(image, self.parent.mapX, self.parent.mapY)
        image = drawPoint(image, self.parent.imageHeight, self.parent.coor)
        self.show.showOriginalImage(image)

    def updateParamAnypoint(self):
        self.parent.ui.lineEdit_beta.setText("%.2f" % self.beta)
        self.parent.ui.lineEdit_alpha.setText("%.2f" % self.alpha)
        self.parent.ui.spinBox_zoom.setValue(self.zoom)

    def anypoint_mode_1(self):
        self.parent.anypointState = 0
        self.resetAlphaBeta()
        self.anypoint_view()

    def anypoint_mode_2(self):
        self.parent.anypointState = 1
        self.resetAlphaBeta()
        self.anypoint_view()

    def set_anypoint(self):
        self.parent.alpha = float(self.parent.ui.lineEdit_alpha.text())
        self.parent.beta = float(self.parent.ui.lineEdit_beta.text())
        self.parent.zoom = float(self.parent.ui.spinBox_zoom.text())
        self.anypoint_view()

    def drawPolygon(self, image, mapX, mapY):
        hi, wi = image.shape[:2]
        X1 = []
        Y1 = []
        X2 = []
        Y2 = []
        X3 = []
        Y3 = []
        X4 = []
        Y4 = []

        x = 0
        while x < wi:
            a = mapX[0,]
            b = mapY[0,]
            e = mapX[-1,]
            f = mapY[-1,]

            if a[x] == 0. or b[x] == 0.:
                pass
            else:
                X1.append(a[x])
                Y1.append(b[x])

            if f[x] == 0. or e[x] == 0.:
                pass
            else:
                Y3.append(f[x])
                X3.append(e[x])
            x += 10

        y = 0
        while y < hi:
            c = mapX[:, 0]
            d = mapY[:, 0]
            g = mapX[:, -1]
            h = mapY[:, -1]
            if d[y] == 0. or c[y] == 0.:  # or d[y] and c[y] == 0.0:
                pass

            else:
                Y2.append(d[y])
                X2.append(c[y])

            if h[y] == 0. or g[y] == 0.:
                pass
            else:
                Y4.append(h[y])
                X4.append(g[y])
            y += 10

        p = np.array([X1, Y1])
        q = np.array([X2, Y2])
        r = np.array([X3, Y3])
        s = np.array([X4, Y4])
        points = p.T.reshape((-1, 1, 2))
        points2 = q.T.reshape((-1, 1, 2))
        points3 = r.T.reshape((-1, 1, 2))
        points4 = s.T.reshape((-1, 1, 2))
        # print(self.points)
        cv2.polylines(image, np.int32([points]), False, (0, 255, 0), 10)
        cv2.polylines(image, np.int32([points2]), False, (0, 255, 0), 10)
        cv2.polylines(image, np.int32([points3]), False, (0, 255, 0), 10)
        cv2.polylines(image, np.int32([points4]), False, (0, 255, 0), 10)
        return image
