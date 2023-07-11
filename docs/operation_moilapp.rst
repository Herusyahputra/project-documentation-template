Operation of MoilApp
####################

In this session we will explain the components in the MoilApp application and tutorials on how to use the application.

4.1 Overview of The User Interface
==================================

When you open a project in PyCharm, the default user interface looks as follows:

.. figure:: assets/24.Overview_user_interface_MoilApp_application.png
   :scale: 55 %
   :alt: alternate text
   :align: center

   Overview user interface MoilApp application

Here is detail explanation:

1. Menu bar
-----------

This container stores various button

    - File

      File contains Load image, Load video, Open cam, Cam parameter, Record Video, Save Image, and Exit

    - Window

      Window contains Maximize and Minimize

    - Apps

      Apps contains Add, Open, Delete, Create and Help for Add-Ons

    - Help

      Help contains About Apps, About Us and Accessibility

2. Title application
---------------------

.. raw:: html

   <p style="text-align: justify;">

    This part will give you information about the application name and information about image and video location as a source.</p>

3. Source media button
----------------------

.. raw:: html

   <p style="text-align: justify;">

    This grub contains three buttons: load image, load video and open camera. You can load images and videos from your directory
    and also can get images from your camera by streaming video. On open camera you can use USB Camera and streaming camera.</p>

4. Rotate button
----------------

.. raw:: html

   <p style="text-align: justify;">

    Rotate image to the clockwise and anticlockwise direction.</p>

5. Zoom button
--------------

.. raw:: html

   <p style="text-align: justify;">

    Make the image look bigger or smaller by zoom in and zoom out.</p>

6. Saving button
-----------------

.. raw:: html

   <p style="text-align: justify;">

    Save the resulting image or recording video in your local directory </p>

7. Plugin controller
--------------------

.. raw:: html

   <p style="text-align: justify;">

    The container Plugin controller contains several buttons that have functions to control plugins such as adding, opening and removing plugin
    application from the main application.</p>

8. Information label
--------------------

.. raw:: html

   <p style="text-align: justify;">

    Show the information of the camera type used.</p>

9. Selection mode view
----------------------

.. raw:: html

   <p style="text-align: justify;">

    This container contains several view mode selection buttons including original view, Anypoint view and panoramic view.</p>

10. Help button
---------------

.. raw:: html

   <p style="text-align: justify;">

    Contains several buttons that display information from this application such as manual guide, about us and about MoilApp.</p>

11. Clear media from widget
---------------------------

.. raw:: html

   <p style="text-align: justify;">

    This button will remove all objects such as pixmap images and others from the user interface to make the application look like it was just opened. </p>

12. Extra button
----------------

.. raw:: html

   <p style="text-align: justify;">

    This button will be active when you select Anypoint or panorama view and help you to explore the image.</p>

13. Widget show result image
----------------------------

.. raw:: html

   <p style="text-align: justify;">

    This widget will be showing the result image after processing, this is the main image viewer on the user interface application. </p>

14. Widget to show Image saved
------------------------------

.. raw:: html

   <p style="text-align: justify;">

    Displaying images successfully saved which can then be reopened if your source media is video or camera.</p>

15. Video controller
--------------------

.. raw:: html

   <p style="text-align: justify;">

    The video controller container contains several buttons and labels that function to control media such as start, pause, stop, forward,
    backward, time slider and duration label. </p>

16. Widget show original image
------------------------------

.. raw:: html

   <p style="text-align: justify;">

    This widget serves to display and maintain the original image to provide a reference regarding the process that occurs.</p>

4.2 Open media source
=====================

.. raw:: html

   <p style="text-align: justify;">

    MoilApp provides various sources that can be used for processing, including image files, video files, and cameras both USB cams,
    web cams or streaming cams from raspberry-pi. You only need to press the button according to the media source that you will process
    and the app will open a file explorer dialog like shown below. </p>

.. figure:: assets/25.Open_Image.png
   :scale: 55 %
   :alt: alternate text
   :align: center

   Open Image

.. raw:: html

   <p style="text-align: justify;">

    If you open a video file, you will be asked to choose the type of camera used at the combo box prompt after select file.
    This is useful for loading the camera parameters from the database. </p>

.. figure:: assets/26.Load_Video_file.png
   :scale: 35 %
   :alt: alternate text
   :align: center

   Load Video file

