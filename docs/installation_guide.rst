Moilapp Installation Guide
##########################

.. raw:: html

   <p style="text-align: justify;">

   <i>This guide provides step-by-step instructions to install and run the <b>MoilApp repository</b> on <b>Ubuntu 20.04</b> with Python <b>version > 3.7.</b></i></p>

Clone this Repository
-----------------------
.. raw:: html

   <p style="text-align: justify;">

   1. Use the <i>"git clone"</i> command to <i>download</i> the code from the repository to your local machine.</p>

.. code-block:: bash

   $ git clone https://github.com/McutOIL/moilapp.git --branch=develop_v4.1

Change Working Directory
--------------------------

.. raw:: html

   <p style="text-align: justify;">

   2. After <b>successfully</b> cloning the repository, change working directory by using the command line below and the try to
   install <b>. build.sh</b>file to install all <i>dependencies library</i>.</p>

.. code-block:: bash

    $ cd moilapp

    $ . build.sh

.. raw:: html

    <p style="text-align: justify;">

    <i>In case the command <b>. build.sh </b> above is installed <b>Successfully,</b> you can proceed to part <i>Run the Application</i>. Nevertheless, if the
    installation fails, you can install manually by referring to section <i>Set up Virtual Environment</i> below.</i></p>

Set up Virtual Environment
---------------------------

.. raw:: html

   <p style="text-align: justify;">

   3. Two ways to build a <i>virtual environment</i> are: installing it in general or specifically for Python. Use the provided
   command to prevent installation errors and ensure that dependencies required for each project are installed without
   interfering with other projects or the system's Python installation. <i>A virtual environment</i> helps developers maintain
   project stability and avoid compatibility issues between package versions.</p>

.. code-block:: bash

    $ sudo apt install virtualenv

    $ virtualenv venv

    or

    $ python3.8 -m venv venv

.. raw:: html

   <p style="text-align: justify;">

   <i>Note: you can change the python version ex: <b>*python3.8, python3.9, python3.10</b></i></p>

.. raw:: html

   <p style="text-align: justify;">

   4. To start using the virtual environment, you need to <i>activate</i> it. You can do this by running the activate script located in the `bin` directory of your virtual environment. On Linux, use the following command: </p>

.. code-block:: bash

    $ source venv/bin/activate

.. raw:: html

   <p style="text-align: justify;">

    5. Before installation the library requirements you should be to <b>upgrade</b> an existing package <b>PIP</b> to the latest version,
    you can use the command.</p>

.. code-block:: bash

    $ pip install --upgrade pip

.. raw:: html

   <p style="text-align: justify;">

   Followed by the name of the package. This command will download and install the latest version of the package,
   replacing the older version that was previously installed.</p>

   <p> 6. With the environment activated, you can install all required packages. The packages will be installed in the
   virtual environment and will not affect the global Python installation.</p>

.. code-block:: bash

    $ pip install -r requirements.txt

Run the Application
-------------------

.. raw:: html

   <p style="text-align: justify;">

   7. After all ready, run the main program in `src` directory, on your terminal you can type this command to run the project

.. code-block:: bash

    $ cd src

    $ python3 main.py

.. raw:: html

   <p style="text-align: justify;">

   <i>That's it! You should now have the <b>McutOIL/moilapp repository</b> installed and ready to use on your <b>Ubuntu 20.04 or 22.04 LTS</b> machine.</i></p>