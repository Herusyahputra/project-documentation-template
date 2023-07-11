Debian package Distribution
###########################

.. raw:: html

   <p style="text-align: justify;">

    <b>Install using Debian package Distribution</b></p>

.. raw:: html

   <p style="text-align: justify;">

    The release of the MoilApp application is now available, you can easily download and install it on your computer without experiencing any difficulties.
    In the process of packaging this application, we use the fman build system (fbs) platform where It takes the source code and turns it into a standalone executable on Windows,
    Mac or Linux. On Linux OS, the standalone executable will be in the form of a file with a Debian package (.deb) extension. Debian packages are standard Unix ar archives that
    include two tar archives. One archive holds the control information and another contains the installable data. </P>

.. raw:: html

   <p style="text-align: justify;">

    You can find the MoilApp installer on the GitHub release at the following link: https://github.com/MoilOrg/MoilApp/releases/tag/V.3.1.  </p>

.. figure:: assets/60.MoilApp_Release.png
   :scale: 70 %
   :alt: alternate text
   :align: center

   MoilApp Release

.. raw:: html

   <p style="text-align: justify;">

    <b>1. Installation guide:</b></p>

.. raw:: html

   <p style="text-align: justify;">

    Download the MoilApp.deb from release on GitHub, you can do it manually by visit the link or use command line from terminal in your Linux: </p>

.. raw:: html

   <p style="text-align: justify;">

    <b>2. Using wget</b></p>

.. code-block:: bash

    $ wget https://github.com/MoilOrg/MoilApp/releases/download/V.3.1/MoilApp.deb

.. raw:: html

   <p style="text-align: justify;">

    Using Curl</p>

.. code-block:: bash

    $ curl -L https://github.com/MoilOrg/MoilApp/releases/download/V.3.1/MoilApp.deb > MoilApp.deb

.. raw:: html

   <p style="text-align: justify;">

    <b>2. There are two ways to install the application, that is:</b></p>


- Simply Right click on the .deb file, and choose Open With Software Install->Install.</p>

- Alternatively, you can also install a .deb file by opening a terminal and typing:</p>

.. code-block:: bash

    $ sudo dpkg -i MoilApp.deb

.. raw:: html

   <p style="text-align: justify;">

    <b>3. Uninstall the apps</b></p>

You can easly uninstall this app using command line:

.. code-block:: bash

    $ sudo dpkg --purge MoilApp

    Remove the cache

.. code-block:: bash

    $ sudo rm -r /opt/MoilApp

.. raw:: html

   <p style="text-align: justify;">

    <b>4. Reference</b>

C. Chuang-jan and Jan Gwo-Jen, “METHOD FOR PRESENTING FISHEYE-CAMERAMAGES,” US 7,042,508 B2, 2006.

- https://www.borrowlenses.com/blog/rectilinear-fisheye-wide-angle-lens/

- https://build-system.fman.io/pyqt5-tutorial

- https://zetcode.com/gui/pyqt5/

- https://www.tutorialspoint.com/pyqt5/index.htm

- https://betterprogramming.pub/speed-up-your-python-codebases-with-c-extensions-94859875eb70