.. raw:: html

   <p style="text-align: justify;">

    To open the camera, there are options, namely usb cam and streaming cam. for USB cameras, you can detect the port to find out which
    port is used and then select it in the combo box, click button “oke” and you will be asked to choose the type of camera used at the
    combo box prompt. as shown in the image below. </p>

.. figure:: assets/27.Open_USB_camera.png
   :scale: 50 %
   :alt: alternate text
   :align: center

   Open USB camera

.. raw:: html

   <p style="text-align: justify;">

    streaming cam option is to open camera from stream server URL which is usually used to access raspberry-pi camera. you only need to provide
    the URL of the camera and press button “oke” like the example below. you will be asked to choose the type of camera used at the combo box prompt.

.. figure:: assets/28.Open_streaming_camera.png
   :scale: 55 %
   :alt: alternate text
   :align: center

   Open streaming camera

If everything goes properly, the user interface will display the image as shown below.

.. figure:: assets/29.image_frame_shown_on_MoilApp.png
   :scale: 35 %
   :alt: alternate text
   :align: center

   image frame shown on MoilApp

.. raw:: html

   <p style="text-align: justify;">

    For media from video and camera we provide controllers such as play, pause, stop, forward, backward and slider timer. where this controller can be used to facilitate image processing.</p>

4.3 Process to Anypoint view
============================

.. raw:: html

   <p style="text-align: justify;">

    To improve the results of observations, sometimes we only want to see areas that have a lot of information. Therefore, we can use the undistortion rectilinear selected image method.
    This method is convert the image plane coordinate to hemispherical coordinates, move the optical axis to the specified zenithal (alpha) and azimuthal (beta) angle [refer to section 1.2]. </p>

.. raw:: html

   <p style="text-align: justify;">

    Anypoint view has 2 modes, where mode 1 is the result rotation from betaOffset degree rotation around the Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). Below is the example of Anypoint result mode-1.</p>

.. figure:: assets/30.Anypoint_view_mode_1.png
   :scale: 35 %
   :alt: alternate text
   :align: center

   Anypoint view mode 1

.. raw:: html

   <p style="text-align: justify;">

    Whereas, for mode -2 the result rotation is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation around the X-axis(pitch). With the results of the image of this process can be seen in the following image. </p>

.. figure:: assets/31.Anypoint_view_mode_2.png
   :scale: 35 %
   :alt: alternate text
   :align: center

   Anypoint view mode 2

.. raw:: html

   <p style="text-align: justify;">

    When you are in Anypoint view mode, you can activate the help button which functions to change from mode 1 to mode 2 or vice versa. This help button also functions to see Anypoint result from a predetermined direction. Below is an overview of the extra button in Anypoint view mode.</p>

.. figure:: assets/32.Extra_buttons_Anypoint_view.png
   :scale: 60 %
   :alt: alternate text
   :align: center

   Extra buttons Anypoint view

4.4 Process to panorama view
=============================

.. raw:: html

   <p style="text-align: justify;">

    As explained earlier, the panorama view may present a horizontal view in a specific immersed environment to meet the common human visual perception. The Figure below shows a diagram of transforming a fisheye image into a panoramic view. </p>

.. figure:: assets/33.Diagram_transforming_panorama_image.png
   :scale: 60 %
   :alt: alternate text
   :align: center

   Diagram transforming panorama image

.. raw:: html

   <p style="text-align: justify;">

    The image below is the result of image processing panorama view. </p>

.. figure:: assets/34.Panorama_view.png
   :scale: 35 %
   :alt: alternate text
   :align: center

   Panorama view

.. raw:: html

   <p style="text-align: justify;">

    You can also change the values of the maximum and minimum FoV via lineedit which will only appear in this mode. The overview of the line edit can be seen in the picture below: </p>

.. figure:: assets/35.Line_edit_Panorama_view.png
   :scale: 90 %
   :alt: alternate text
   :align: center

   Line edit Panorama view

4.5 Save image and record video
===============================

a. Save image
-------------

.. raw:: html

   <p style="text-align: justify;">

    You can save the original image or result image by pressing the save image button or by right clicking the mouse on the result image and selecting save image. at the first time you will save the image, application will open dialog to directed to choose the directory will use as storage.  </p>

.. figure:: assets/36.Select_folder_to_save_file.png
   :scale: 50 %
   :alt: alternate text
   :align: center

   Select folder to save file

.. figure:: assets/37.File_saved.png
   :scale: 35 %
   :alt: alternate text
   :align: center

   File saved

b. Record video
----------------

