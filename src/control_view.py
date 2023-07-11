class ManipulateView(object):
    def __init__(self, main_controller):
        self.parent = main_controller

    def zoom_in(self):
        """
        Zoom in image on result label

        """
        if self.parent.image is not None:
            if self.parent.width_result_image > 6000:
                pass
            else:
                self.parent.width_result_image += 100
            self.parent.showToWindow()
            self.parent.show_percentage()

    def zoom_out(self):
        """
        Zoom out image on result label

        """
        if self.parent.image is not None:
            if self.parent.width_result_image < 800:
                pass
            else:
                self.parent.width_result_image -= 100
            self.parent.showToWindow()
            self.parent.show_percentage()

    def rotate_left(self):
        """
        Rotate image in anti clockwise.

        """
        if self.parent.image is not None:
            if self.parent.angle == 180:
                pass
            else:
                self.parent.angle += 10
            self.parent.showToWindow()

    def rotate_right(self):
        """
        Rotate image in clockwise.

        """
        if self.parent.image is not None:
            if self.parent.angle == 180:
                pass
            else:
                self.parent.angle -= 10
            self.parent.showToWindow()
