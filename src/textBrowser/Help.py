from HelpUiShow import Ui_Help
import Image_Source


class Win_Help(Ui_Help):
    def __init__(self, parent_win, parent_dialog):
        # super().__init__(parent_win)

        self.parent_win = parent_win
        self.parent_dialog = parent_dialog

        self.setupUi(self.parent_dialog)
        self.eventButton()
        self.listWidget.setCurrentRow(0)
        self.selectItem()

    def eventButton(self):
        self.listWidget.itemSelectionChanged.connect(self.selectItem)

    def selectItem(self):
        apps = self.listWidget.currentItem().text()
        if apps == '1. Car Safety system':
            self.carSafetysytem()
        elif apps == '2. Tube Inspection':
            self.tubeInsspection()
        elif apps == '3. Survaceilance':
            self.survaceilance()
        elif apps == '4. Colonoscopy':
            self.colonoscopy()
        elif apps == '5. 3D Measurement':
            self.measurement()
        elif apps == '6. 3D Reconstruction':
            self.recontruction()
        elif apps == '7. Visual Odometry':
            self.visualodometry()
        elif apps == '8. Object Detection':
            self.objectdetection()
        elif apps == '9. Face Recognition':
            self.facerecognition()
        elif apps == '10. Setup Center Camera':
            self.setupcentercamera()
        else:
            self.inDEvelopment()

    def carSafetysytem(self):
        self. textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline;\">Car safety system</span></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Automotive safety is the study and practice of design, construction, equipment and regulation to minimize the occurrence and consequences of traffic collisions involving motor vihicles. Road traffic safety more broadly includes roadway design. [<a href=\"https://en.wikipedia.org/wiki/Automotive_safety\"><span style=\" text-decoration: underline; color:#0000ff;\">wiki</span></a>]</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">example:</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/car.png\" /></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

    def tubeInsspection(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Tube Inspection</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    With automation, 3-D optical measurements increasingly replacing the traditionally used techniques in industry, which include mechanical gauging techniques such as the coordinate measurement machine (CMM),2 due to its characteristics of noncontact, non-destruction, high efficiency, and high accuracy.</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    An <span style=\" font-weight:600;\">important application</span> is crack inspection,quality control, installation, and even revamping of an existing pipeline in the oil/gas industry.<a href=\"https://www.spiedigitallibrary.org/journals/optical-engineering?SSO=1\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/internal2.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thread Inspection<a href=\"https://www.spiedigitallibrary.org/journals/optical-engineering?SSO=1\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p></body></html>")

    def survaceilance(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Surveillance</span></a></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:14px; font-weight:600; color:#000000;\">    </span><span style=\" font-weight:600; color:#000000; background-color:transparent;\">Surveillance</span><span style=\" color:#000000; background-color:transparent;\"> is the monitoring of behavior, activities, or information for the purpose of information gathering, influencing, managing or directing. This can include observation from a distance by means of electronic equipment, such as closed-circuit television (CCTV), or interception of electronically transmitted information, such as Internet traffic. It can also include simple technical methods, such as human intelligence gathering and postal interception.</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" font-weight:600; color:#000000; background-color:transparent;\">    Surveillance</span><span style=\" color:#000000; background-color:transparent;\"> is used by governments for intelligence gathering, prevention of crime, the protection of a process, person, group or object, or the investigation of crime. It is also used by criminal organizations to plan and commit crimes, and by businesses to gather intelligence on criminals, their competitors, suppliers or customers. Religious organisations charged with detecting heresy and heterodoxy may also carry out surveillance and Auditors carry out a form of surveillance.</span><a href=\"https://en.wikipedia.org/wiki/Surveillance\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"center\" style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><img src=\":/newPrefix/Security.jpg\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" background-color:#ffffff;\">Fish eye camera for surveillance</span><a href=\"https://www.sourcesecurity.com/insights/omnidirectional-cameras-video-surveillance-benefits-challenges-co-9385-ga-co-9294-ga.20448.html\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p></body></html>")

    def colonoscopy(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Colonoscopy</span></a></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:14px; font-weight:600; color:#000000;\">    Colonoscopy</span><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#000000;\"> (/ˌkɒləˈnɒskəpi/) or coloscopy (/kəˈlɒskəpi/) is the endoscopic examination of the large bowel and the distal part of the small bowel with a CCD camera or a fiber optic camera on a flexible tube passed through the anus. It can provide a visual diagnosis (e.g., ulceration, polyps) and grants the opportunity for biopsy or removal of suspected colorectal cancer lesions.</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:14px; font-weight:600; color:#000000;\">    Colonoscopy</span><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#000000;\"> can remove polyps smaller than one millimeter. Once polyps are removed, they can be studied with the aid of a microscope to determine if they are precancerous or not. It can take up to 15 years for a polyp to turn cancerous.</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:14px; font-weight:600; color:#000000;\">    Colonoscopy</span><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#000000;\"> is similar to sigmoidoscopy—the difference being related to which parts of the colon each can examine. A colonoscopy allows an examination of the entire colon (1200–1500 mm in length). A sigmoidoscopy allows an examination of the distal portion (about 600 mm) of the colon, which may be sufficient because benefits to cancer survival of colonoscopy have been limited to the detection of lesions in the distal portion of the colon.</span><a href=\"https://en.wikipedia.org/wiki/Colonoscopy\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"center\" style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><img src=\":/newPrefix/colonoscopy.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:16px; color:#111111; background-color:#ffffff;\">During a colonoscopy, the doctor inserts a colonoscope into your rectum to check for abnormalities in your entire colon.</span><a href=\"https://www.mayoclinic.org/tests-procedures/colonoscopy/about/pac-20393569#dialogId47046770\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p></body></html>")

    def recontruction(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">3D Reconstruction</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    In computer vision and computer graphics, <span style=\" font-weight:600;\">3D reconstruction </span>is the process of capturing the shape and appearance of real objects. This process can be accomplished either by active or passive methods. If the model is allowed to change its shape in time, this is referred to as non-rigid or spatio-temporal reconstruction.<a href=\"https://en.wikipedia.org/wiki/3D_reconstruction\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    <span style=\" font-weight:600;\">3D reconstruction from multiple images </span>is the creation of three-dimensional models from a set of images. It is the reverse process of obtaining 2D images from 3D scenes. The essence of an image is a projection from a 3D scene onto a 2D plane, during which process the depth is lost. The 3D point corresponding to a specific image point is constrained to be on the line of sight. From a single image, it is impossible to determine which point on this line corresponds to the image point. If two images are available, then the position of a 3D point can be found as the intersection of the two projection rays. This process is referred to as triangulation. The key for this process is the relations between multiple views which convey the information that corresponding sets of points must contain some structure and that this structure is related to the poses and the calibration of the camera.<a href=\"https://en.wikipedia.org/wiki/3D_reconstruction_from_multiple_images\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/3D_Recons.jpeg\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" text-decoration: underline; color:#0000ff;\">[3]</span></a></p></body></html>")

    def measurement(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">3D Measurement</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">    3D measurements </span>is actually one of the most recent technologies used in metrology, which is the science of measurement and the standardization of measurements. The first measurements date back to the ancient Egyptians to facilitate commerce, build infrastructure and record human activity. Modern metrology, however, gets its roots from the French revolution.</p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">    3D measurement </span>is a process in which various types of equipment collect 3D data on physical objects, including their shape, sizes and colours, to construct and analyze digital 3D models with high-density point clouds or triangle meshes.<a href=\"https://www.creaform3d.com/blog/explore-3d-scanners-and-3d-measurement-technologies/\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/measurement.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3D Measurement from 2 images<a href=\"https://www.simpact.co.uk/case-studies/the-application-of-3d-digital-image-correlation-dic-to-blast-load-cases\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p></body></html>")

    def visualodometry(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Visual Odometry</span></a></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" background-color:#ffffff;\">    In robotics and computer vision, </span><span style=\" font-weight:600; background-color:#ffffff;\">visual</span><span style=\" background-color:#ffffff;\"> </span><span style=\" font-weight:600; background-color:#ffffff;\">odometry</span><span style=\" background-color:#ffffff;\"> is the process of determining the position and orientation of a robot by analyzing the associated camera images. It has been used in a wide variety of robotic applications, such as on the Mars Exploration Rovers.</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" background-color:#ffffff;\">    In navigation, </span><span style=\" font-weight:600; background-color:#ffffff;\">odometry</span><span style=\" background-color:#ffffff;\"> is the use of data from the movement of actuators to estimate change in position over time through devices such as rotary encoders to measure wheel rotations. While useful for many wheeled or tracked vehicles, traditional odometry techniques cannot be applied to mobile robots with non-standard locomotion methods, such as legged robots. In addition, odometry universally suffers from precision problems, since wheels tend to slip and slide on the floor creating a non-uniform distance traveled as compared to the wheel rotations. The error is compounded when the vehicle operates on non-smooth surfaces. Odometry readings become increasingly unreliable as these errors accumulate and compound over time.</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; background-color:#ffffff;\">    Visual odometry</span><span style=\" background-color:#ffffff;\"> is the process of determining equivalent odometry information using sequential camera images to estimate the distance traveled. Visual odometry allows for enhanced navigational accuracy in robots or vehicles using any type of locomotion on any surface.</span><a href=\"https://en.wikipedia.org/wiki/Visual_odometry\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/main-slam-kitti-map (1).png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visual Odometry<a href=\"https://en.wikipedia.org/wiki/Visual_odometry\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

    def objectdetection(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Object Detection</span></a></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    </span><span style=\" font-weight:600; background-color:#ffffff;\">Object detection </span><span style=\" background-color:#ffffff;\">is a computer technology related to computer vision and image processing that deals with detecting instances of semantic objects of a certain class (such as humans, buildings, or cars) in digital images and videos. Well-researched domains of object detection include face detection and pedestrian detection. Object detection has applications in many areas of computer vision, including image retrieval and video surveillance.</span></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:#ffffff;\">    It is widely used in computer vision tasks such as image annotation, activity recognition, face detection, face recognition, video object co-segmentation. It is also used in tracking objects, for example tracking a ball during a football match, tracking movement of a cricket bat, or tracking a person in a video.</span><a href=\"https://en.wikipedia.org/wiki/Object_detection\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/objectdetection.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Objects detected</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")

    def facerecognition(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Face Recognition</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    A <span style=\" font-weight:600;\">face reecognition or facial recognition</span> system is a technology capable of matching a human face from a digital image or a video frame against a database of faces, typically employed to authenticate users through ID verification services, works by pinpointing and measuring facial features from a given image.</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    While initially a form of computer application, <span style=\" font-weight:600;\">facial recognition</span> systems have seen wider uses in recent times on smartphones and in other forms of technology, such as robotics. Because computerized facial recognition involves the measurement of a human\'s physiological characteristics facial recognition systems are categorised as biometrics. Although the accuracy of facial recognition systems as a biometric technology is lower than iris recognition and fingerprint recognition, it is widely adopted due to its contactless process. Facial recognition systems have been deployed in advanced human-computer interaction, video surveillance and automatic indexing of images. They are also used widely by law enforcement agencies.<a href=\"https://en.wikipedia.org/wiki/Facial_recognition_system\"><span style=\" text-decoration: underline; color:#0000ff;\">[1]</span></a></p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/recognition.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'proxima-nova,sans-serif\'; font-size:14px; color:#000000;\">Face recognition with OpenCV and Python.</span><a href=\"https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/\"><span style=\" text-decoration: underline; color:#0000ff;\">[2]</span></a></p></body></html>")

    def setupcentercamera(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://medium.com/@dc.aihub/3d-reconstruction-with-stereo-images-part-1-camera-calibration-d86f750a1ade\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\">Setup Center Camera</span></a></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; text-decoration: underline; color:#000000;\"><br /></p>\n"
            "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Before we taking a photo using fish eye camera, we must to setup the position of camera for better result and computation.</p>\n"
            "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/center2.png\" /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Setup Center Camera</p></body></html>")

    def inDEvelopment(self):
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline;\">In Developmnet</span></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/test.png\" /></p></body></html>")
