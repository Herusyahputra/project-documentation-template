import cv2
from ShowResult import ShowImageResult
from imutils import contours, grab_contours
import imutils
import numpy as np


class Object_detection:
    def __init__(self, mainWindow):
        self.parent = mainWindow
        self.show = ShowImageResult(self.parent)
        self.parent.ui.horizontalSlider_GausialBlur.setRange(1, 27)
        self.parent.ui.horizontalSlider_GausialBlur.setValue(15)
        self.parent.ui.label_55.setText("15")
        self.gausian_filter = self.parent.ui.horizontalSlider_GausialBlur.value()
        self.parent.ui.horizontalSlider_Opening.setValue(26)
        self.parent.ui.label_107.setText("26")
        self.parent.ui.horizontalSlider_Opening.setRange(0, 50)
        self.kernel_opening = self.parent.ui.horizontalSlider_Opening.value()
        self.parent.ui.doubleSpinBox_contrastAlpha.setValue(3.85)
        self.alpha_contrast = self.parent.ui.doubleSpinBox_contrastAlpha.value()
        self.parent.ui.spinBox_contrastBeta.setValue(-95)
        self.beta_contrast = self.parent.ui.spinBox_contrastBeta.value()
        self.parent.ui.thresholdHeight.setValue(300)
        self.maxHeightValue_object = self.parent.ui.thresholdHeight.value()
        self.parent.ui.thresholdWindth.setValue(300)
        self.maxWidthValue_object = self.parent.ui.thresholdWindth.value()
        self.parent.ui.doubleSpinBox_contrastGamma.setValue(1.5)
        self.maxRatioValue_object = self.parent.ui.doubleSpinBox_contrastGamma.value()
        self.parent.ui.horizontalSlider_GausialBlur.valueChanged.connect(self.gausianValue)
        self.parent.ui.horizontalSlider_Opening.valueChanged.connect(self.openingValue)
        self.parent.ui.doubleSpinBox_contrastAlpha.valueChanged.connect(self.alphaValue)
        self.parent.ui.spinBox_contrastBeta.valueChanged.connect(self.betaValue)
        self.parent.ui.doubleSpinBox_contrastGamma.valueChanged.connect(self.gammaValue)
        self.parent.ui.thresholdWindth.valueChanged.connect(self.maxWidthValue)
        self.parent.ui.thresholdHeight.valueChanged.connect(self.maxHeightValue)
        self.parent.ui.thresholdRatio.valueChanged.connect(self.maxRatioValue)

    def gausianValue(self, value):
        if self.parent.image is None:
            pass
        else:
            if value % 2 == 1:
                self.gausian_filter = value
                self.parent.ui.label_55.setText(str(value))
                self.detectObject()

    def openingValue(self, value):
        if self.parent.image is None:
            pass
        else:
            self.kernel_opening = value
            self.parent.ui.label_107.setText(str(self.kernel_opening))
            self.detectObject()

    def alphaValue(self):
        if self.parent.image is None:
            pass
        else:
            self.alpha_contrast = self.parent.ui.doubleSpinBox_contrastAlpha.value()
            self.detectObject()

    def betaValue(self):
        if self.parent.image is None:
            pass
        else:
            self.beta_contrast = self.parent.ui.spinBox_contrastBeta.value()
            self.detectObject()

    def gammaValue(self):
        if self.parent.image is None:
            pass
        else:
            self.gamma_contrast = self.parent.ui.doubleSpinBox_contrastGamma.value()
            self.detectObject()

    def maxHeightValue(self):
        if self.parent.image is None:
            pass
        else:
            self.maxHeightValue_object = self.parent.ui.thresholdHeight.value()
            self.detectObject()

    def maxWidthValue(self):
        if self.parent.image is None:
            pass
        else:
            self.maxWidthValue_object = self.parent.ui.thresholdWindth.value()
            self.morp_image()

    def maxRatioValue(self):
        if self.parent.image is None:
            pass
        else:
            self.maxRatioValue_object = self.parent.ui.thresholdRatio.value()
            self.detectObject()

    def detectObject(self):
        if self.parent.image is None:
            self.parent.ui.frame_8.setDisabled(True)
        else:
            self.parent.ui.frame_8.setDisabled(False)
            if self.parent.ui.checkPanorama.isChecked():
                result = self.parent.anypoint_Image
            elif self.parent.ui.checkAnypoint.isChecked():
                result = self.parent.panorama_Image
            else:
                result = self.parent.image.copy()
            self.morphImage = self.detector(result, self.kernel_opening, self.gausian_filter,
                                                 self.alpha_contrast, self.beta_contrast, self.maxWidthValue_object,
                                                 self.maxHeightValue_object, self.maxRatioValue_object)
            self.show.showOriginalImage(self.parent.image)
            self.show.showResult(self.morphImage)

    def detector(self, image, kernel_opening, gaussian_filter, alpha_contrast, beta_contrast, maxWidth, maxHeight,
                      ratio):
        """
        object detection function
        """
        kernel = np.ones((kernel_opening, kernel_opening), np.uint8)
        new_image = cv2.convertScaleAbs(image, alpha=alpha_contrast, beta=beta_contrast)
        gray = cv2.cvtColor(new_image, cv2.IMREAD_GRAYSCALE)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.GaussianBlur(opening, (gaussian_filter, gaussian_filter), 0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges
        edged = cv2.Canny(gray, 50, 150)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = grab_contours(cnts)
        # sort the contours from left-to-right and initialize the bounding box
        # point colors
        (cnts, _) = contours.sort_contours(cnts)
        colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
        # loop over the contours individually
        for (i, c) in enumerate(cnts):
            # if the contour is not sufficiently large, ignore it
            if cv2.contourArea(c) < 100:
                continue
            # compute the rotated bounding box of the contour, then
            # draw the contours
            box = cv2.minAreaRect(c)
            (x, y), (w, h), angle = box
            if w > maxWidth or w < 100:
                continue
            if h > maxHeight or h < 100:
                continue
            if w / h > ratio or h / w > ratio:
                continue
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")
            cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
            cv2.putText(image, "H=" + str(round(h)) + "px", (int(x - 40), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0),
                        2)
            cv2.putText(image, "W=" + str(round(w)) + "px", (int(x - 40), int(y + 40)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
        return image
