Plugin Extention
################

Introduction
============

.. raw:: html

   <p style="text-align: justify;">

    MoilApp V4.0 is an application with an MVC (Model-View-Controller) architecture design. However, in the current MoilApp V4.1 version,
    MoilApp has implemented a slightly different MVC model using the Plugin model type. This new model can be used to control
    other application plugins. For instance, Plugin model 1 can control plugins 1, 2, and 3, whereas Plugin model 2 can only control
    plugins 2, 3, and N. Similarly, Plugin model N can only control plugins 3 and N. This implementation was done because the
    plugin concept is independent, and each plugin can have its own specific requirements or models. However, the MoilApp dashboard
    can still control multiple plugins based on the requirements or models used for a particular application plugin. In this way,
    MoilApp can provide better flexibility and control to the user while maintaining the overall architecture design.
    To summarize, MoilApp V4.1 now utilizes a Plugin model type, which allows for better control and flexibility over the
    various application plugins, while still maintaining the overall MVC architecture design.</p>

.. figure:: assets/1.plugin-arc.png
   :scale: 70 %
   :alt: alternate text
   :align: center

   Design the MoilApp plugin

Prerequisites
==============

Before proceeding with this guide, make sure that:

    - *You have a basic understanding of Python and PyQt.*
    - *You have installed the Qt Designer tool.*
    - *You have installed the PyQt5 library.*
    - *You have cloned the MoilApp repository from GitHub.*

Action Plugin
--------------

.. raw:: html

   <p style="text-align: justify;">

    The MoilApp program includes a plugin notion that is integrated into its design, featuring a menu bar and a button.
    Containers that are dedicated to managing the plugin application. The interface is depicted in the following illustration:</p>

.. raw:: html

   <p style="text-align: justify;">

    - <i>Adding a plugin app</i><br>

      To include your own plugin application, access the app's folder from the controller in the plugin and add your app.
      If your app adheres to the specified format and is successfully added, it will be accessible through the plugin and can be executed.</p>

.. raw:: html

   <p style="text-align: justify;">

   - <i>Installing the app</i><br>

     You can use the plugin store icon to install the provided application.<//p>

.. raw:: html

   <p style="text-align: justify;">

   - <i>Opening the plugin application</i><br>

     You can open the plugin you have installed by selecting it in the combo box and pressing the Open Plugins button.

.. raw:: html

   <p style="text-align: justify;">

   - <i>Deleting a plugin app</i><br>

     To remove a plugin application from the MoilApp program, you need to access the plugin controller container and
     Click on the <b><i>"Delete"</i></b> button. This action will prompt a confirmation dialog to ensure that you want to proceed with
     the deletion.  If you confirm the deletion, the plugin application will be removed from the list of available applications in the combo box.</p>

GitHub Operation
=================

.. raw:: html

    <p style="text-align: justify;">

    To publish the new application from the local branch to the repository group, the user must first create a fork on their
    own <b><i>GitHub account</i></b>. After that, they can use the MoilApp plugin to create a new application.</p>

Do Fork Repository
-------------------

.. raw:: html

   <p style="text-align: justify;">

    Making a note of the name of the repository you wish to share on your GitHub account is the first step.
    You can click the <b>"Fork"</b> button in the top right corner of the screen once you have arrived at the repository's
    GitHub page.  The repository will be duplicated in your personal GitHub account as a result.<br>

    To make sure that just the main branch of the repository is cloned, it is crucial to select <b>"Copy Main Only."</b>
    option when creating the fork. The confirmation window that opens when you click the <b>"Fork"</b> button typically has
    this option.  You may be sure that any alterations or updates you make to the repository will take effect by simply
    duplicating the <i>main branch.</i></p>

.. figure:: assets/7.fork.png
   :scale: 50 %
   :alt: alternate text
   :align: center

   Fork the repository

Do Create New Branch
--------------------

.. raw:: html

   <p style="text-align: justify;">

    To avoid conflicts between your changes and the updates made to the original MoilApp repository, it is recommended that
    You create a new branch under the <b>"develop"</b> branch after cloning the MoilApp repository. This way, you can work on your
    changes in isolation without affecting the original codebase or interfering with updates to the develop branch in the original repository.</p>

.. figure:: assets/8.new-branch.png
   :scale: 55 %
   :alt: alternate text
   :align: center

   Create new branch on your branch

Create Plugin Application
=========================

.. raw:: html

   <p style="text-align: justify;">

    To build an application with an <b>API</b>, you need to create a program that can interact with the API to exchange data and
    perform functions.  <b>APIs</b> provide protocols and tools that enable different software applications to communicate with each other.</p>

Design User Interface
---------------------