.. raw:: html

   <p style="text-align: justify;">

    If you want to record a video you can press the record button, the process is almost the same as saving an image.
    Before starting recording, you will be directed to choose a directory and the video files will be saved in that folder. </p>

4.6 Camera parameters
=====================

.. raw:: html

   <p style="text-align: justify;">

    Camera parameter is a very important component in fisheye image processing. Each fisheye camera can be calibrated and
    derives a set of parameters by MOIL laboratory before the successive functions can work correctly, configuration is necessary
    at the beginning of the program. MoilApp provides a form dialog that can add, modify, and delete parameters that will be stored in the database.
    To be able to use this feature, please click on File >> Camera Parameters. The overview of this form shown like picture below: </p>

.. figure:: assets/38.Camera_parameters_form.png
   :scale: 70 %
   :alt: alternate text
   :align: center

   Camera parameters form

.. raw:: html

   <p style="text-align: justify;">

    If you want to see the parameter, you can list the camera type from comboBox list parameter, and will display like figure below: </p>

.. figure:: assets/39.Show_camera_parameters.png
   :scale: 70 %
   :alt: alternate text
   :align: center

   Show camera parameters

The following is the use of this feature in detail

a. Add camera parameters
-------------------------

.. raw:: html

   <p style="text-align: justify;">

    If you are using a camera whose parameters are not yet available in the database, you can add them. you just need to write all the parameters on the form, then click the "new" button. after that the data will be saved and you can use the camera parameters.</p>


.. figure:: assets/parameters.png
   :scale: 120 %
   :alt: alternate text
   :align: center

   New parameters saved

.. figure:: assets/41.New_parameters_saved.png
   :scale: 60 %
   :alt: alternate text
   :align: center

   Operations of the MoilApp

b. Modify camera parameters
----------------------------

.. raw:: html

   <p style="text-align: justify;">

    If you want to change the value of the parameter, you can modify it. select the camera type in the list parameter combobox,
    then you enter the new parameter value. click the update button and the modified parameters will be saved in the database. </p>

.. figure:: assets/modify.png
   :scale: 120 %
   :alt: alternate text
   :align: center

   Operations of the MoilApp

c. Delete camera parameters
---------------------------

.. raw:: html

   <p style="text-align: justify;">

    You can also delete parameters by pressing the delete button on the selected parameter list.</p>

.. figure:: assets/43.Delete_camera_parameters.png
   :scale: 65 %
   :alt: alternate text
   :align: center

   Delete camera parameters

4.7 Mouse event action
======================

.. raw:: html

   <p style="text-align: justify;">

    There are several functions of the mouse event that you can use to speed up work. The mouse event will only work on the result image and the original image of the user interface widget. Some of the mouse event's functions including: </p>

a. Mouse click event
--------------------

.. raw:: html

   <p style="text-align: justify;">

    Mouse click event works only on the original image widget when Anypoint mode. This handy determine the coordinates of points that will be converted to alpha beta value. which then this value will be a parameter in converting the original image to Anypoint image.</p>

b. Mouse press-move event
--------------------------

.. raw:: html

   <p style="text-align: justify;">

    The mouse press event has its own function in each image widget, in the original image this widget works in Anypoint mode which allows for surrounding views. Different functions if you press the press-move mouse event on the result image widget, you can enlarge the area you are
    interested in using this function and its work in all mode view, for the example shown in the image below: </p>

.. figure:: assets/44.Mouse_Pres-move_event.png
   :scale: 40 %
   :alt: alternate text
   :align: center

   Mouse Pres-move event

.. figure:: assets/45.Enlarge_view_selected_area.png
   :scale: 40 %
   :alt: alternate text
   :align: center

   Enlarge view selected area

c. Double click event
----------------------

.. raw:: html

   <p style="text-align: justify;">

    The Double click mouse event has function to reset Anypoint view to default in Anypoint mode. </p>

d. Right click event
---------------------

.. raw:: html

   <p style="text-align: justify;">

    If you right click on the mouse, it will display menu options like maximized, minimized, save image and show info.</p>

e. Wheel event
---------------

.. raw:: html

   <p style="text-align: justify;">

    Wheel event will work by pressing the ctrl key simultaneously to zoom in and zoom out images on the user interface display. </p>

4.8 MoilApp keyboard shortcut
==============================

.. raw:: html

   <p style="text-align: justify;">

    MoilApp has keyboard shortcuts for most of its commands related to processing and other tasks. Memorizing these hotkeys can help you stay more productive
    by keeping your hands on the keyboard. The following table lists some of the most useful shortcuts to learn: </p>