.. raw:: html

   <p style="text-align: justify;">

    To develop an application, you start by designing the user interface using Qt Designer. If you don't have this tool,
    installed on your computer, please install it first. Once you have designed the interface, you need to convert the <b>*.ui</b>
    file to a <b>*.py</b> file, which can be done as follows:</p>


.. figure:: assets/2.create-user-interface.png
   :scale: 50 %
   :alt: alternate text
   :align: center

   Create User Interface

Plugin Interface (API)
-----------------------

.. raw:: html

   <p style="text-align: justify;">

    A plugin interface is an <b>API</b> that connects the main application with the plugin widget. It allows you to create custom
    user interfaces and use models from the main app without starting from scratch.</p>

.. figure:: assets/3.api.png
   :scale: 55 %
   :alt: alternate text
   :align: center

   Plugin Interface (API)

.. raw:: html

   <p style="text-align: justify;">

    The purpose of this class is to define an interface that can be implemented by plugins in various applications.
    By default, the <i>"description"</i> attribute of the object's init method is set to <i>"UNKNOWN."</i>

    These are the methods that concrete subclasses of the <b>"Plugin"</b> class should implement:</p>

- **Set_plugin_widget:** This method should establish a plugin widget based on a *Model* object that is passed in as input.

- **Set_icon_apps:** This method should determine the plugin application's icon.

- **Change_stylesheet:** This method should modify the plugin applications's CSS.

.. raw:: html

   <p style="text-align: justify;">

    By default, the <b>always_pop_up</b> method of the <b>Plugin</b> class returns the boolean value <b>False</b>, meaning that the plugin does not always pop up.

How to Add an Icon on MoilApp Plugin
-------------------------------------

.. raw:: html

   <p style="text-align: justify;">

    In the code, we import the PluginInterface and define a class MyPlugin that inherits from PluginInterface.
    We then define the <i>set_icon_apps</i> function, which simply returns the name of the icon file that we want to use.
    You can replace <b>"my_icon_file.png"</b> with the name of your own icon file.</p>

.. figure:: assets/4.add-icon.png
   :scale: 60 %
   :alt: alternate text
   :align: center

   Add icon on MoilApp

How to Open Image on User Interface
-----------------------------------

.. raw:: html

   <p style="text-align: justify;">

    <b>Import Ui_form</b> so that the Python file that you have converted from <b>*.ui</b> to <b>*.py</b> can be integrated into a Python
    function such as the class attribute integrated in the Python function below.</p>

.. figure:: assets/5.add-image-ui.png
   :scale: 55 %
   :alt: alternate text
   :align: center

   Add action push button to load image

Showing on User Interface (Hello World)
------------------------------------------

.. raw:: html

   <p style="text-align: justify;">

    Once the program is running, you should be able to interact with the user interface as designed and test its
    functionality. if any issued or errors arise, you may need to review the code and make adjustments as necessary,
    as shown in the user interface below.</p>

.. figure:: assets/6.show-ui.png
   :scale: 50 %
   :alt: alternate text
   :align: center

   Show in user interface

Publish Your Project
====================

.. raw:: html

   <p style="text-align: justify;">

    Refer to the User Operation section to understand more details about the repository project.</p>

Push your Project to GitHub
----------------------------

.. raw:: html

   <p style="text-align: justify;">

    To upload your project, you need to first convert it to <b>"*.zip"</b> format and ensure that it does not contain unwanted
    files like <i>PyCache, Ideas, etc</i>. The User also execute a few terminal commands to complete the upload process.</p>

.. code-block:: bash

    git add .
    git commit -m "commit your project"
    git push -u origin "your branch"

.. raw:: html

   <p style="text-align: justify;">

    After completing the changes, you can <i>submit a pull request</i> to merge your changes into the original repository.
    The project management team will then review your changes and decide whether to approve them for merging or request further revisions.</p

.. figure:: assets/9.push.png
   :scale: 70 %
   :alt: alternate text
   :align: center

   Push your project on repository


Tutorial Develop Apps use MoilApp
=================================

.. raw:: html

   <p style="text-align: justify;">

    MoilApp is an open-source software that is designed to develop applications using the <b>Python programming language</b>.
    It provides a set of tools and libraries that allow developers to create desktop applications with graphical user interface
    (GUIs) quickly and easily. Here's <i>tutorial</i> on how to develop apps using MoilApp version 4.0 or version 4.1:</p>


.. raw:: html

   <iframe width="680" height="315" src="https://www.youtube.com/embed/vTyTqT4yXLM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Note Information
-----------------

- If you want to create your own plugin application, you can follow the tutorial in **section 6.2**.
- Tutorial how to operate MoilApp can watch here: https://youtu.be/ExeY8Q6QNf8
- Suppose you have any issue or want to contribute to this project, you can open issue in GitHub repository and you can ask for pull request.

